from pydantic import BaseModel

from src.messaging.consumer import kafka_consumer
from src.messaging.producer import kafka_producer
from datetime import datetime, timezone


def _serialize(obj):
    if isinstance(obj, dict):
        return {k: _serialize(v) for k, v in obj.items()}

    if isinstance(obj, list):
        return [_serialize(v) for v in obj]

    if isinstance(obj, BaseModel):
        return obj.model_dump()

    return obj


class EventBus:

    def publish(
            self,
            topic: str,
            payload: dict
    ):
        kafka_producer.publish(
            topic,
            {
                "event": topic,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "payload": _serialize(payload),
            }
        )

    def subscribe(self, topic: str, handler):
        kafka_consumer.listen(topic=topic, handler=handler)


event_bus = EventBus()
