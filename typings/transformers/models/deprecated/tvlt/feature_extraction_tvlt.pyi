"""
This type stub file was generated by pyright.
"""

import numpy as np
from typing import List, Optional, Union
from ....feature_extraction_sequence_utils import BatchFeature, SequenceFeatureExtractor
from ....utils import TensorType

"""Feature extractor class for TVLT."""
logger = ...
class TvltFeatureExtractor(SequenceFeatureExtractor):
    r"""
    Constructs a TVLT audio feature extractor. This feature extractor can be used to prepare audios for the model.

    This feature extractor inherits from [`FeatureExtractionMixin`] which contains most of the main methods. Users
    should refer to this superclass for more information regarding those methods.

    Args:
        spectrogram_length (`Dict[str, int]` *optional*, defaults to 2048):
            The time length of each audio spectrogram.
        num_channels (`int` *optional*, defaults to 1):
            Number of audio channels.
        patch_size (`List[int]` *optional*, defaults to `[16, 16]`):
            The patch size of audio patch embedding.
        feature_size (`int`, *optional*, defaults to 128):
            The frequency length of audio spectrogram.
        sampling_rate (`int`, *optional*, defaults to 44100):
            The sampling rate at which the audio files should be digitalized expressed in Hertz (Hz).
        hop_length_to_sampling_rate (`int`, *optional*, defaults to 86):
            Hop length is length of the overlaping windows for the STFT used to obtain the Mel Frequency coefficients.
            For example, with sampling rate 44100, the hop length is 512, with 44100 / 512 = 86
        n_fft (`int`, *optional*, defaults to 2048):
            Size of the Fourier transform.
        padding_value (`float`, *optional*, defaults to 0.0):
            Padding value used to pad the audio. Should correspond to silences.
    """
    model_input_names = ...
    def __init__(self, spectrogram_length=..., num_channels=..., patch_size=..., feature_size=..., sampling_rate=..., hop_length_to_sampling_rate=..., n_fft=..., padding_value=..., **kwargs) -> None:
        ...
    
    def __call__(self, raw_speech: Union[np.ndarray, List[float], List[np.ndarray], List[List[float]]], return_tensors: Optional[Union[str, TensorType]] = ..., return_attention_mask: Optional[bool] = ..., sampling_rate: Optional[int] = ..., resample: bool = ..., mask_audio: bool = ..., **kwargs) -> BatchFeature:
        """
        Main method to prepare one or several audio(s) for the model.

        Args:
            raw_speech (`np.ndarray`, `List[float]`, `List[np.ndarray]`, `List[List[float]]`):
                The sequence or batch of sequences to be padded. Each sequence can be a numpy array, a list of float
                values, a list of numpy arrays or a list of list of float values. Must be mono channel audio, not
                stereo, i.e. single float per timestep.
            return_tensors (`str` or [`~utils.TensorType`], *optional*):
                If set, will return tensors instead of list of python integers. Acceptable values are:
                - `'pt'`: Return PyTorch `torch.Tensor` objects.
                - `'np'`: Return Numpy `np.ndarray` objects.
            return_attention_mask (`bool`, *optional*, default to `True`):
                Whether to return the attention mask. If left to the default, will return the attention mask according
                to the specific feature_extractor's default. [What are attention masks?](../glossary#attention-mask)

                <Tip>

                For TvltTransformer models, `attention_mask` should alwys be passed for batched inference, to avoid
                subtle bugs.

                </Tip>

            sampling_rate (`int`, *optional*):
                The sampling rate at which the `raw_speech` input was sampled. It is strongly recommended to pass
                `sampling_rate` at the forward call to prevent silent errors and allow automatic speech recognition
                pipeline. Current model supports sampling rate 16000 and 44100.
            resample (`bool`, *optional*, defaults to `False`):
                If the sampling rate is not matched, resample the input audio to match.
            mask_audio (`bool`, *optional*, defaults to `False`):
                Whether or not to mask input audio for MAE task.

        Returns:
            [`BatchFeature`]: A [`BatchFeature`] with the following fields:

            - **audio_values** -- Audio values to be fed to a model, of shape (batch_size, num_channels, height,
              width).

            - **audio_mask** -- Audio masks to be fed to a model, of shape (batch_size, num_audio_patches).
        """
        ...
    


