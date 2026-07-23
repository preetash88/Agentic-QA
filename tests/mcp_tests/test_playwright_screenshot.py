import asyncio

from src.mcp_integration.client.playwright_client import (
    execute_playwright_tool
)


def test_screenshot():

    asyncio.run(
        execute_playwright_tool(
            "browser_navigate",
            {
                "url": "https://automationexercise.com/"
            }
        )
    )

    result = asyncio.run(
        execute_playwright_tool(
            "browser_take_screenshot",
            {
                "filename": "example.png"
            }
        )
    )

    print(
        result.model_dump_json(
            indent=4
        )
    )

    assert result.isError is False