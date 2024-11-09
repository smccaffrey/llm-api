"""
This type stub file was generated by pyright.
"""

from contextlib import contextmanager
from typing import List, Optional, Union
from ...processing_utils import ProcessingKwargs, ProcessorMixin, Unpack
from ...tokenization_utils_base import AudioInput, PreTokenizedInput, TextInput

"""
Speech processor class for Wav2Vec2
"""
class Wav2Vec2ProcessorKwargs(ProcessingKwargs, total=False):
    _defaults = ...


class Wav2Vec2Processor(ProcessorMixin):
    r"""
    Constructs a Wav2Vec2 processor which wraps a Wav2Vec2 feature extractor and a Wav2Vec2 CTC tokenizer into a single
    processor.

    [`Wav2Vec2Processor`] offers all the functionalities of [`Wav2Vec2FeatureExtractor`] and [`PreTrainedTokenizer`].
    See the docstring of [`~Wav2Vec2Processor.__call__`] and [`~Wav2Vec2Processor.decode`] for more information.

    Args:
        feature_extractor (`Wav2Vec2FeatureExtractor`):
            An instance of [`Wav2Vec2FeatureExtractor`]. The feature extractor is a required input.
        tokenizer ([`PreTrainedTokenizer`]):
            An instance of [`PreTrainedTokenizer`]. The tokenizer is a required input.
    """
    feature_extractor_class = ...
    tokenizer_class = ...
    def __init__(self, feature_extractor, tokenizer) -> None:
        ...
    
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, **kwargs): # -> tuple[Self, dict[str, Any]] | Self:
        ...
    
    def __call__(self, audio: AudioInput = ..., text: Optional[Union[str, List[str], TextInput, PreTokenizedInput]] = ..., images=..., videos=..., **kwargs: Unpack[Wav2Vec2ProcessorKwargs]):
        """
        When used in normal mode, this method forwards all its arguments to Wav2Vec2FeatureExtractor's
        [`~Wav2Vec2FeatureExtractor.__call__`] and returns its output. If used in the context
        [`~Wav2Vec2Processor.as_target_processor`] this method forwards all its arguments to PreTrainedTokenizer's
        [`~PreTrainedTokenizer.__call__`]. Please refer to the docstring of the above two methods for more information.
        """
        ...
    
    def pad(self, *args, **kwargs):
        """
        When used in normal mode, this method forwards all its arguments to Wav2Vec2FeatureExtractor's
        [`~Wav2Vec2FeatureExtractor.pad`] and returns its output. If used in the context
        [`~Wav2Vec2Processor.as_target_processor`] this method forwards all its arguments to PreTrainedTokenizer's
        [`~PreTrainedTokenizer.pad`]. Please refer to the docstring of the above two methods for more information.
        """
        ...
    
    def batch_decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to PreTrainedTokenizer's [`~PreTrainedTokenizer.batch_decode`]. Please
        refer to the docstring of this method for more information.
        """
        ...
    
    def decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to PreTrainedTokenizer's [`~PreTrainedTokenizer.decode`]. Please refer
        to the docstring of this method for more information.
        """
        ...
    
    @contextmanager
    def as_target_processor(self): # -> Generator[None, Any, None]:
        """
        Temporarily sets the tokenizer for processing the input. Useful for encoding the labels when fine-tuning
        Wav2Vec2.
        """
        ...
    

