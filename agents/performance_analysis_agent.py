from langchain_ollama import ChatOllama

from agents.models import PerformanceReport

llm = ChatOllama(
    model="qwen3:8b",
    temperature=0
).with_structured_output(PerformanceReport)


def analyze_performance(k6_output: str) -> PerformanceReport:
    prompt = f"""
    You are a Principal Performance Engineer.

    Analyze the following k6 load testing results.

    K6 Results:

    {k6_output}

    Evaluate:

    - Response time
    - Throughput
    - Error rate
    - P95 latency
    - P99 latency
    - Saturation indicators
    - Scalability concerns

    Identify:

    - Performance bottlenecks
    - Risks
    - Recommendations

    Return findings ordered by severity.
"""
    return llm.invoke(prompt)
