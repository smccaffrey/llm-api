"""
This type stub file was generated by pyright.
"""

from typing import TYPE_CHECKING
from ...utils import OptionalDependencyNotAvailable, _LazyModule, is_tokenizers_available, is_torch_available, is_vision_available
from .configuration_layoutlmv2 import LayoutLMv2Config
from .processing_layoutlmv2 import LayoutLMv2Processor
from .tokenization_layoutlmv2 import LayoutLMv2Tokenizer

_import_structure = ...
if not is_tokenizers_available():
    ...
if not is_vision_available():
    ...
if not is_torch_available():
    ...
if TYPE_CHECKING:
    ...
else:
    ...
