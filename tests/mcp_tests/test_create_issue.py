import asyncio

from src.agents.result import GithubIssue
from src.mcp_integration.client.github_client import create_issue


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
