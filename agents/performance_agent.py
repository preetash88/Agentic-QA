from langchain_ollama import ChatOllama

from agents.models import TestPlan

llm = ChatOllama(
    model="qwen3:8b",
    temperature=0
)


def generate_performance_tests(performance_ideas: list[str]):
    prompt = f"""
    You are an expert Performance Tester with nearly 15 years of experience. 
    
    Generate performance scenarios for:

    {performance_ideas}
    
    Cover:
    
    - Load
    - Stress
    - Spike
    - Soak
    - Volume
    """

    return llm.invoke(prompt).content
