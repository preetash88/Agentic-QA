from rag.retrieve import retrieve


def test_retrieval():

    results = retrieve(
        "JWT token expiration issue"
    )

    print("\n\nRetrieved Documents:\n")

    for doc in results:
        print("\n========================")
        print(doc.metadata)
        print(doc.page_content[:500])
