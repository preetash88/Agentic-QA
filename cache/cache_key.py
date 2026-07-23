import hashlib
from typing import Optional

from pydantic import schema


def generate_cache_key(
        agent_name: str,
        model: str,
        prompt: str,
        schema_name: Optional[str] = None,

):
    value = (
        f"{agent_name}|"
        f"{model}|"
        f"{schema_name or "text"}|"
        f"{prompt}"
    )

    return hashlib.sha256(value.encode("utf-8")).hexdigest()
