# import json
# from typing import TypeVar, Type
#
# from langchain_ollama import ChatOllama
# from pydantic import BaseModel
#
# from cache import semantic_cache
# from monitoring.metrics import cache_hit, cache_miss, llm_requests
#
# T = TypeVar('T', bound=BaseModel)
#
#
# class CachedLLM:
#     def __init__(self, model: str = "qwen3:8b", temperature: float = 0):
#         self.model = model
#         self.temperature = temperature
#
#     def with_structured_output(self, schema: Type[T]):
#         llm = ChatOllama(model=self.model, temperature=self.temperature).with_structured_output(schema)
#
#         class StructuredInvoker:
#
#             def invoke(_, prompt: str) -> T:
#                 cached = semantic_cache.lookup(self.model, prompt)
#
#                 if cached:
#                     cache_hit.inc()
#                     print("✅ Redis Cache Hit")
#
#                     data = json.loads(cached)
#
#                     return schema.model_validate(data)
#
#                 cache_miss.inc()
#
#                 llm_requests.inc()
#                 print("❌ Redis Cache Miss")
#
#                 response = llm.invoke(prompt)
#
#                 semantic_cache.save(
#                     self.model,
#                     prompt,
#                     json.dumps(
#                         response.model_dump(),
#                         default=str
#                     ),
#                 )
#
#                 return response
#
#         return StructuredInvoker()
#
#
# llm = CachedLLM()
