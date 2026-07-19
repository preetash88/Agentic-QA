from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=[
        "\n# ",
        "\n## ",
        "\n### ",
        "\n\n",
        "\n",
        ". ",
        " "
    ]
)


def chunk_documents(documents):
    chunks = []

    for doc in documents:
        split_docs = splitter.create_documents([doc["content"]])

        for chunk in split_docs:
            chunk.metadata.update(doc["metadata"])

        chunks.extend(split_docs)

    return chunks
