from src.mcp_integration.manager import manager
from src.mcp_integration.models import ToolExecutionResult


class ToolExecutor:

    async def execute(self, tool_name: str, arguments: dict):
        tool = manager.get_tool(tool_name)

        if tool is None:
            return ToolExecutionResult(
                success=False,
                tool=tool_name,
                server="",
                error="Unknown Tool",
            )

        result = await manager.registry.execute(
            server=tool.server,
            tool_name=tool.name,
            arguments=arguments,
        )

        return ToolExecutionResult(
            success=True,
            tool=tool.name,
            server=tool.server,
            result=result,
        )


executor = ToolExecutor()
