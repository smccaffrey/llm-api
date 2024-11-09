"""
This type stub file was generated by pyright.
"""

import numpy as np
from typing import Dict, List, Optional, Tuple, Union
from ...image_processing_utils import BaseImageProcessor
from ...image_utils import ChannelDimension, ImageInput, PILImageResampling
from ...utils import TensorType, is_torch_available, is_vision_available

"""Image processor class for SegGPT."""
if is_torch_available():
    ...
if is_vision_available():
    ...
logger = ...
def build_palette(num_labels: int) -> List[Tuple[int, int]]:
    ...

def mask_to_rgb(mask: np.ndarray, palette: Optional[List[Tuple[int, int]]] = ..., data_format: Optional[ChannelDimension] = ...) -> np.ndarray:
    ...

class SegGptImageProcessor(BaseImageProcessor):
    r"""
    Constructs a SegGpt image processor.

    Args:
        do_resize (`bool`, *optional*, defaults to `True`):
            Whether to resize the image's (height, width) dimensions to the specified `(size["height"],
            size["width"])`. Can be overridden by the `do_resize` parameter in the `preprocess` method.
        size (`dict`, *optional*, defaults to `{"height": 448, "width": 448}`):
            Size of the output image after resizing. Can be overridden by the `size` parameter in the `preprocess`
            method.
        resample (`PILImageResampling`, *optional*, defaults to `Resampling.BICUBIC`):
            Resampling filter to use if resizing the image. Can be overridden by the `resample` parameter in the
            `preprocess` method.
        do_rescale (`bool`, *optional*, defaults to `True`):
            Whether to rescale the image by the specified scale `rescale_factor`. Can be overridden by the `do_rescale`
            parameter in the `preprocess` method.
        rescale_factor (`int` or `float`, *optional*, defaults to `1/255`):
            Scale factor to use if rescaling the image. Can be overridden by the `rescale_factor` parameter in the
            `preprocess` method.
        do_normalize (`bool`, *optional*, defaults to `True`):
            Whether to normalize the image. Can be overridden by the `do_normalize` parameter in the `preprocess`
            method.
        image_mean (`float` or `List[float]`, *optional*, defaults to `IMAGENET_DEFAULT_MEAN`):
            Mean to use if normalizing the image. This is a float or list of floats the length of the number of
            channels in the image. Can be overridden by the `image_mean` parameter in the `preprocess` method.
        image_std (`float` or `List[float]`, *optional*, defaults to `IMAGENET_DEFAULT_STD`):
            Standard deviation to use if normalizing the image. This is a float or list of floats the length of the
            number of channels in the image. Can be overridden by the `image_std` parameter in the `preprocess` method.
        do_convert_rgb (`bool`, *optional*, defaults to `True`):
            Whether to convert the prompt mask to RGB format. Can be overridden by the `do_convert_rgb` parameter in the
            `preprocess` method.
    """
    model_input_names = ...
    def __init__(self, do_resize: bool = ..., size: Optional[Dict[str, int]] = ..., resample: PILImageResampling = ..., do_rescale: bool = ..., rescale_factor: Union[int, float] = ..., do_normalize: bool = ..., image_mean: Optional[Union[float, List[float]]] = ..., image_std: Optional[Union[float, List[float]]] = ..., do_convert_rgb: bool = ..., **kwargs) -> None:
        ...
    
    def get_palette(self, num_labels: int) -> List[Tuple[int, int]]:
        """Build a palette to map the prompt mask from a single channel to a 3 channel RGB.

        Args:
            num_labels (`int`):
                Number of classes in the segmentation task (excluding the background).

        Returns:
            `List[Tuple[int, int]]`: Palette to map the prompt mask from a single channel to a 3 channel RGB.
        """
        ...
    
    def mask_to_rgb(self, image: np.ndarray, palette: Optional[List[Tuple[int, int]]] = ..., data_format: Optional[Union[str, ChannelDimension]] = ...) -> np.ndarray:
        """Converts a segmentation map to RGB format.

        Args:
            image (`np.ndarray`):
                Segmentation map with dimensions (height, width) where pixel values represent the class index.
            palette (`List[Tuple[int, int]]`, *optional*, defaults to `None`):
                Palette to use to convert the mask to RGB format. If unset, the mask is duplicated across the channel
                dimension.
            data_format (`ChannelDimension` or `str`, *optional*):
                The channel dimension format for the output image. If unset, the channel dimension format of the input
                image is used. Can be one of:
                - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.

        Returns:
            `np.ndarray`: The mask in RGB format.
        """
        ...
    
    def resize(self, image: np.ndarray, size: Dict[str, int], resample: PILImageResampling = ..., data_format: Optional[Union[str, ChannelDimension]] = ..., input_data_format: Optional[Union[str, ChannelDimension]] = ..., **kwargs) -> np.ndarray:
        """
        Resize an image to `(size["height"], size["width"])`.

        Args:
            image (`np.ndarray`):
                Image to resize.
            size (`Dict[str, int]`):
                Dictionary in the format `{"height": int, "width": int}` specifying the size of the output image.
            resample (`PILImageResampling`, *optional*, defaults to `PILImageResampling.BICUBIC`):
                `PILImageResampling` filter to use when resizing the image e.g. `PILImageResampling.BICUBIC`.
            data_format (`ChannelDimension` or `str`, *optional*):
                The channel dimension format for the output image. If unset, the channel dimension format of the input
                image is used. Can be one of:
                - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
                - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.
            input_data_format (`ChannelDimension` or `str`, *optional*):
                The channel dimension format for the input image. If unset, the channel dimension format is inferred
                from the input image. Can be one of:
                - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
                - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.

        Returns:
            `np.ndarray`: The resized image.
        """
        ...
    
    def preprocess(self, images: Optional[ImageInput] = ..., prompt_images: Optional[ImageInput] = ..., prompt_masks: Optional[ImageInput] = ..., do_resize: Optional[bool] = ..., size: Dict[str, int] = ..., resample: PILImageResampling = ..., do_rescale: Optional[bool] = ..., rescale_factor: Optional[float] = ..., do_normalize: Optional[bool] = ..., image_mean: Optional[Union[float, List[float]]] = ..., image_std: Optional[Union[float, List[float]]] = ..., do_convert_rgb: Optional[bool] = ..., num_labels: Optional[int] = ..., return_tensors: Optional[Union[str, TensorType]] = ..., data_format: Union[str, ChannelDimension] = ..., input_data_format: Optional[Union[str, ChannelDimension]] = ..., **kwargs): # -> BatchFeature:
        """
        Preprocess an image or batch of images.

        Args:
            images (`ImageInput`):
                Image to _preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If
                passing in images with pixel values between 0 and 1, set `do_rescale=False`.
            prompt_images (`ImageInput`):
                Prompt image to _preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If
                passing in images with pixel values between 0 and 1, set `do_rescale=False`.
            prompt_masks (`ImageInput`):
                Prompt mask from prompt image to _preprocess that specify prompt_masks value in the preprocessed output.
                Can either be in the format of segmentation maps (no channels) or RGB images. If in the format of
                RGB images, `do_convert_rgb` should be set to `False`. If in the format of segmentation maps, `num_labels`
                specifying `num_labels` is recommended to build a palette to map the prompt mask from a single channel to
                a 3 channel RGB. If `num_labels` is not specified, the prompt mask will be duplicated across the channel
                dimension.
            do_resize (`bool`, *optional*, defaults to `self.do_resize`):
                Whether to resize the image.
            size (`Dict[str, int]`, *optional*, defaults to `self.size`):
                Dictionary in the format `{"height": h, "width": w}` specifying the size of the output image after
                resizing.
            resample (`PILImageResampling` filter, *optional*, defaults to `self.resample`):
                `PILImageResampling` filter to use if resizing the image e.g. `PILImageResampling.BICUBIC`. Only has
                an effect if `do_resize` is set to `True`. Doesn't apply to prompt mask as it is resized using nearest.
            do_rescale (`bool`, *optional*, defaults to `self.do_rescale`):
                Whether to rescale the image values between [0 - 1].
            rescale_factor (`float`, *optional*, defaults to `self.rescale_factor`):
                Rescale factor to rescale the image by if `do_rescale` is set to `True`.
            do_normalize (`bool`, *optional*, defaults to `self.do_normalize`):
                Whether to normalize the image.
            image_mean (`float` or `List[float]`, *optional*, defaults to `self.image_mean`):
                Image mean to use if `do_normalize` is set to `True`.
            image_std (`float` or `List[float]`, *optional*, defaults to `self.image_std`):
                Image standard deviation to use if `do_normalize` is set to `True`.
            do_convert_rgb (`bool`, *optional*, defaults to `self.do_convert_rgb`):
                Whether to convert the prompt mask to RGB format. If `num_labels` is specified, a palette will be built
                to map the prompt mask from a single channel to a 3 channel RGB. If unset, the prompt mask is duplicated
                across the channel dimension. Must be set to `False` if the prompt mask is already in RGB format.
            num_labels: (`int`, *optional*):
                Number of classes in the segmentation task (excluding the background). If specified, a palette will be
                built, assuming that class_idx 0 is the background, to map the prompt mask from a plain segmentation map
                with no channels to a 3 channel RGB. Not specifying this will result in the prompt mask either being passed
                through as is if it is already in RGB format (if `do_convert_rgb` is false) or being duplicated
                across the channel dimension.
            return_tensors (`str` or `TensorType`, *optional*):
                The type of tensors to return. Can be one of:
                - Unset: Return a list of `np.ndarray`.
                - `TensorType.TENSORFLOW` or `'tf'`: Return a batch of type `tf.Tensor`.
                - `TensorType.PYTORCH` or `'pt'`: Return a batch of type `torch.Tensor`.
                - `TensorType.NUMPY` or `'np'`: Return a batch of type `np.ndarray`.
                - `TensorType.JAX` or `'jax'`: Return a batch of type `jax.numpy.ndarray`.
            data_format (`ChannelDimension` or `str`, *optional*, defaults to `ChannelDimension.FIRST`):
                The channel dimension format for the output image. Can be one of:
                - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
                - Unset: Use the channel dimension format of the input image.
            input_data_format (`ChannelDimension` or `str`, *optional*):
                The channel dimension format for the input image. If unset, the channel dimension format is inferred
                from the input image. Can be one of:
                - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
                - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.
        """
        ...
    
    def post_process_semantic_segmentation(self, outputs, target_sizes: Optional[List[Tuple[int, int]]] = ..., num_labels: Optional[int] = ...): # -> list[Any]:
        """
        Converts the output of [`SegGptImageSegmentationOutput`] into segmentation maps. Only supports
        PyTorch.

        Args:
            outputs ([`SegGptImageSegmentationOutput`]):
                Raw outputs of the model.
            target_sizes (`List[Tuple[int, int]]`, *optional*):
                List of length (batch_size), where each list item (`Tuple[int, int]`) corresponds to the requested
                final size (height, width) of each prediction. If left to None, predictions will not be resized.
            num_labels (`int`, *optional*):
                Number of classes in the segmentation task (excluding the background). If specified, a palette will be
                built, assuming that class_idx 0 is the background, to map prediction masks from RGB values to class
                indices. This value should be the same used when preprocessing inputs.
        Returns:
            semantic_segmentation: `List[torch.Tensor]` of length `batch_size`, where each item is a semantic
            segmentation map of shape (height, width) corresponding to the target_sizes entry (if `target_sizes` is
            specified). Each entry of each `torch.Tensor` correspond to a semantic class id.
        """
        ...
    

