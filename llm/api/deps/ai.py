from functools import lru_cache
from transformers import pipeline  # type: ignore
from transformers.pipelines.base import Pipeline  # type: ignore

MODEL_NAME = "gpt2"


@lru_cache()  # caches model not data
def get_model() -> Pipeline:
    generator: Pipeline = pipeline(task="text-generation", model=MODEL_NAME)
    return generator
