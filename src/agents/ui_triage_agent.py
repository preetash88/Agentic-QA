import os

from langchain_ollama import ChatOllama

from src.agents.models import UITriageReport

llm = ChatOllama(
    model="qwen3:8b",
    temperature=0,
    base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
).with_structured_output(UITriageReport)


def analyze_ui_failure(snapshot: str, console_logs: str):
    prompt = f"""
    You are a Senior SDET.

    Analyze the following UI failure.
    
    DOM Snapshot:
    {snapshot}
    
    Console Logs:
    {console_logs}
    
    Determine:
    
    1. Root cause
    2. Probable owner
    3. Confidence score
"""
    return llm.invoke(prompt)
