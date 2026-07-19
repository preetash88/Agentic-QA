from typing import Optional

from langchain_ollama import ChatOllama

from agents.models import SecurityReport

llm = ChatOllama(
    model="qwen3:8b",
    temperature=0
).with_structured_output(SecurityReport)


def analyze_security(
        url: str,
        headers: dict,
        response_body: str,
        cookies: Optional[dict] = None,
) -> SecurityReport:
    prompt = f"""
    You are a Senior Application Security Engineer.

    Analyze this application response for security issues.

    URL:
    {url}

    Headers:
    {headers}
    
    Cookies:
    {cookies}

    Response Body:
    {response_body}

    Check for:

    - Missing CSP
    - Missing HSTS
    - Missing X-Frame-Options
    - Missing X-Content-Type-Options
    - Missing Secure Cookies
    - Missing HttpOnly Cookie
    - Missing SameSite Cookie
    - Information Disclosure
    - CORS Misconfiguration
    - Potential XSS Risks
    - OWASP API Top 10 issues

    Return findings sorted by severity.
    """

    return llm.invoke(prompt)
