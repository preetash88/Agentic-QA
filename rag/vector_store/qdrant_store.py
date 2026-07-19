from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

client = QdrantClient(path="./qdrant_data")

dense_embedding = OllamaEmbeddings(model="embeddinggemma:latest")


def get_vector_store():
    return QdrantVectorStore(client=client,
                             collection_name="qa_rag",
                             embedding=dense_embedding)
