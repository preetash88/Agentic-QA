from src.llm.provider import lllm

llm = lllm


def generate_ui_tests(requirement: list[str]):
    prompt = f"""
    You are an expert Senior Test Architect with more than 20 years of experience. 
    Generate UI test scenarios.
    
    Requirement:
    {requirement}
"""

    return llm.invoke(agent_name="ui_agent", prompt=prompt)
