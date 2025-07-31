from app.services.RagSystem.document_loader import load_documents
from app.services.RagSystem.store_vector_embeddings import add_to_chroma
from app.services.RagSystem.text_splitter import semantic_split_documents as split_documents

# This script builds the RAG system database by loading documents,
def main():

    documents = load_documents()
    print("Loaded documents")
    print(f"Number of documents loaded: {len(documents)}")

    chunks = split_documents(documents) #type: ignore
    print("Split documents into chunks")


    add_to_chroma(chunks)
    print("Added chunks to Chroma DB")



if __name__ == "__main__":
    main()
    print("RAG system database built successfully.")


