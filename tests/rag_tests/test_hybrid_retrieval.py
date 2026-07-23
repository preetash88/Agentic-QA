from src.rag.retrievers.hybrid_retriever import retrieve


def test_hybrid_retrieval():
    docs = retrieve("JWT token expired causing 401 unauthorized")

    for doc in docs:
        print("\n")
        print("=" * 80)
        print(doc.metadata)
        print(doc.page_content[:500])

    assert len(docs) == 2