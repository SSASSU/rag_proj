#coding:utf-8

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoConfig, AutoModel
from langchain_community.chat_models import ChatOllama


def llm_loader(model_path):
   
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Using device:", device)
    
    #tokenizer = AutoTokenizer.from_pretrained("CohereForAI/aya-23-35B")
    #model = AutoModel.from_pretrained("bartowski/aya-23-35B-GGUF")

    return model, tokenizer, device 

def ollama_llm():

    model = ChatOllama(model="aya:35b")

    return model 


async def ollama_response(user_text, model):

    resp_text = model.invoke(user_text)

    return resp_text


async def generate_response(prompt, model, tokenizer, device, model_config):

    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)

    output = model.generate(input_ids,
                            max_length=model_config["generation"]["max_length"],
                            temperature=model_config["generation"]["temperature"]
                            )

    response = tokenizer.decode(output[0], skip_special_tokens=True)

    return response

