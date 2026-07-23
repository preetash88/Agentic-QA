from src.evaluation import EvaluationEngine
from src.evaluation.models.evaluation_request import EvaluationRequest
from src.evaluation import EvaluationService


def test_promptfoo():
    service = EvaluationService()

    request = EvaluationRequest(
        prompt="What is the capital of Iceland?",
        actual_output="",
        expected_output="Reykjavik",
        metrics=["contains"],
        engine=EvaluationEngine.PROMPTFOO,
    )

    results = service.evaluate(request)

    for result in results:
        print(result.model_dump_json(indent=2))

# import shutil
# print(shutil.which("npx"))