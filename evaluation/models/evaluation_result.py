from pydantic import BaseModel, Field


class EvaluationResult(BaseModel):
    """
        Normalized evaluation result returned by every evaluation provider.
        """
    engine: str = Field(...)
    metric: str = Field(...)
    score: float = Field(...)
    passed: bool = Field(...)
    reason: str = Field(...)
