from evaluation.metrics import EvaluationEngine
from evaluation.models.evaluation_request import EvaluationRequest
from evaluation.service import EvaluationService

print("1. Creating service...")
service = EvaluationService()
print("✓ Service created")

request = EvaluationRequest(
    prompt="What is the capital of Iceland?",
    actual_output="The capital of Iceland is Reykjavik",
    expected_output="Reykjavik",
    metrics=["answer_relevancy", "faithfulness"],
    engine=EvaluationEngine.DEEPEVAL
)

print("2. Request created")

print("3. Calling evaluate()")
results = service.evaluate(request)

print("4. Evaluation finished")

for result in results:
    print(result.model_dump())
