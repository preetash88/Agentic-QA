import asyncio

from src.mcp_integration.client.github_client import get_github_tools


def test_github_tools():
    tools = asyncio.run(get_github_tools())

    for tool in tools.tools:
        if tool.name == "issue_write":
            print(tool.inputSchema)

    # assert len(tools.tools) > 0