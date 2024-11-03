from typing import Any, Generator

from transformers.pipelines.base import Pipeline  # type: ignore


class PromptsManger:
    """For interacting with local LLMs"""

    def prompt_response(self, prompt: str, model: Pipeline) -> str:
        """Prompt LLM for response"""
        outputs: Generator[Any, Any, None] = model(
            prompt, max_length=100, num_return_sequences=1
        )  # type: ignore
        return " ".join([output["generated_text"] for output in outputs])


prompts_manager = PromptsManger()
