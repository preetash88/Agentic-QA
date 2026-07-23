from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore

from src.rag.qdrant_client import get_qdrant_client

dense_embedding = OllamaEmbeddings(model="embeddinggemma:latest")


def get_vector_store():
    return QdrantVectorStore(client=get_qdrant_client(),
                             collection_name="qa_rag",
                             embedding=dense_embedding)
