import asyncio

from src.mcp_integration.client.playwright_client import (
    execute_playwright_tool
)


def test_playwright_snapshot():
    asyncio.run(execute_playwright_tool(
        "browser_navigate",
        {
            "url": "https://example.com"
        }
    )
    )

    result = asyncio.run(execute_playwright_tool(
        "browser_snapshot",
        {"path": "F:\\QA_SDET\\snapshot"}
    )
    )

    print(result.model_dump_json(indent=4)
          )

    assert result.isError is False
