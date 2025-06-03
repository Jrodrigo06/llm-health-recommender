from sentence_transformers import SentenceTransformer


# Function to return embedding function
def get_embedding_function():
    embeddings = SentenceTransformer('all-mpnet-base-v2')
    return embeddings