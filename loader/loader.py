import os
import numpy as np
import pandas as pd
import asyncio
import pdfplumber
import pymupdf

# INFO: only support PDF
class DocumentLoader():
    def __init__(self):
        pass

    async def autoloading(self, fpath):
        output = {"meta": {}, "data": {}}

        # check extension of file
        if (fpath.lower().split(".")[-1] == "pdf"):
            pass
        else:
            return None
        
        try:
            # for text extraction
            doc_pdfplumber = pdfplumber.open(fpath)
        except Exception as e:
            print(e)
            return None
        try:
            # for table extraction
            doc_pymupdf = pymupdf.open(fpath)
        except Exception as e:
            print(e)
            return None
        
        # === extraction ===
        try:
            # get metadata
            output["meta"] = doc_pymupdf.metadata
            # get table of contents
            toc = self.create_toc_table(doc_pymupdf)
            # await asyncio.to_thread(self.create_toc_table, doc_pymupdf)
            for page_number, page in enumerate(doc_pdfplumber.pages):
                output["data"][page_number] = {"width": 0.0, "height": 0.0, "pixel": None, "toc": None, "text": {}, "table": []}
                # page info
                output["data"][page_number]["width"] = page.width
                output["data"][page_number]["height"] = page.height
                output["data"][page_number]["pixel"] = doc_pymupdf[page_number].get_pixmap().tobytes()
                output["data"][page_number]["toc"] = toc.get(page_number, "")
                # text
                output["data"][page_number]["text"] = [{k.replace("top", "y0").replace("bottom", "y1"): v for k, v in i.items()} for i in page.extract_text_lines(keep_blank_chars=True, use_text_flow=True, strip=False, return_chars=False)]
                # table
                output["data"][page_number]["table"] = [i.to_markdown() for i in doc_pymupdf[page_number].find_tables()]
        except Exception as e:
            print(e)
            return None
        finally:
            doc_pdfplumber.close()
            doc_pymupdf.close()

        return output

    def get_recursive_toc(self, df, i, container):
        container.append(f'depth={df["depth"].iloc[i]}&title={df["text"].iloc[i]}')
        init_loc = np.where(df["depth"] == (df["depth"].iloc[i] - 1))[0]
        init_loc = init_loc[init_loc < i]
        if (not ((df["depth"].iloc[i] == 1) or (i == 0))) and (len(init_loc) > 0):
            self.get_recursive_toc(df, init_loc[-1], container)
        return container

    def agg_toc_by_page(self, x):
        tmp = []
        for i in x:
            tmp.extend(i.split("|"))
        return "|".join(pd.Series(tmp).drop_duplicates().to_list())

    def create_toc_table(self, doc: pymupdf.Document):
        # 목차 가져오기
        toc = doc.get_toc()
        toc = pd.DataFrame(toc, columns=["depth", "text", "page_number"])
        toc["page_id"] = toc["page_number"] - 1
        # 계층적으로 할당된 목차를 recursive 함수를 통해 모두 결합
        toc["concat"] = ["|".join(self.get_recursive_toc(toc, i, [])[::-1]) for i in range(len(toc))]
        # 페이지에 다중으로 할당되어 있는 목차 데이터를 모두 하나로 결합
        toc = toc.groupby("page_id", sort=False)["concat"].apply(self.agg_toc_by_page)
        return toc
