import time

from src.llm.provider import lllm
from src.monitoring.metrics import agent_tool, agent_duration

from src.agents.models import TestPlan

llm = lllm.with_structured_output(TestPlan, agent_name="planner")


def generate_test_plan(requirement: str) -> TestPlan:
    agent_tool.labels("planner").inc()

    start = time.time()

    prompt = f"""
    You are a Senior SDET.
    
    Analyze the requirement and generate:

    - positive scenarios
    - negative scenarios
    - edge cases
    - api test ideas
    - ui test ideas
    - security test ideas
    - performance test ideas
    
    Requirement:
    {requirement}
    """

    response = llm.invoke(prompt=prompt)

    agent_duration.labels("planner").observe(time.time() - start)

    return response
