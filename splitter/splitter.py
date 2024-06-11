import re
from langchain_text_splitters.character import RecursiveCharacterTextSplitter

class TextPreprocessor():
    def __init__(self, default_text="내용없음"):
        self.default_text = default_text

    def run(self, text):
        if isinstance(text, str):
            text = re.sub(r'[\t\r\f\v]', '', text)
            text = re.sub(r'[\t]', ' ', text)
            text = re.sub(r'\n{3,}', '\n\n', text)
            text = re.sub(r' {2,}', ' ', text)
            text = text.strip()
            text = self.default_text if len(text) == 0 else text
            return text
        elif isinstance(text, list):
            text = [re.sub(r'[\t\r\f\v]', '', i) for i in text]
            text = [re.sub(r'[\t]', ' ', i) for i in text]
            text = [re.sub(r'\n{3,}', '\n\n', i) for i in text]
            text = [re.sub(r' {2,}', ' ', i) for i in text]
            text = [i.strip() for i in text]
            text = [self.default_text if len(i) == 0 else i for i in text]
            return text
        else:
            return None

class TextSplitter():
    def __init__(self, min_chunk_length=3):
        self.min_chunk_length = min_chunk_length

    def rc_splitter(self, text, splitter_params={}):
        splitter = RecursiveCharacterTextSplitter(**splitter_params)
        output = []
        if isinstance(text, str):
            output = [(chunk_id, chunk) for chunk_id, chunk in enumerate(splitter.split_text(text)) if len(chunk) >= self.min_chunk_length]
            return output
        elif isinstance(text, list):
            for i in text:
                output.append([(chunk_id, chunk) for chunk_id, chunk in enumerate(splitter.split_text(i)) if len(chunk) >= self.min_chunk_length])
            return output
        else:
            return None
        
    def rc_splitter(self, text, splitter_params={}):
        splitter = RecursiveCharacterTextSplitter(**splitter_params)
        output = []
        if isinstance(text, str):
            output = [(chunk_id, chunk) for chunk_id, chunk in enumerate(splitter.split_text(text)) if len(chunk) >= self.min_chunk_length]
            return output
        elif isinstance(text, list):
            for i in text:
                output.append([(chunk_id, chunk) for chunk_id, chunk in enumerate(splitter.split_text(i)) if len(chunk) >= self.min_chunk_length])
            return output
        else:
            return None  
