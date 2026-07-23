from abc import ABC, abstractmethod


class EvaluationProvider(ABC):

    @abstractmethod
    def evaluate(
            self,
            metric,
            input_text: str,
            actual_output: str,
            expected_output: str | None = None,
            retrieval_context: list[str] | None = None
    ):
        pass
