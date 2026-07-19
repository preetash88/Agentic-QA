from abc import ABC, abstractmethod
from typing import TypeVar, Generic

TInput = TypeVar("TInput")
TOutput = TypeVar("TOutput")


class BaseAgent(ABC, Generic[TInput, TOutput]):

    @abstractmethod
    def run(self, input_data: TInput) -> TOutput:
        """Execute the agent."""
        raise NotImplementedError

    @abstractmethod
    def evaluate(self, input_data: TInput, output_data: TOutput):
        """Evaluate the agent output."""
        raise NotImplementedError
