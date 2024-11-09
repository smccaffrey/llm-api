"""
This type stub file was generated by pyright.
"""

from typing import TYPE_CHECKING
from ...utils import OptionalDependencyNotAvailable, _LazyModule, is_sentencepiece_available, is_tokenizers_available, is_torch_available
from .configuration_seamless_m4t import SeamlessM4TConfig
from .feature_extraction_seamless_m4t import SeamlessM4TFeatureExtractor
from .processing_seamless_m4t import SeamlessM4TProcessor

_import_structure = ...
if not is_sentencepiece_available():
    ...
if not is_tokenizers_available():
    ...
if not is_torch_available():
    ...
if TYPE_CHECKING:
    ...
else:
    ...