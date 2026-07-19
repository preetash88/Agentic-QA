from langchain_ollama import ChatOllama

from agents.models import TestPlan

llm = ChatOllama(
    model="qwen3:8b",
    temperature=0
).with_structured_output(TestPlan)


def generate_test_plan(requirement: str) -> TestPlan:
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

    response = llm.invoke(prompt)

    return response
