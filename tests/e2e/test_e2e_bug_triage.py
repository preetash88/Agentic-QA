import asyncio

from src.agents.bug_triage_agent import analyze_failure
from src.agents.duplicate_detector import detect_duplicates
from src.agents.github_mapper import bug_report_github_issue
from src.mcp_integration.client.github_client import create_issue


def test_e2e_bug_triage():
    report = analyze_failure(
        logs="""
            JWT validation failed.
            Token expired.
            Authentication service returned 401 Unauthorized.
            """,
        console_logs=None,
        playwright_error="""
            locator("#dashboard")
            timeout 30000ms exceeded
            """
    )

    report = detect_duplicates(report)

    if report.is_duplicate:
        print("Duplicate issue detected")
        return

    github_issue = bug_report_github_issue(report)

    result = asyncio.run(
        create_issue(
            owner="preetash88",
            repo="github-mcp-test",
            issue=github_issue
        )
    )
    print(len(github_issue.body))

    print(result)

    assert result.isError is False
