from mcp import StdioServerParameters, stdio_client, ClientSession


def get_playwright_server():
    return StdioServerParameters(
        command="cmd",
        args=[
            "/c",
            "npx",
            "@playwright/mcp@latest"
        ])


async def get_playwright_tools():
    async with stdio_client(get_playwright_server()) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            return await session.list_tools()


async def execute_playwright_tool(tool_name: str, arguments: dict):
    async with stdio_client(get_playwright_server()) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            result = await session.call_tool(tool_name, arguments)
            return result
