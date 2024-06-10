import numpy as np
import cohere
from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection

cohere_key = "[COHERE KEY]"
co = cohere.Client(cohere_key)

# Milvus에 연결
connections.connect("default", host="192.168.15.94", port="19530")

# Milvus Collection 로드
collection = Collection(name="pdf_chunks")

# 검색 코드
def search_milvus(query):

    text_list = []
    query_emb = co.embed(texts=[query], input_type="search_query", model="embed-multilingual-v3.0").embeddings

    search_params = {"metric_type": "L2", "params": {}}
    results = collection.search(query_emb, "embedding", param=search_params, output_fields=["text"], limit=3, expr=None)

    for result in results[0]:

        text_list.append(result.entity.get('text'))

    return text_list   

