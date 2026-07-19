from dataclasses import dataclass, field

from evaluation.metrics import EvaluationEngine


@dataclass
class EvaluationRequest:
    """
        Generic request accepted by every evaluation provider.
        """
    prompt: str
    actual_output: str
    expected_output: str | None = None
    retrieval_context: list[str] = field(default_factory=list)
    metrics: list[str] = field(default_factory=list)
    engine: EvaluationEngine = EvaluationEngine.DEEPEVAL
