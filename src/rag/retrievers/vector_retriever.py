
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore


from src.rag.qdrant_client import get_qdrant_client

embed = OllamaEmbeddings(model="embeddinggemma:latest")

vec_store = QdrantVectorStore(
    client=get_qdrant_client(),
    collection_name="qa_rag",
    embedding=embed
)

# client.close()

def get_vector_retriever():
    return vec_store.as_retriever(search_kwargs={
        "k": 20
    })
