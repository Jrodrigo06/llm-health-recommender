from langchain_huggingface import HuggingFaceEmbeddings


# Function to return embedding function
def get_embedding_function():
    embeddings = HuggingFaceEmbeddings(
        model_name='all-mpnet-base-v2')
    return embeddings