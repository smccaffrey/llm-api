"""
This type stub file was generated by pyright.
"""

from typing import Optional
from huggingface_hub import Discussion, HfApi

logger = ...
def previous_pr(api: HfApi, model_id: str, pr_title: str, token: str) -> Optional[Discussion]:
    ...

def spawn_conversion(token: str, private: bool, model_id: str): # -> None:
    ...

def get_conversion_pr_reference(api: HfApi, model_id: str, **kwargs): # -> str:
    ...

def auto_conversion(pretrained_model_name_or_path: str, ignore_errors_during_conversion=..., **cached_file_kwargs): # -> tuple[None, None] | tuple[str | None, str, bool] | None:
    ...
