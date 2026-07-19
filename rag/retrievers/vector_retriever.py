# from langchain_classic.retrievers import EnsembleRetriever
#
# hybridRetriever = EnsembleRetriever(
#     retrievers=[vector_retriever,
#                 bm25_retriever],
#     weights=[0.7, 0.3]
# )
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

embed = OllamaEmbeddings(model="embeddinggemma:latest")

client = QdrantClient(path="./qdrant_data")

vec_store = QdrantVectorStore(client=client, collection_name="qa_rag", embedding=embed)

# client.close()

def get_vector_retriever():
    return vec_store.as_retriever(search_kwargs={
        "k": 20
    })
