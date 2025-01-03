"""
This type stub file was generated by pyright.
"""

from typing import TYPE_CHECKING
from ...utils import OptionalDependencyNotAvailable, _LazyModule, is_sentencepiece_available, is_tf_available, is_torch_available
from .configuration_speech_to_text import Speech2TextConfig
from .feature_extraction_speech_to_text import Speech2TextFeatureExtractor
from .processing_speech_to_text import Speech2TextProcessor

_import_structure = ...
if not is_sentencepiece_available():
    ...
if not is_tf_available():
    ...
if not is_torch_available():
    ...
if TYPE_CHECKING:
    ...
else:
    ...
