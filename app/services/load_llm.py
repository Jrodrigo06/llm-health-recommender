import torch, platform, traceback, sys
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"

def load_model():

    print("[load_model] Loading tokenizer…")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=True, local_files_only=True)
    print("[load_model] Tokenizer loaded")

    system = platform.system()
    has_cuda = torch.cuda.is_available()
    print(f"[load_model] CUDA available: {has_cuda}")
    print("[load_model] Loading model")
    model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            device_map="cuda",
            torch_dtype=torch.float16,
            low_cpu_mem_usage=True,
    )
    print("[load_model] Model loaded", file=sys.stderr)
    

    model.eval()
    print("[load_model] Model set to eval()", file=sys.stderr)

    print("[load_model] Returning tokenizer & model", file=sys.stderr)
    return tokenizer, model
