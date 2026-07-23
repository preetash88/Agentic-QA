import os
from typing import TypeVar, Any, Callable

from langsmith import Client

from src.config.observability import observability_config

T = TypeVar("T")


class LangsmithTracer:
    def __init__(self):
        if observability_config.langsmith_api_key:
            os.environ["LANGCHAIN_TRACING_V2"] = observability_config.langchain_tracing_v2
            os.environ["LANGCHAIN_PROJECT"] = observability_config.langchain_project
            os.environ["LANGSMITH_TRACING_V2"] = observability_config.langsmith_tracing_v2
            os.environ["LANGSMITH_PROJECT"] = observability_config.langsmith_project
            if observability_config.langsmith_endpoint:
                os.environ["LANGSMITH_ENDPOINT"] = observability_config.langsmith_endpoint
            os.environ["LANGSMITH_API_KEY"] = observability_config.langsmith_api_key

        self.client = Client() if observability_config.langsmith_api_key else None

    def enabled(self) -> bool:
        return self.client is not None

    def annotate(self, name: str, payload: dict[str, Any]):
        if not self.client:
            return
        try:
            self.client.create_run(
                name=name,
                run_type="chain",
                inputs=payload,
            )
        except Exception:
            pass

    def wrap(self, name: str, fn: Callable[..., T], *args: Any, **kwargs: Any) -> T:
        return fn(*args, **kwargs)


tracer = LangsmithTracer()
