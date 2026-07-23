import asyncio

from src.mcp_integration.client.playwright_client import execute_playwright_tool


def test_playwright_navigation():
    result = asyncio.run(execute_playwright_tool("browser_navigate", {
        "url": "https://automationexercise.com/"
    }))

    print(result.model_dump_json(indent=4))

    assert result.isError is False
