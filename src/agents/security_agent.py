from src.llm.provider import lllm

llm = lllm


def generate_security_tests(security_ideas: list[str]):
    prompt = f"""
    You are a Cybersecurity expert.
    
    Generate security scenarios based on:

    {security_ideas}
    
    Focus on:
    
    - OWASP Top 10
    - Authentication
    - Authorization
    - Session Management
    - API Security
"""
    return llm.invoke(agent_name="security_agent", prompt=prompt)
