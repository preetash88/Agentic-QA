import json
import logging
import os

from kafka import KafkaProducer, KafkaConsumer

from src.infra.infra_manager import InfraManager

logger = logging.getLogger(__name__)

BOOTSTRAP = os.getenv(
    "KAFKA_BOOTSTRAP",
    "localhost:9092",
)


def get_producer():
    producer = InfraManager.kafka()

    if producer is None:
        return producer

    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP,
        value_serializer=lambda v: json.dumps(v).encode()
    )

    InfraManager.register_kafka(producer)

    return producer


def create_consumer(topic: str):
    return KafkaConsumer(
        topic,
        bootstrap_servers=BOOTSTRAP,
        value_deserializer=lambda v: json.loads(v.decode()),
        auto_offset_reset="latest",
        group_id="qa_sdet",
    )


def close_producer():
    global _producer

    if _producer:
        logger.info("Closing Kafka Producer...")
        _producer.flush()
        _producer.close()
        _producer = None
