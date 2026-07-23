from src.messaging.kafka_client import create_consumer
import logging

logger = logging.getLogger(__name__)


class KafkaConsumerService:

    def listen(
            self,
            topic: str,
            handler
    ):
        consumer = create_consumer(topic)

        logger.info(f"Listening on {topic}")

        for message in consumer:
            try:
                handler(message.value)
            except Exception:
                logger.exception(
                    "Kafka consumer failed."
                )


kafka_consumer = KafkaConsumerService()
