from cache.cache_service import cache


class SemanticCache:

    def lookup(self, agent_name: str, model: str, prompt: str):
        return cache.get(agent_name=agent_name, model=model, prompt=prompt)

    def save(self, agent_name: str, model: str, prompt: str, response: str):
        cache.put(agent_name=agent_name, model=model, prompt=prompt, response=response)


semantic_cache = SemanticCache()
