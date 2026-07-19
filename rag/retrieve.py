from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

embed = OllamaEmbeddings(model="embeddinggemma:latest")

client = QdrantClient(path="./qdrant_data")

vector_db_store = QdrantVectorStore(
    client=client,
    collection_name="qa_rag",
    embedding=embed,
)

retriever = vector_db_store.as_retriever(
    search_kwargs={
        "k": 5
    }
)
# client.close()


def retrieve(query: str):
    return retriever.invoke(query)
