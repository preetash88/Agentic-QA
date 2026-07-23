from src.mcp_integration.catalog import ToolCatalog
from src.mcp_integration.models import ToolDefinition


class ToolDiscovery:
    def __init__(self, registry):
        self.registry = registry
        self.catalog = ToolCatalog()

    async def discover(self):
        self.catalog.clear()

        for server in self.registry.registered_servers():
            tools = await self.registry.list_tools(server)
            for tool in tools:
                self.catalog.register(
                    ToolDefinition(
                        server=server,
                        name=tool.name,
                        description=tool.description,
                        input_schema=tool.input_schema,
                        annotations=getattr(tool, "annotations", None)
                    )
                )

        return self.catalog
