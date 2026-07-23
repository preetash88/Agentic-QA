import os

from qdrant_client import QdrantClient

from src.infra.infra_manager import InfraManager


def get_qdrant_client() -> QdrantClient:
    client = InfraManager.qdrant()

    if client is not None:
        return client

    client = QdrantClient(
        host=os.getenv("QDRANT_HOST", "localhost"),
        port=int(os.getenv("QDRANT_PORT", 6333)),
    )

    InfraManager.register_qdrant(client)

    return client
