from langchain_classic.retrievers import EnsembleRetriever

from src.rag.chunkers.semantic_chunker import chunk_documents
from src.rag.loaders.docling_loader import load_documents
from src.rag.rerankers.cross_encode_reranker import rerank
from src.rag.retrievers.bm25_retriever import get_bm25_retriever
from src.rag.retrievers.vector_retriever import get_vector_retriever

documents = load_documents("rag/sample_docs")

chunks = chunk_documents(documents)

bm25 = get_bm25_retriever(chunks)

vector = get_vector_retriever()

hybrid_retriever = EnsembleRetriever(retrievers=[bm25, vector], weights=[0.3, 0.7])


def retrieve(query: str):
    docs = hybrid_retriever.invoke(query)

    return rerank(query, docs)
