from deepeval.models import DeepEvalBaseLLM
from langchain_ollama import ChatOllama


class OllamaDeepeval(DeepEvalBaseLLM):

    def __init__(
            self,
            model: str = "qwen3:8b",
            temperature: float = 0.0
    ):
        self.temperature = temperature
        super().__init__(model=model)

    def load_model(self):
        return ChatOllama(model=self.name,temperature=self.temperature)

    def generate(self, prompt: str, **kwargs) -> str:
        response = self.model.invoke(prompt)

        if hasattr(response, "content"):
            return response.content

        return str(response)

    async def a_generate(self, prompt: str, **kwargs) -> str:

        response = await self.model.ainvoke(prompt)

        if hasattr(response, "content"):
            return response.content

        return str(response)

    def get_model_name(self):
        return self.name
