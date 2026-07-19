import time

from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

from rag.chunkers.semantic_chunker import chunk_documents
from rag.loaders.docling_loader import load_documents

BATCH_SIZE = 50

documents = load_documents("rag/sample_docs")

chunks = chunk_documents(documents)

print(f"Total chunks generated: {len(chunks)}")

client = QdrantClient(path="./qdrant_data")

embedding = OllamaEmbeddings(model="embeddinggemma:latest")

VECTOR_SIZE = len(embedding.embed_query("test"))

collections = [collection.name for collection in client.get_collections().collections]

if "qa_rag" not in collections:
    client.create_collection(
        collection_name="qa_rag",
        vectors_config=VectorParams(
            size=VECTOR_SIZE,
            distance=Distance.COSINE
        )
    )

vector_db_store = QdrantVectorStore(
    client=client,
    collection_name="qa_rag",
    embedding=embedding
)


for start in range(0, len(chunks), BATCH_SIZE):

    end = min(start + BATCH_SIZE, len(chunks))
    batch = chunks[start:end]
    print(f"Processing batch {start // BATCH_SIZE + 1} "
          f"({start + 1} -> {end})")

    start_time = time.time()

    vector_db_store.add_documents(batch)

    elapsed = time.time() - start_time

    print(
        f"Batch completed in {elapsed:.2f}s"
    )

print(
    f"Successfully ingested {len(chunks)} chunks."
)

client.close()