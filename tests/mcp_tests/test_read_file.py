import asyncio
import json

from mcp_integration.filesystem_client import execute_filesystem_tool


def test_read_file():

    result = asyncio.run(execute_filesystem_tool(
        "read_text_file",
        {
            "path":"F:\\QA_SDET\\artifacts\\sample_failure.log"
        }
    ))

    print("\n===== FILE CONTENT =====\n")
    print(result.structuredContent["content"])
    print("\n========================\n")

    print("\n===== FILE CONTENT in JSON=====\n")
    print(json.dumps(result.structuredContent, indent=4))
    print("\n========================\n")
    # assert result is not None