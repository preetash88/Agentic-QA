from deepeval.test_case import LLMTestCase

from evaluation.providers.deepeval_provider import DeepevalProvider


class Evaluator:
    _provider = DeepevalProvider()

    @classmethod
    def evaluate(cls, **kwargs):
        return cls._provider.evaluate(**kwargs)
