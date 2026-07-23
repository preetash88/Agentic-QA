import asyncio

from src.agents import analyze_ui_failure
from src.mcp_integration.client.playwright_client import execute_playwright_tool


def test_ui_triage():
    asyncio.run(
        execute_playwright_tool(
            "browser_navigate",
            {
                "url": "https://automationexercise.com/"
            }
        )
    )

    snapshot = asyncio.run(
        execute_playwright_tool(
            "browser_snapshot",
            {}
        )
    )

    console = asyncio.run(
        execute_playwright_tool(
            "browser_console_messages",
            {}
        )
    )

    result = analyze_ui_failure(
        str(snapshot),
        str(console)
    )

    print(
        result.model_dump_json(
            indent=4
        )
    )

    assert result.root_cause is not None
