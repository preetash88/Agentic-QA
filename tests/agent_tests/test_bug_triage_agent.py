import asyncio

from src.agents.bug_triage_agent import analyze_failure
from src.mcp_integration.client.filesystem_client import read_text_file


def test_bug_triage_agent():
    app_logs = asyncio.run(read_text_file("F:\\QA_SDET\\artifacts\\sample_failure.log"))

    console_logs = asyncio.run(read_text_file("F:\\QA_SDET\\artifacts\\console.log"))

    playwright_logs = asyncio.run(read_text_file("F:\\QA_SDET\\artifacts\\playwright_error.txt"))

    result = analyze_failure(app_logs, console_logs, playwright_logs)

    print(result.model_dump_json(indent=4))

    assert result is not None
