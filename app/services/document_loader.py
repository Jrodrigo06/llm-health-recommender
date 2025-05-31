from langchain_community.document_loaders import PyPDFDirectoryLoader
import os

def load_documents():    
    DATA_PATH = "docs_preprocessed"
    absolute_path = os.path.abspath(DATA_PATH)
    print(f"Looking in: {absolute_path}")
    print("Files found:", os.listdir(absolute_path))
    document_loader = PyPDFDirectoryLoader(DATA_PATH)
    return document_loader.load()


if __name__ == "__main__":
    documents = load_documents()
    print(f"Loaded {len(documents)} documents.")
    for doc in documents:
        print(f"Document: {doc.metadata.get('source', 'Unknown source')}")
        print(f"Content: {doc.page_content[:100]}...") 