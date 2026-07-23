from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ToolDefinition:
    server: str
    name: str
    description: str
    input_schema: dict[str, Any]
    annotations: dict[str, Any] | None = None


@dataclass(slots=True)
class ToolExecutionResult:
    success: bool
    tool: str
    server: str
    result: Any = None
    error: str | None = None
