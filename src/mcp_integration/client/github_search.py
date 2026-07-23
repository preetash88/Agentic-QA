from src.mcp_integration.client.github_client import execute_github_tool


async def search_issues(owner: str, repo: str, query: str):
    return await execute_github_tool(
        "search_issues",
        {
            "query": query

        })
