from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from app.models.schema import UserInfo, UserRequest  # import your real models


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
model = AutoModelForCausalLM.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
model.to(device)
model.eval()

# Function to call to format the user_info and question into a prompt for the LLM
def format_prompt(user_info, question) -> str:
    prompt = "You are a helpful health assistant. Answer the question based on the user profile below.\n\n"
    prompt += f"Considering this User Information: "
    for key, value in user_info.items():
        prompt += f"{key}: {value}"
    
    prompt += "Answer the following question for the user: "
    prompt += f"{question}"
    return prompt

def get_response_from_llm(prompt) -> str:

    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=200,   
            do_sample=True,      
            top_p=0.9,            
            temperature=0.7       
        )
    
    generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated[len(prompt):].strip()  

   
if __name__ == "__main__":
    data = UserInfo(
                name="John Doe",
                email="johndoe@gmail.com",
                age=30,
                bmi=22.5,
                height=175.0,
                weight=70.0,
                diabetes=False,
                overweight=False,
                heart_disease=False,
                family_history="No family history",
                smoking=False,
                alcohol=False
                )
            
    user_request = UserRequest(
        user_id=1,
        user_info=data,
        question="Is my BMI normal?"
        )

    prompt = format_prompt(user_request.user_info.model_dump(), user_request.question)
    response = get_response_from_llm(prompt)
    print("LLM Response:", response)