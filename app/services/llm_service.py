

# Function to call to format the user_info and question into a prompt for the LLM
def format_prompt(user_info, question):
    """
    Format the user information and question into a prompt for the LLM.
    """
    prompt = f"Considering this User Information: "
    for key, value in user_info.items():
        prompt += f"{key}: {value}"
    
    prompt += "Answer the following question: "
    prompt += f"{question}"
    return prompt

def get_response_from_llm(prompt):
   #Dummy response from LLM
    return "Dummy response from LLM"