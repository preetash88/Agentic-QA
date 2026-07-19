from deepeval.test_case import LLMTestCase

from evaluation.metrics import MetricFactory
from evaluation.models.evaluation_result import EvaluationResult
from evaluation.providers.base_provider import EvaluationProvider


class DeepevalProvider(EvaluationProvider):
    def evaluate(
            self,
            metric,
            input_text: str,
            actual_output: str,
            expected_output: str | None = None,
            retrieval_context: list[str] | None = None,
    ) -> EvaluationResult:
        test_case = LLMTestCase(
            input=input_text,
            actual_output=actual_output,
            expected_output=expected_output,
            retrieval_context=retrieval_context or []
        )

        if metric == "answer_relevancy":
            metric_obj = MetricFactory.answer_relevancy()

        elif metric == "faithfulness":
            metric_obj = MetricFactory.faithfulness()

        elif metric == "hallucination":
            metric_obj = MetricFactory.hallucination()

        else:
            raise ValueError(f"Unknown metric: {metric}")

        metric_obj.measure(test_case)

        return EvaluationResult(
            engine="DeepEval",
            metric=metric,
            score=metric_obj.score,
            passed=metric_obj.success,
            reason=metric_obj.reason,
        )
