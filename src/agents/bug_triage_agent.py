from typing import Optional
from src.agents.gtihub_similarity_agent import find_duplicates
from src.agents.result import BugReport
from src.llm.provider import lllm
from src.rag.retrievers.hybrid_retriever import retrieve

llm = lllm.with_structured_output(BugReport)


def analyze_failure(
        logs: str,
        console_logs: Optional[str],
        playwright_error: Optional[str]
) -> BugReport:
    retrieval_query = f"""
    {logs}

    {console_logs}

    {playwright_error}
    """

    context_docs = retrieve(retrieval_query)

    context = "\n\n".join([doc.page_content for doc in context_docs])

    prompt = f"""
    You are a Senior SDET and Production Support Engineer.

    Use historical incidents and runbooks if relevant.
    
    Historical Context:
    {context}
    
    Application Logs:
    {logs}
    
    Console Logs:
    {console_logs}
    
    Playwright Error:
    {playwright_error}
    
    Provide:

    1. Severity
    2. Probable Engineer Owner
    3. Owning Team
    4. Root Cause
    5. Failure Category
    6. Next Steps
    7. Similar Incidents
    8. Recommended Runbooks
    9. Confidence Score
"""
    report: BugReport = llm.invoke(prompt)

    duplicates = find_duplicates(report.failure_category)

    report.github_duplicates.extend(str(duplicates))

    return report
