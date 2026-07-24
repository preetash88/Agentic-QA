from src.llm.provider import lllm

llm = lllm


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

    return llm.invoke(
        agent_name="performance_agent",
        prompt=prompt
    ).content
