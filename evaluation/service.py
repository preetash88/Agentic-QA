from evaluation.metrics import EvaluationEngine
from evaluation.models.evaluation_request import EvaluationRequest
from evaluation.providers.deepeval_provider import DeepevalProvider


class EvaluationService:
    def __init__(self):
        self._providers = {
            EvaluationEngine.DEEPEVAL: DeepevalProvider(),
        }

    def evaluate(self, request: EvaluationRequest):
        provider = self._providers.get(request.engine)

        if provider is None:
            raise ValueError(f"No provider found for engine {request.engine}")

        results = []

        for metric in request.metrics:
            result = provider.evaluate(
                metric=metric,
                input_text=request.prompt,
                actual_output=request.actual_output,
                expected_output=request.expected_output,
                retrieval_context=request.retrieval_context,
            )

            results.append(result)

        return results
