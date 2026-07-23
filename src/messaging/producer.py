from src.messaging.kafka_client import get_producer
import logging

logger = logging.getLogger(__name__)


class KafkaProducerService:

    def publish(
            self,
            topic: str,
            event: dict
    ):
        try:
            producer = get_producer()
            future = producer.send(topic, event)
            future.get(timeout=10)
            producer.flush()

            logger.info(f"Published event to {topic}")
        except Exception as e:
            logger.exception(f"Failed to publish event to {topic}: {e}")
        


kafka_producer = KafkaProducerService()
