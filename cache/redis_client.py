import os

from redis import Redis

from src.infra.infra_manager import InfraManager


class RedisClient:

    @property
    def client(self) -> Redis:
        client = InfraManager.redis()

        if client is not None:
            return client

        client = Redis(
            host=os.getenv("REDIS_HOST", "localhost"),
            port=int(os.getenv("REDIS_PORT", 6379)),
            db=int(os.getenv("REDIS_DB", 0)),
            decode_responses=True,
        )
        return client

    def get(self, key: str):
        return self.client.get(key)

    def set(self, key: str, value: str, ttl: int = 3600):
        return self.client.setex(key, ttl, value)


redis_client = RedisClient()
