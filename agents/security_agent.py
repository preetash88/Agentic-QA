from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="qwen3:8b",
    temperature=0
)


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
    return llm.invoke(prompt).content
