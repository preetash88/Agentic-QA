from mcp import StdioServerParameters, stdio_client, ClientSession


def get_filesystem_server():
    return StdioServerParameters(
        command="cmd",
        args=[
            "/c",
            "npx",
            "-y",
            "@modelcontextprotocol/server-filesystem",
            "F:\\QA_SDET"
        ])


async def get_filesystem_tools():
    async with stdio_client(get_filesystem_server()) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()

            return tools


async def execute_filesystem_tool(tool_name: str, arguments: dict):
    async with stdio_client(get_filesystem_server()) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            response = await session.call_tool(tool_name, arguments)
            print("RAW MCP RESPONSE:")
            print(response)
            print(type(response))

            return response


async def read_text_file(path: str) -> str:
    result = await execute_filesystem_tool("read_text_file", {"path": path})

    if result.isError:
        raise Exception("Unable to read file")

    return result.structuredContent["content"].replace("\r\n", "\n").strip()
