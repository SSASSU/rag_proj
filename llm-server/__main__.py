#coding:utf-8

import yaml
import uvicorn
from fastapi import FastAPI, Request
from modules.llm import llm

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
    model, tokenizer, device = llm.llm_loader(config["model"]["path"])

@app.post("/question")
async def generate_response(request: Request):

    global model, tokenizer, device, config

    data = await request.json()
    prompt = data.get("prompt")

    resp = await llm.generate_response(prompt, model, tokenizer, device, config)

    return {"response": resp}
