import chromadb
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain.embeddings import SentenceTransformerEmbeddings

loader = PyPDFLoader("./sample.pdf")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=30,
    chunk_overlap=5
    )

pages = loader.load_and_split(text_splitter)
embeddings = SentenceTransformerEmbeddings(model_name="paraphrase-MiniLM-L6-v2")

#client = chromadb.HttpClient(host="localhost", port=8000)

# Create a persistent, file-based vector store, using Chroma vector store.
directory = 'index_store'
vector_index = Chroma.from_documents(
    pages, # Documents
    embeddings, # Text embedding model
    persist_directory=directory # persists the vectors to the file system
    )


vector_index.persist()

query = "오늘 기온 온도?"
matching_docs = vector_index.similarity_search(query)


print(matching_docs)
