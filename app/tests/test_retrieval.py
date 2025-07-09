from app.services.RagSystem.embedding_function import get_embedding_function
from langchain_chroma import Chroma


if __name__ == "__main__":
    chroma = Chroma(
        persist_directory="data/chroma_db",
        embedding_function=get_embedding_function(),
    )
    docs = chroma.similarity_search("What foods are good for prediabetes?", k=3)
    for d in docs:
        print(d.page_content[:400], "…")