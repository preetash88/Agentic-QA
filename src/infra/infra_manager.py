import logging
from typing import Optional

from kafka import KafkaProducer
from qdrant_client import QdrantClient
from redis import Redis

logger = logging.getLogger(__name__)


class InfraManager:
    _kafka_producer: Optional[KafkaProducer] = None
    _redis: Optional[Redis] = None
    _qdrant: Optional[QdrantClient] = None

    @classmethod
    def register_kafka(cls, producer: KafkaProducer):
        cls._kafka_producer = producer

    @classmethod
    def kafka(cls) -> Optional[KafkaProducer]:
        return cls._kafka_producer

    @classmethod
    def register_redis(cls, redis: Redis):
        cls._redis = redis

    @classmethod
    def redis(cls) -> Optional[Redis]:
        return cls._redis

    @classmethod
    def register_qdrant(cls, qdrant: QdrantClient):
        cls._qdrant = qdrant

    @classmethod
    def qdrant(cls) -> Optional[QdrantClient]:
        return cls._qdrant

    @classmethod
    def shutdown(cls):
        if cls._kafka_producer:
            logger.info("Closing Kafka producer...")
            cls._kafka_producer.flush()
            cls._kafka_producer.close()

        if cls._redis:
            logger.info("Closing Redis...")
            cls._redis.close()

        if cls._qdrant:
            logger.info("Closing Qdrant...")
            cls._qdrant.close()
