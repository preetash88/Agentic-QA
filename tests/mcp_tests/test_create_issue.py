import asyncio

from agents.models import GithubIssue
from mcp_integration.github_client import create_issue


def test_create_issue():
    issue = GithubIssue(
        title="MCP Test Issue",
        body="The issue was created by MCP.",
        labels=["mcp-test"]
    )

    result = asyncio.run(
        create_issue(
            owner="preetash88",
            repo="github-mcp-test",
            issue=issue
        )
    )

    print(result)
