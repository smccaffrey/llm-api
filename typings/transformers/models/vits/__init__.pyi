"""
This type stub file was generated by pyright.
"""

from typing import TYPE_CHECKING
from ...utils import OptionalDependencyNotAvailable, _LazyModule, is_sentencepiece_available, is_speech_available, is_torch_available
from .configuration_vits import VitsConfig
from .tokenization_vits import VitsTokenizer

_import_structure = ...
if not is_torch_available():
    ...
if TYPE_CHECKING:
    ...
else:
    ...
