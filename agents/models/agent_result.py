from typing import TypeVar, Generic

from pydantic import BaseModel

T = TypeVar("T")

class AgentResult(BaseModel, Generic[T]):
    output: T
    evaluation: dict | None = None
    execution_time_ms: float | None = None
