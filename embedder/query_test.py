from langchain.vectorstores import Chroma

# 저장된 ChromaDB 벡터를 로드합니다.
directory = 'index_store'
vector_index = Chroma.from_documents(directory)

query = "오늘 날씨"
matching_docs = vector_index.similarity_search(query)

print(matching_docs[0])
