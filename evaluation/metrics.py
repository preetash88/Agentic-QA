from enum import Enum

from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric, HallucinationMetric

from config.llm_config import DEFAULT_EVALUATION_MODEL, DEFAULT_TEMPERATURE
from evaluation.models.ollama_deepeval import OllamaDeepeval


class EvaluationEngine(Enum):
    DEEPEVAL = "deepeval"


class MetricFactory:
    _model = OllamaDeepeval(model=DEFAULT_EVALUATION_MODEL, temperature=DEFAULT_TEMPERATURE)

    @classmethod
    def answer_relevancy(cls):
        return AnswerRelevancyMetric(model=cls._model, threshold=0.75)

    @classmethod
    def faithfulness(cls):
        return FaithfulnessMetric(model=cls._model, threshold=0.75)

    @classmethod
    def hallucination(cls):
        return HallucinationMetric(model=cls._model, threshold=0.3)
