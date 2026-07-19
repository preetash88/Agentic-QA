import asyncio

from mcp_integration.playwright_client import (
    execute_playwright_tool
)


def test_console_messages():

    asyncio.run(
        execute_playwright_tool(
            "browser_navigate",
            {
                "url": "https://example.com"
            }
        )
    )

    result = asyncio.run(
        execute_playwright_tool(
            "browser_console_messages",
            {}
        )
    )

    print(
        result.model_dump_json(
            indent=4
        )
    )

    assert result.isError is False