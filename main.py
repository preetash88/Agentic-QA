import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from kafka import KafkaProducer
from qdrant_client import QdrantClient
from redis import Redis

from src.orchestration.workflow import AgentWorkflow
from src.infra.infra_manager import InfraManager
from src.api.health import router as health_router
from src.api.metrics import router as metrics_router
from src.api.workflow import router as workflow_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating Redis Client...")
    redis_client = Redis(
        host=os.getenv("REDIS_HOST", "redis"),
        port=int(os.getenv("REDIS_PORT", 6379)),
        decode_responses=True,
    )

    print("Creating Kafka Producer...")
    kafka_producer = KafkaProducer(
        bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP", "kafka:9092"),
    )

    print("Creating Qdrant Client...")
    qdrant_client = QdrantClient(
        host=os.getenv("QDRANT_HOST", "qdrant"),
        port=int(os.getenv("QDRANT_PORT", 8080)),
    )

    print("Registering Redis Client...")
    InfraManager.register_redis(redis_client)

    print("Registering Kafka Producer...")
    InfraManager.register_kafka(kafka_producer)

    print("Registering Qdrant Client...")
    InfraManager.register_qdrant(qdrant_client)

    print("Starting QA_SDET Runtime...")
    app.state.workflow = AgentWorkflow()

    yield

    print("Stopping QA_SDET Runtime...")

    InfraManager.shutdown()


app = FastAPI(
    title="QA_SDET",
    description="Enterprise Agentic AI Testing Framework",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(health_router)
app.include_router(metrics_router)
app.include_router(workflow_router)
