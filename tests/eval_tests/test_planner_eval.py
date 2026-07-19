from agents.planner_agent import generate_test_plan
from evaluation.evaluator import Evaluator
from evaluation.metrics import MetricFactory


def test_planner_eval():
    requirement = """
    User logs into application using email and password.    
    """
    result = generate_test_plan(requirement)

    evaluation = Evaluator.evaluate(
        metric=MetricFactory.answer_relevancy(),
        input_text=requirement,
        actual_output=result.model_dump_json(indent=2)
    )

    print(evaluation.model_dump_json(indent=2))
