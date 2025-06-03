from embedding_function import get_embedding_function
from langchain.vectorstores.chroma import Chroma
from langchain.schema import Document


def add_to_chroma(chunks: list[Document]):
    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=get_embedding_function())
    db.add_documents(new_chunks, ids=new_chunks_ids)
    db.persist()


def get_new_chunks(chunks: list[Document]) -> list[Document]:
    last_page_id = None
    current_chunk_index = 0


    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"
        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0
        
        chunk.metadata["id"] = current_page_id
        
        last_page_id = current_page_id