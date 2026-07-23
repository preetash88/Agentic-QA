from langchain_classic.retrievers import BM25Retriever


def get_bm25_retriever(chunks):
    retriever = BM25Retriever.from_documents(chunks)

    retriever.k = 20
    return retriever