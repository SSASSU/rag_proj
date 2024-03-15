#coding:utf-8

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def llm_loader(model_path):
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Using device:", device)

    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path).to(device)

    return model, tokenizer, device 

async def generate_response(prompt, model, tokenizer, device, model_config):

    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)

    output = model.generate(input_ids,
                            max_length=model_config["generation"]["max_length"],
                            temperature=model_config["generation"]["temperature"]
                            )

    response = tokenizer.decode(output[0], skip_special_tokens=True)

    return response
