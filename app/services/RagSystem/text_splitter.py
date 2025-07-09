from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document

# Function to split documents into smaller chunks
def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 800,
        chunk_overlap = 80,
        length_function = len,
    )
    return text_splitter.split_documents(documents)