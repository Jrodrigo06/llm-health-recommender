from langchain_community.document_loaders import PyPDFDirectoryLoader
import os

# Function to load nutrition advice documents 
def load_documents():    
    DATA_PATH = "docs_preprocessed"
    absolute_path = os.path.abspath(DATA_PATH)
    print(f"Looking in: {absolute_path}")
    print("Files found:", os.listdir(absolute_path))
    document_loader = PyPDFDirectoryLoader(DATA_PATH)
    return document_loader.load()





 