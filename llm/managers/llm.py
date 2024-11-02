from typing import Any, Generator

from transformers import pipeline  # type: ignore


model_name = "gpt2"
generator = pipeline(
    task="text-generation",
    model=model_name
)


class LlmManger():
    """For interacting with local LLMs"""

    def prompt_response(self, prompt: str) -> str:
        """Prompt LLM for response"""
        outputs: Generator[Any, Any, None] = generator(
            prompt,
            max_length=50,
            num_return_sequences=1
        )  # type: ignore
        return " ".join([output["generated_text"] for output in outputs])

llm_manager = LlmManger()
