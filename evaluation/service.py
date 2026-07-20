import time
import traceback

from evaluation.metrics import EvaluationEngine
from evaluation.models.evaluation_request import EvaluationRequest
from evaluation.models.evaluation_result import EvaluationResult
from evaluation.providers.deepeval_provider import DeepevalProvider
from evaluation.providers.promptfoo_provider import PromptfooProvider
from reporting.allure_reporter import AllureReporter


class EvaluationService:
    def __init__(self):
        self._providers = {
            EvaluationEngine.DEEPEVAL: DeepevalProvider(),
            EvaluationEngine.PROMPTFOO: PromptfooProvider()
        }
        self._allure = AllureReporter()

    def evaluate(self, request: EvaluationRequest):
        provider = self._providers.get(request.engine)

        if provider is None:
            raise ValueError(f"No provider found for engine {request.engine}")

        results = []

        for metric in request.metrics:
            start = time.perf_counter()
            try:
                result = provider.evaluate(
                    metric=metric,
                    input_text=request.prompt,
                    actual_output=request.actual_output,
                    expected_output=request.expected_output,
                    retrieval_context=request.retrieval_context,
                )

                result.latency = round(time.perf_counter() - start, 3)
            except Exception as ex:
                traceback.print_exc()

                result = EvaluationResult(
                    engine=request.engine.value,
                    metric=metric,
                    score=0.0,
                    passed=False,
                    reason=str(ex),
                    latency=round(time.perf_counter() - start, 3),
                )

            self._allure.report(result)

            results.append(result)

        return results
