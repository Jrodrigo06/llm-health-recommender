import nltk # type: ignore
nltk.download('punkt') #type: ignore
nltk.download('punkt_tab') #type: ignore
from nltk.tokenize import sent_tokenize #type: ignore

from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim  # type: ignore
from typing import List

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

from langchain.schema import Document

def semantic_split_documents(documents: list[Document], threshold=0.75, max_chunk_size=5) -> List[Document]:  #type: ignore
    """
    Splits a list of documents into smaller chunks based on semantic similarity.
    
    Args:
        documents (list[Document]): List of Document objects to be split.
        threshold (float): Similarity threshold for chunking.
        max_chunk_size (int): Maximum number of sentences in each chunk.
    
    Returns:
        list[Document]: List of Document objects containing the chunks.
    """
    all_chunks = []
    for doc in documents:
        chunks = _chunk_single_document(doc, threshold, max_chunk_size)
        all_chunks.extend(chunks) #type: ignore
    return all_chunks #type: ignore

def _chunk_single_document(document: Document, threshold=0.75, max_chunk_size=5) -> List[Document]: #type: ignore
    """ Splits a single document into smaller chunks based on semantic similarity.
    Args:
        document (Document): The Document object to be split.
        threshold (float): Similarity threshold for chunking. We use 0.75 as default.
        max_chunk_size (int): Maximum number of sentences in each chunk. We use 5 as default.
    Returns:
        list[Document]: List of Document objects containing the chunks.
    """
    return semantic_chunk_text(document.page_content, threshold, max_chunk_size)


# Function to semantically chunk text into smaller segments based on sentence similarity
def semantic_chunk_text(text: str, threshold=0.75, max_chunk_size=5) -> List[Document]: #type: ignore
    """ Splits text into smaller chunks based on semantic similarity of sentences.
    Args:
        text (str): The text to be split.
        threshold (float): Similarity threshold for chunking. We use 0.75 as default.
        max_chunk_size (int): Maximum number of sentences in each chunk. We use 5 as default.
    Returns:
        list[Document]: List of Document objects containing the chunks.
    """
    
    
    sentences = sent_tokenize(text)
    embeddings = model.encode(sentences, convert_to_tensor=True) #type: ignore
 
    chunks = []
    current_chunk = [sentences[0]]

    for i in range(1, len(sentences)):
        sim = cos_sim(embeddings[i], embeddings[i - 1]).item()
        if sim > threshold and len(current_chunk) < max_chunk_size:
            current_chunk.append(sentences[i])
        else:
            chunks.append(" ".join(current_chunk)) #type: ignore
            current_chunk = [sentences[i]]

    if current_chunk:
        chunks.append(" ".join(current_chunk)) #type: ignore
 
    return [Document(page_content=chunk) for chunk in chunks] #type: ignore


