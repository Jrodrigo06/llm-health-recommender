from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.embeddings.bedrock import BedrockEmbeddings
import os

# Function to load nutrition advice documents 
def load_documents():    
    DATA_PATH = "docs_preprocessed"
    absolute_path = os.path.abspath(DATA_PATH)
    print(f"Looking in: {absolute_path}")
    print("Files found:", os.listdir(absolute_path))
    document_loader = PyPDFDirectoryLoader(DATA_PATH)
    return document_loader.load()


# Function to split documents into smaller chunks
def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 800,
        chunk_overlap = 80,
        length_function = len,
        is_seperator_regex = False,
    )
    return text_splitter.split_documents(documents)

# Function to return embedding function
def get_embedding_function():
    embeddings = BedrockEmbeddings(
        credentials_profile_name="default",
        region_name="us-west-2",
    )
    return embeddings



if __name__ == "__main__":
    documents = load_documents()
    print(f"Loaded {len(documents)} documents.")
    for doc in documents:
        print(f"Document: {doc.metadata.get('source', 'Unknown source')}")
        print(f"Content: {doc.page_content[:100]}...") 