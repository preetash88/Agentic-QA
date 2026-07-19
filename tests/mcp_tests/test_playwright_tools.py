import asyncio

from mcp_integration.playwright_client import get_playwright_tools


def test_playwright_tools():
    tools = asyncio.run(get_playwright_tools())

    for tool in tools.tools:
        print(tool.name)

    assert len(tools.tools) > 0