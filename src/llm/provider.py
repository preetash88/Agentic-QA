import json
import os
from typing import TypeVar, Type

from langchain_ollama import ChatOllama
from pydantic import BaseModel

from cache.semantic_cache import semantic_cache
from src.monitoring.metrics import cache_hit, cache_miss, llm_requests

T = TypeVar('T', bound=BaseModel)


class CachedLLM:
    def __init__(self, model: str = "qwen3:8b", temperature: float = 0):
        self.model = model
        self.temperature = temperature

    def with_structured_output(self, schema: Type[T], agent_name: str):
        llm = ChatOllama(
            model=self.model,
            temperature=self.temperature,
            base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        ).with_structured_output(
            schema)

        class StructuredInvoker:

            def invoke(_, prompt: str) -> T:
                cached = semantic_cache.lookup(agent_name=agent_name, model=self.model, prompt=prompt)

                if cached:
                    cache_hit.inc()
                    print(f"Redis Cache Hit for {agent_name} agent")

                    data = json.loads(cached)

                    return schema.model_validate(data)

                cache_miss.inc()

                llm_requests.inc()
                print(f"Redis Cache Miss for {agent_name} agent")

                response = llm.invoke(prompt)

                semantic_cache.save(
                    agent_name=agent_name,
                    model=self.model,
                    prompt=prompt,
                    response=json.dumps(
                        response.model_dump(),
                        default=str
                    ),
                )

                return response

        return StructuredInvoker()

    def invoke(self, agent_name: str, prompt: str):
        llm = ChatOllama(
            model=self.model,
            temperature=self.temperature,
            base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        )

        cached = semantic_cache.lookup(agent_name=agent_name, model=self.model, prompt=prompt)

        if cached:
            cache_hit.inc()
            print(f"Redis Cache Hit for {agent_name} agent")

            return cached

        cache_miss.inc()
        llm_requests.inc()

        print(f"Redis Cache Miss for {agent_name} agent")

        response = llm.invoke(prompt)

        semantic_cache.save(
            agent_name=agent_name,
            model=self.model,
            prompt=prompt,
            response=response.content
        )
        return response.content


lllm = CachedLLM()
