from app.services.RagSystem.embedding_function import get_embedding_function
from langchain_chroma import Chroma
from langchain.schema import Document
import os

CHROMA_PATH = "data/chroma_db"

def add_to_chroma(chunks: list[Document]):
    new_chunks, new_chunks_ids = get_new_chunks(chunks)

    db = Chroma(
        persist_directory=os.path.abspath(CHROMA_PATH),
        embedding_function=get_embedding_function())
    
    db.add_documents(new_chunks, ids=new_chunks_ids)




def get_new_chunks(chunks: list[Document]) -> tuple[list[Document], list[str]]:
    last_page_id = None
    chunk_index = 0
    new_chunks_ids: list[str] = []


    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"
        if current_page_id == last_page_id:
            chunk_index += 1
        else:
            chunk_index = 0
        unique_id = f"{current_page_id}:{chunk_index}"
        chunk.metadata["id"] = unique_id
        new_chunks_ids.append(unique_id)
        
        last_page_id = current_page_id
    
    return chunks, new_chunks_ids