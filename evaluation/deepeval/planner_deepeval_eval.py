from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase

metric = AnswerRelevancyMetric(threshold=0.7)


def evaluate_answer(input_text, actual_output):
    test_case = LLMTestCase(input=input_text, actual_output=actual_output)

    metric.measure(test_case)

    return {
        "score": metric.score,
        "reason": metric.reason,
        "passed": metric.success
    }
