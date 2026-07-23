from cache.cache_key import generate_cache_key
from cache.redis_client import redis_client


class CacheService:

    def get(
            self,
            agent_name: str,
            model: str,
            prompt: str
    ):
        key = generate_cache_key(agent_name=agent_name, model=model, prompt=prompt)

        return redis_client.get(key)

    def put(self, agent_name: str, model: str, prompt: str, response: str, ttl: int = 3600):
        key = generate_cache_key(agent_name=agent_name, model=model, prompt=prompt)

        redis_client.set(key, response, ttl)


cache = CacheService()
