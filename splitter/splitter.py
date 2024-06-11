import re

class NtelsTextSplitter():
    def __init__(self, default_text="내용없음"):
        self.default_text = default_text

    def preprocessing(self, text):
        text = re.sub(r'[\t\r\f\v]', '', text)
        text = re.sub(r'[\t]', ' ', text)
        text = re.sub(r'\n{3,}', '\n\n', text)
        text = re.sub(r' {2,}', ' ', text)
        text = text.strip()
        if len(text) == 0:
            return self.default_text3
        else:
            return text

    def chunking(text):
        pass


a = 3
print(a)






