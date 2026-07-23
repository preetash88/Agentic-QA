import asyncio

from src.mcp_integration.client.filesystem_client import get_filesystem_tools


def test_filesystem_mcp():
    tools = asyncio.run(get_filesystem_tools())
    # print(type(tools))

    for tool in tools.tools:
        print(tool.name)

    # assert len(tools.tools) > 0
