from typing import Any, Optional
from functools import lru_cache
import torch
from transformers.models.auto.configuration_auto import AutoConfig
from transformers.pipelines import pipeline
from transformers.pipelines.base import Pipeline
from pydantic import BaseModel

class ModelConfig(BaseModel):
    pad_token_id: Optional[int] = None
    eos_token_id: Optional[int] = None

MODEL_NAME = "gpt2"

hf_config: Any = AutoConfig.from_pretrained(MODEL_NAME)
config = ModelConfig(
    pad_token_id=hf_config.pad_token_id or hf_config.eos_token_id,
    eos_token_id=hf_config.eos_token_id
)

@lru_cache()  # Cache the model instance
def get_model() -> Pipeline:
    device = 0 if torch.cuda.is_available() else -1

    generator: Pipeline = pipeline(
        task="text-generation",
        model=MODEL_NAME,
        device=device,
        pad_token_id=config.pad_token_id
    )
    return generator
