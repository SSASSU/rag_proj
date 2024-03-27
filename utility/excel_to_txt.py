import openpyxl

def extract_text_from_excel(excel_file, text_file):

    wb = openpyxl.load_workbook(excel_file)
    sheet = wb.active

    with open(text_file, 'w', encoding='utf-8') as f:
        for row in sheet.iter_rows(values_only=True):
            doc_type, title, category, question, content = row[:5]
            
            f.write(f"[{doc_type}]->[{title}]->[{category}]->{question}\n\n")
            f.write(f"{content}\n\n\n")

# 엑셀 파일 경로와 텍스트 파일 경로 지정
excel_file = "sample.xlsx"
text_file = "output.txt"

# 텍스트 추출 함수 호출
extract_text_from_excel(excel_file, text_file)
