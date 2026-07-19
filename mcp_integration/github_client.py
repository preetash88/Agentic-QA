import os

import httpx
from dotenv import load_dotenv
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

from agents.models import GithubIssue

load_dotenv()

github_pat = os.getenv("GITHUB_MCP_PAT")


async def get_github_tools():
    if not github_pat:
        raise Exception("GITHUB_MCP_PAT not defined")

    async with httpx.AsyncClient(headers={
        "Authorization": f"Bearer {github_pat}"
    }) as http_client:
        async with streamable_http_client(
                "https://api.githubcopilot.com/mcp/",
                http_client=http_client,
        ) as (read, write, _):
            async with ClientSession(read, write) as session:
                await session.initialize()

                return await session.list_tools()


async def execute_github_tool(tool_name: str, arguments: dict):
    async with httpx.AsyncClient(headers={
        "Authorization": f"Bearer {github_pat}"
    }) as http_client:
        async with streamable_http_client(
                "https://api.githubcopilot.com/mcp/",
                http_client=http_client,
        ) as (read, write, _):
            async with ClientSession(read, write) as session:
                await session.initialize()

                return await session.call_tool(tool_name, arguments)


async def create_issue(owner: str, repo: str, issue: GithubIssue):
    return await execute_github_tool(
        "issue_write",
        {
            "method": "create",
            "owner": owner,
            "repo": repo,
            "title": issue.title,
            "body": issue.body,
            "labels": issue.labels,
            "assignees": issue.assignees,
        }
    )
