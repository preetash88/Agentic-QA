from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3:8b",
    temperature=0
)


def generate_api_tests(requirement: list[str]):
    prompt = f"""
    You are an expert Senior SDET with more than 15 years of experience.
    
    Generate all basic to complex real world API Test scenarios
    
    Requirement: 
    {requirement}
"""
    return llm.invoke(prompt).content
