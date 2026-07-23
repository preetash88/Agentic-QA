from src.mcp_integration.models import ToolDefinition


class ToolCatalog:
    def __init__(self):
        self._tools: dict[str, ToolDefinition] = {}

    def register(self, tool: ToolDefinition):
        key = f"{tool.server}.{tool.name}"
        self._tools[key] = tool

    def get(self, tool_name: str) -> ToolDefinition | None:
        return self._tools.get(tool_name)

    def all_tools(self):
        return list(self._tools.values())

    def by_server(self, server: str):
        return [tool for tool in self._tools.values() if tool.server == server]

    def clear(self):
        self._tools.clear()
