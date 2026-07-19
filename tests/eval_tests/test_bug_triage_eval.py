from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase


metric = AnswerRelevancyMetric(
    threshold=0.7
)

test_case = LLMTestCase(
    input="JWT expired",
    actual_output="""
Authentication failure caused by
expired JWT token.
"""
)

metric.measure(
    test_case
)

print(metric.score)