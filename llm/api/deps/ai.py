from functools import lru_cache
from transformers import pipeline
from transformers.pipelines.base import Pipeline
import torch

MODEL_NAME = "gpt2"

@lru_cache()
def get_model() -> Pipeline:
    generator: Pipeline = pipeline(
        task="text-generation",
        model=MODEL_NAME
    )
    return generator
