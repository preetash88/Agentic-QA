from src.mcp_integration.registry import MCPRegistry
from src.mcp_integration.discovery import ToolDiscovery


class MCPManager:
    def __init__(self):
        self.registry = MCPRegistry()
        self.discovery = ToolDiscovery(
            self.registry,
        )
        self.catalog = None

    async def initialize(self):
        self.catalog = await self.discovery.discover()

    def get_tool(self, tool_name: str):
        return self.catalog.get(tool_name)

    def list_tools(self):
        return self.catalog.all_tools()

    def browser_tools(self):
        return self.catalog.by_server("playwright")

    def github_tools(self):
        return self.catalog.by_server("github")

    def filesystem_tools(self):
        return self.catalog.by_server("filesystem")


manager = MCPManager()
