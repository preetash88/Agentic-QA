from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3:8b",
    temperature=0
)


def generate_ui_tests(requirement: list[str]):
    prompt = f"""
    You are an expert Senior Test Architect with more than 20 years of experience. 
    Generate UI test scenarios.
    
    Requirement:
    {requirement}
"""

    return llm.invoke(prompt).content