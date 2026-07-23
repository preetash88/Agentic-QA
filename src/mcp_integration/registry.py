from src.mcp_integration.client.filesystem_client import get_filesystem_tools, execute_filesystem_tool
from src.mcp_integration.client.github_client import get_github_tools, execute_github_tool
from src.mcp_integration.client.playwright_client import get_playwright_tools, execute_playwright_tool


class MCPRegistry:
    def __init__(self):
        self._servers = {
            "playwright": (get_playwright_tools, execute_playwright_tool),
            "github": (get_github_tools, execute_github_tool),
            "filesystem": (get_filesystem_tools, execute_filesystem_tool),
        }

    def registered_servers(self) -> list[str]:
        return list(self._servers.keys())

    async def list_tools(self, server: str):
        if server not in self._servers:
            raise ValueError(f"Server {server} is not registered")

        getter, _ = self._servers[server]
        return await getter()

    async def execute(self, server: str, tool_name: str, arguments: dict):
        if server not in self._servers:
            raise ValueError(f"Unknown MCP server: {server}")
        _, executor = self._servers[server]
        return await executor(tool_name, arguments)
