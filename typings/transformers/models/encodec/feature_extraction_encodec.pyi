"""
This type stub file was generated by pyright.
"""

import numpy as np
from typing import List, Optional, Union
from ...feature_extraction_sequence_utils import SequenceFeatureExtractor
from ...feature_extraction_utils import BatchFeature
from ...utils import PaddingStrategy, TensorType

"""Feature extractor class for EnCodec."""
logger = ...
class EncodecFeatureExtractor(SequenceFeatureExtractor):
    r"""
    Constructs an EnCodec feature extractor.

    This feature extractor inherits from [`~feature_extraction_sequence_utils.SequenceFeatureExtractor`] which contains
    most of the main methods. Users should refer to this superclass for more information regarding those methods.

    Instantiating a feature extractor with the defaults will yield a similar configuration to that of the
    [facebook/encodec_24khz](https://huggingface.co/facebook/encodec_24khz) architecture.

    Args:
        feature_size (`int`, *optional*, defaults to 1):
            The feature dimension of the extracted features. Use 1 for mono, 2 for stereo.
        sampling_rate (`int`, *optional*, defaults to 24000):
            The sampling rate at which the audio waveform should be digitalized expressed in hertz (Hz).
        padding_value (`float`, *optional*, defaults to 0.0):
            The value that is used to fill the padding values.
        chunk_length_s (`float`, *optional*):
            If defined the audio is pre-processed into chunks of lengths `chunk_length_s` and then encoded.
        overlap (`float`, *optional*):
            Defines the overlap between each chunk. It is used to compute the `chunk_stride` using the following
            formulae : `int((1.0 - self.overlap) * self.chunk_length)`.
    """
    model_input_names = ...
    def __init__(self, feature_size: int = ..., sampling_rate: int = ..., padding_value: float = ..., chunk_length_s: float = ..., overlap: float = ..., **kwargs) -> None:
        ...
    
    @property
    def chunk_length(self) -> Optional[int]:
        ...
    
    @property
    def chunk_stride(self) -> Optional[int]:
        ...
    
    def __call__(self, raw_audio: Union[np.ndarray, List[float], List[np.ndarray], List[List[float]]], padding: Optional[Union[bool, str, PaddingStrategy]] = ..., truncation: Optional[bool] = ..., max_length: Optional[int] = ..., return_tensors: Optional[Union[str, TensorType]] = ..., sampling_rate: Optional[int] = ...) -> BatchFeature:
        """
        Main method to featurize and prepare for the model one or several sequence(s).

        Args:
            raw_audio (`np.ndarray`, `List[float]`, `List[np.ndarray]`, `List[List[float]]`):
                The sequence or batch of sequences to be processed. Each sequence can be a numpy array, a list of float
                values, a list of numpy arrays or a list of list of float values. The numpy array must be of shape
                `(num_samples,)` for mono audio (`feature_size = 1`), or `(2, num_samples)` for stereo audio
                (`feature_size = 2`).
            padding (`bool`, `str` or [`~utils.PaddingStrategy`], *optional*, defaults to `True`):
                Select a strategy to pad the returned sequences (according to the model's padding side and padding
                index) among:

                - `True` or `'longest'`: Pad to the longest sequence in the batch (or no padding if only a single
                  sequence if provided).
                - `'max_length'`: Pad to a maximum length specified with the argument `max_length` or to the maximum
                  acceptable input length for the model if that argument is not provided.
                - `False` or `'do_not_pad'` (default): No padding (i.e., can output a batch with sequences of different
                  lengths).
            truncation (`bool`, *optional*, defaults to `False`):
                Activates truncation to cut input sequences longer than `max_length` to `max_length`.
            max_length (`int`, *optional*):
                Maximum length of the returned list and optionally padding length (see above).
            return_tensors (`str` or [`~utils.TensorType`], *optional*):
                If set, will return tensors instead of list of python integers. Acceptable values are:

                - `'tf'`: Return TensorFlow `tf.constant` objects.
                - `'pt'`: Return PyTorch `torch.Tensor` objects.
                - `'np'`: Return Numpy `np.ndarray` objects.
            sampling_rate (`int`, *optional*):
                The sampling rate at which the `audio` input was sampled. It is strongly recommended to pass
                `sampling_rate` at the forward call to prevent silent errors.
        """
        ...
    

