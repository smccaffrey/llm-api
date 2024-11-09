"""
This type stub file was generated by pyright.
"""

from typing import TYPE_CHECKING
from ...utils import OptionalDependencyNotAvailable, _LazyModule, is_flax_available, is_tf_available, is_torch_available
from .auto_factory import get_values
from .configuration_auto import AutoConfig, CONFIG_MAPPING, MODEL_NAMES_MAPPING
from .feature_extraction_auto import AutoFeatureExtractor, FEATURE_EXTRACTOR_MAPPING
from .image_processing_auto import AutoImageProcessor, IMAGE_PROCESSOR_MAPPING
from .processing_auto import AutoProcessor, PROCESSOR_MAPPING
from .tokenization_auto import AutoTokenizer, TOKENIZER_MAPPING

_import_structure = ...
if not is_torch_available():
    ...
if not is_tf_available():
    ...
if not is_flax_available():
    ...
if TYPE_CHECKING:
    ...
else:
    ...