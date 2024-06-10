import os
import fitz  # PyMuPDF
import numpy as np
import cohere
from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection

def read_pdf_pages(file_path):
    doc = fitz.open(file_path)
    pages = []
    for page in doc:
        text = page.get_text("text").strip()
        if text:
            pages.append(text)
    return pages

cohere_key = "[COHERE KEY]"
co = cohere.Client(cohere_key)

connections.connect("default", host="192.168.15.94", port="19530")

fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=1024),  
    FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=65535)
]
schema = CollectionSchema(fields, "pdf_chunks")

collection = Collection("pdf_chunks", schema)

index_params = {
    "index_type": "IVF_FLAT",
    "metric_type": "L2",
    "params": {"nlist": 100}
}
collection.create_index(field_name="embedding", index_params=index_params)

pdf_dir = "./pdf"

all_chunks = []
for filename in os.listdir(pdf_dir):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_dir, filename)
        chunks = read_pdf_pages(pdf_path)
        all_chunks.extend(chunks)

embeddings = co.embed(texts=all_chunks, input_type="search_document", model="embed-multilingual-v3.0").embeddings
embeddings = np.asarray(embeddings)

data = [
    embeddings.tolist(),
    all_chunks
]
collection.insert(data)
collection.load()
