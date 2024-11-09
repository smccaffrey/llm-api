"""
This type stub file was generated by pyright.
"""

import numpy as np
from typing import List, Optional, Union
from ....feature_extraction_sequence_utils import SequenceFeatureExtractor
from ....feature_extraction_utils import BatchFeature
from ....file_utils import PaddingStrategy, TensorType

"""
Feature extractor class for M-CTC-T
"""
logger = ...
class MCTCTFeatureExtractor(SequenceFeatureExtractor):
    r"""
    Constructs a M-CTC-T feature extractor.

    This feature extractor inherits from [`~feature_extraction_sequence_utils.SequenceFeatureExtractor`] which contains
    most of the main methods. Users should refer to this superclass for more information regarding those methods. This
    code has been adapted from Flashlight's C++ code. For more information about the implementation, one can refer to
    this [notebook](https://colab.research.google.com/drive/1GLtINkkhzms-IsdcGy_-tVCkv0qNF-Gt#scrollTo=pMCRGMmUC_an)
    that takes the user step-by-step in the implementation.

    Args:
        feature_size (`int`, defaults to 80):
            The feature dimension of the extracted features. This is the number of mel_frequency
        sampling_rate (`int`, defaults to 16000):
            The sampling rate at which the audio files should be digitalized expressed in hertz (Hz).
        padding_value (`float`, defaults to 0.0):
            The value that is used to fill the padding values.
        hop_length (`int`, defaults to 10):
            Number of audio samples between windows. Otherwise referred to as "shift" in many papers.
        win_length (`int`, defaults to 25):
            Number of ms per window
        win_function (`str`, defaults to `"hamming_window"`):
            Name for the window function used for windowing, must be accessible via `torch.{win_function}`
        frame_signal_scale (`float`, defaults to 32768.0):
            Constant multiplied in creating the frames before applying DFT.
        preemphasis_coeff (`float`, defaults to 0.97):
            Constant multiplied in applying Pre-emphasis before DFT.
        mel_floor (`float` defaults to 1.0):
            Minimum value of mel frequency banks.
        normalize_means (`bool`, *optional*, defaults to `True`):
            Whether or not to zero-mean normalize the extracted features.
        normalize_vars (`bool`, *optional*, defaults to `True`):
            Whether or not to unit-variance normalize the extracted features.
    """
    model_input_names = ...
    def __init__(self, feature_size=..., sampling_rate=..., padding_value=..., hop_length=..., win_length=..., win_function=..., frame_signal_scale=..., preemphasis_coeff=..., mel_floor=..., normalize_means=..., normalize_vars=..., return_attention_mask=..., **kwargs) -> None:
        ...
    
    def normalize(self, input_features: List[np.ndarray], attention_mask: Optional[np.ndarray] = ...) -> List[np.ndarray]:
        ...
    
    def __call__(self, raw_speech: Union[np.ndarray, List[float], List[np.ndarray], List[List[float]]], padding: Union[bool, str, PaddingStrategy] = ..., max_length: Optional[int] = ..., truncation: bool = ..., pad_to_multiple_of: Optional[int] = ..., return_attention_mask: Optional[bool] = ..., return_tensors: Optional[Union[str, TensorType]] = ..., sampling_rate: Optional[int] = ..., **kwargs) -> BatchFeature:
        """
        Main method to featurize and prepare for the model one or several sequence(s). sequences. It returns the
        log-mel spectrogram of the input audio, as implemented in the original Flashlight MFSC feature extraction code.

        Args:
            raw_speech (`torch.Tensor`, `np.ndarray`, `List[float]`, `List[torch.Tensor]`, `List[np.ndarray]`, `List[List[float]]`):
                The sequence or batch of sequences to be padded. Each sequence can be a tensor, a numpy array, a list
                of float values, a list of tensors, a list of numpy arrays or a list of list of float values. Must be
                mono channel audio, not stereo, i.e. single float per timestep.
            padding (`bool`, `str` or [`~file_utils.PaddingStrategy`], *optional*, defaults to `False`):
                Select a strategy to pad the returned sequences (according to the model's padding side and padding
                index) among:

                - `True` or `'longest'`: Pad to the longest sequence in the batch (or no padding if only a single
                  sequence if provided).
                - `'max_length'`: Pad to a maximum length specified with the argument `max_length` or to the maximum
                  acceptable input length for the model if that argument is not provided.
                - `False` or `'do_not_pad'` (default): No padding (i.e., can output a batch with sequences of different
                  lengths).
            max_length (`int`, *optional*):
                Maximum length of the returned list and optionally padding length (see above).
            truncation (`bool`):
                Activates truncation to cut input sequences longer than *max_length* to *max_length*.
            pad_to_multiple_of (`int`, *optional*):
                If set will pad the sequence to a multiple of the provided value.

                This is especially useful to enable the use of Tensor Cores on NVIDIA hardware with compute capability
                `>= 7.5` (Volta), or on TPUs which benefit from having sequence lengths be a multiple of 128.
            return_attention_mask (`bool`, *optional*):
                Whether to return the attention mask. If left to the default, will return the attention mask according
                to the specific feature_extractor's default.

                [What are attention masks?](../glossary#attention-mask)

            return_tensors (`str` or [`~file_utils.TensorType`], *optional*):
                If set, will return tensors instead of list of python integers. Acceptable values are:

                - `'tf'`: Return TensorFlow `tf.constant` objects.
                - `'pt'`: Return PyTorch `torch.Tensor` objects.
                - `'np'`: Return Numpy `np.ndarray` objects.
            sampling_rate (`int`, *optional*):
                The sampling rate at which the `raw_speech` input was sampled. It is strongly recommended to pass
                `sampling_rate` at the forward call to prevent silent errors.
            padding_value (`float`, defaults to 0.0):
        """
        ...
    

