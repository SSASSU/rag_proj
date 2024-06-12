import re
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
from langchain_text_splitters.character import RecursiveCharacterTextSplitter

class TextPreprocessor():
    def __init__(self, default_text="내용없음", only_korean_lines=True):
        self.default_text = default_text
        self.only_korean_lines = only_korean_lines

    def run(self, text):
        if isinstance(text, str):
            text = ILLEGAL_CHARACTERS_RE.sub('', text)
            text = re.sub(r'[\t]', ' ', text)
            text = re.sub(r'[\r\f\v]', '', text)
            text = re.sub(r' {2,}', ' ', text)
            text = re.sub(r'\n +\n', '\n\n', text)
            text = re.sub(r'\n{3,}', '\n\n', text)
            text = text.strip()
            # at least, korean more than 0
            if self.only_korean_lines:
                text = "\n".join([i for i in text.split("\n") if re.search(r'[가-힣]', i)])
            text = text.strip()
            text = self.default_text if len(text) == 0 else text
            return text
        elif isinstance(text, list):
            text = [ILLEGAL_CHARACTERS_RE.sub('', i) for i in text]
            text = [re.sub(r'[\t]', ' ', i) for i in text]
            text = [re.sub(r'[\r\f\v]', '', i) for i in text]
            text = [re.sub(r' {2,}', ' ', i) for i in text]
            text = [re.sub(r'\n +\n', '\n\n', i) for i in text]
            text = [re.sub(r'\n{3,}', '\n\n', i) for i in text]
            # at least, korean more than 0
            if self.only_korean_lines:
                text = ["\n".join([j for j in i.split("\n") if re.search(r'[가-힣]', j)]) for i in text]
            text = [i.strip() for i in text]
            text = [self.default_text if len(i) == 0 else i for i in text]
            return text
        else:
            return None

class TextSplitter():
    def __init__(self, min_chunk_length=3):
        self.min_chunk_length = min_chunk_length

    def recursive_splitter(self, text, splitter_params={"chunk_size": 200, "chunk_overlap": 100}):
        splitter = RecursiveCharacterTextSplitter(**splitter_params)
        if isinstance(text, str):
            chunks = [chunk for chunk in splitter.split_text(text) if len(chunk) >= self.min_chunk_length]
            output = list(zip(range(len(chunks)), chunks))
            return output
        elif isinstance(text, list):
            output = []
            for i in text:
                chunks = [chunk for chunk in splitter.split_text(i) if len(chunk) >= self.min_chunk_length]
                output.append(list(zip(range(len(chunks)), chunks)))
            return output
        else:
            return None
