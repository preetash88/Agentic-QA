import os
from dataclasses import dataclass


@dataclass(frozen=True)
class ObservabilityConfig:
    langsmith_api_key: str | None = os.getenv("LANGSMITH_API_KEY")
    langsmith_project: str | None = os.getenv("LANGSMITH_PROJECT", "QA_SDET")
    langsmith_tracing_v2: str = os.getenv("LANGSMITH_TRACING_V2", "true")
    langsmith_endpoint: str | None = os.getenv("LANGSMITH_ENDPOINT")
    langchain_tracing_v2: str | None = os.getenv("LANCHAIN_TRACING_V2", "true")
    langchain_project: str = os.getenv("LANCHAIN_PROJECT", "QA_SDET")


observability_config = ObservabilityConfig()
