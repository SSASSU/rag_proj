#coding:utf-8
import yaml
import uvicorn
from fastapi import FastAPI, Request
from modules.llm import llm
from modules.vector_search import vector_search

app = FastAPI()

config = {}
model = None
tokenizer = None
device = None

def load_config():

    with open("./config/config.yaml", "r") as f:
        config = yaml.safe_load(f)
    
    return config 

def main():

    uvicorn.run("__main__:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()

@app.on_event('startup')
def init_data():
    global model, tokenizer, device, config 
    config = load_config()
    #model, tokenizer, device = llm.llm_loader(config["model"]["path"])
    model = llm.ollama_llm()

@app.post("/question")
async def generate_response(request: Request):

    global model, tokenizer, device, config

    text_list = []
    data = await request.json()
    print (f"data : {data}")
    
    text_list = vector_search.search_milvus(data.get('query', ''))
    
    prompt = f"{text_list[0]}\n {text_list[1]}\n {text_list[2]}\n\n무조건 위에 적힌 내용만을 참고해서 아래 질문에 대해 자세하게 답변해줘. \n{data.get('query', '')}"
   
    print (f"prompt : {prompt}")

    rsp = await llm.ollama_response(prompt, model)

    return {"query": rsp}
