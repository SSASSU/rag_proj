from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Milvus
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain.embeddings import SentenceTransformerEmbeddings

## DB Connect


## Text Embed
loader = PyPDFLoader("./sample.pdf")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=30,
    chunk_overlap=10
    )

pages = loader.load_and_split(text_splitter)

print(pages)

embeddings = SentenceTransformerEmbeddings(model_name="paraphrase-MiniLM-L6-v2")


vector_db = Milvus.from_documents(
    pages,
    embeddings,
    connection_args={"host": "127.0.0.1", "port": "19530"},
)

query = "오늘 날짜는?"
docs = vector_db.similarity_search(query)

print (docs)

