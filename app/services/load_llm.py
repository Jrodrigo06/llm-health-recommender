from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Loads Llama 2 7B model and tokenizer
def load_model():
    model_name = "meta-llama/Llama-2-7b-chat-hf"

    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        load_in_4bit=True,           
        device_map="auto",          
        torch_dtype=torch.float16,  
        low_cpu_mem_usage=True,      
    )

    model.eval()  
    return tokenizer, model