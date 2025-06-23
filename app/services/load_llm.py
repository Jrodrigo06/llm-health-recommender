import torch, platform, traceback, sys
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"

def load_model():

    print("[load_model] Loading tokenizer…", file=sys.stderr)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=True)
    print("✔ [load_model] Tokenizer loaded", file=sys.stderr)

    system = platform.system()
    has_cuda = torch.cuda.is_available()
    has_mps  = system=="Darwin" and torch.backends.mps.is_available()
    print(f"[load_model] system={system}, cuda={has_cuda}, mps={has_mps}", file=sys.stderr)
    print("[load_model] Loading model", file=sys.stderr)
    model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            device_map="auto",
            torch_dtype=torch.float16,
            low_cpu_mem_usage=True,
    )
    print("[load_model] Model loaded", file=sys.stderr)
    

    model.eval()
    print("[load_model] Model set to eval()", file=sys.stderr)

    print("[load_model] Returning tokenizer & model", file=sys.stderr)
    return tokenizer, model
