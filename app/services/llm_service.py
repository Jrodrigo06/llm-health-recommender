import torch
from app.services.load_llm import load_model 
from app.models.schema import UserInfo, UserRequest 
from app.services.RagSystem.embedding_function import get_embedding_function
from langchain_chroma import Chroma
from langchain.schema import Document
import os
"""
This formats user information and questions into a prompt,
and retrieves responses from the LLM by calling the model.
"""

CHROMA_PATH = os.path.abspath("data/chroma_db")

print("Loading model and tokenizer...")
tokenizer, model = load_model()
print("Model and tokenizer loaded successfully.")
device = "cuda" if torch.cuda.is_available() else "cpu"






# Method to retrieve relevant chunks from the Chroma database based on the user's question
def retrieve_relevant_chunks(question: str) -> list[Document]:
    chroma = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=get_embedding_function(),
    )
    return chroma.similarity_search(question, k=5)

# Function to call to format the user_info and question into a prompt for the LLM
def format_prompt(user_info, question) -> str:
    prompt = "You are a helpful health assistant given relevant context from medical passages. Answer the question based on the user profile below.\n\n"
    prompt += f"Considering this User Information (Height in inches and weight in lbs): "
    for key, value in user_info.items():
        prompt += f"{key}: {value}, "

    prompt += "\n\n with this context from medical passages: "
    relevant_chunks = retrieve_relevant_chunks(question)
    for idx, doc in enumerate(relevant_chunks, start=1):
        snippet = doc.page_content.replace("\n", " ")[:400]
        prompt += f"  Context {idx}: {snippet}…\n"
    prompt += "\n"
    
    prompt += f"Question: {question}  \n\n"
    prompt += "Please give one specific, actionable answer that uses the context above.\n"
    return prompt


## Function to call the LLM with the formatted prompt and return the response
def get_response_from_llm(prompt) -> str:

    print("Prompt sent to LLM:", prompt) 
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    prompt_length = inputs["input_ids"].shape[-1]
    print("Prompt token count:", prompt_length)  
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=400,   
            do_sample=True,      
            top_p=0.9,            
            temperature=0.7       
        )
    
    generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("Generated response:", generated)  
    answer = generated[len(prompt):].strip()
    return answer

## Example usage of the LLM service   
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
        question="How can I lower my blood sugar?"
        )

    prompt = format_prompt(user_request.user_info.model_dump(), user_request.question)
    response = get_response_from_llm(prompt)
    print("LLM Response:", response)