import json
import shutil
import subprocess
import tempfile
from pathlib import Path

import yaml

from evaluation.models.evaluation_result import EvaluationResult
from evaluation.providers.base_provider import EvaluationProvider


class PromptfooProvider(EvaluationProvider):
    """
        Promptfoo evaluation provider.

        A temporary Promptfoo configuration is generated for every
        EvaluationRequest, executed, parsed and then deleted.
        """
    ASSERTION_MAPPING = {
        "contains": "contains",
        "equals": "equals",
        "similar": "similar",
        "regex": "regex",
        "starts-with": "starts-with",
        "ends-with": "ends-with",
    }

    def evaluate(
            self,
            metric,
            input_text,
            actual_output,
            expected_output=None,
            retrieval_context=None,
    ):
        # output_file = Path("promptfoo-result.json")

        npx = shutil.which("npx")

        if npx is None:
            raise RuntimeError("npx executable not found")

        assertion = self.ASSERTION_MAPPING.get(metric)

        if assertion is None:
            raise ValueError(f"Unsupported Promptfoo assertion : {metric}")

        with tempfile.TemporaryDirectory() as temp_dir:

            temp_dir = Path(temp_dir)

            config_file = temp_dir / "promptfoo.yaml"
            result_file = temp_dir / "result.json"

            config = {
                "description": "Runtime Promptfoo Evaluation",
                "providers": [
                    {
                        "id": "ollama:qwen3:8b"
                    }
                ],
                "prompts": [
                    "{{prompt}}"
                ],
                "tests": [
                    {
                        "vars": {
                            "prompt": input_text
                        },
                        "assert": [
                            {
                                "type": assertion,
                                "value": expected_output
                            }
                        ]
                    }
                ]
            }

            with open(config_file, "w", encoding="utf-8") as f:
                yaml.safe_dump(config, f, sort_keys=False, allow_unicode=True)

            subprocess.run(
                [
                    npx,
                    "promptfoo",
                    "eval",
                    "-c",
                    str(config_file),
                    "--output",
                    str(result_file),
                ],
                check=True,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
            )

            with open(result_file, "r", encoding="utf-8") as f:
                report = json.load(f)

            grading = report["results"]["results"][0]["gradingResult"]

            return EvaluationResult(
                engine="Promptfoo",
                metric=metric,
                score=float(grading["score"]),
                passed=bool(grading["pass"]),
                reason=grading["reason"],
                latency=report["results"]["results"][0]["latencyMs"] / 1000,

            )
