from prometheus_client import Counter, Histogram

workflow_total = Counter("workflow_total","Total workflows executed")

workflow_failed = Counter("workflow_failed","Total failed workflows")

agent_tool = Counter("agent_tool","Total agent executions",["agent"])

agent_duration = Histogram("agent_duration_seconds","Agent execution time",["agent"])

llm_requests = Counter("llm_requests_total","LLM Requests")

llm_tokens = Counter("llm_tokens_total","LLM Tokens")

cache_hit = Counter("cache_hit_total","Redis Cache hits")

cache_miss = Counter("cache_miss_total","Redis Cache misses")

print("metrics.py loaded")
print(id(workflow_total))