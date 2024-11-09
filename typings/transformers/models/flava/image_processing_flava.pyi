"""
This type stub file was generated by pyright.
"""

import numpy as np
import PIL
from functools import lru_cache
from typing import Any, Dict, Iterable, List, Optional, Tuple, Union
from ...image_processing_utils import BaseImageProcessor
from ...image_utils import ChannelDimension, ImageInput, PILImageResampling
from ...utils import TensorType, filter_out_non_signature_kwargs, is_vision_available

"""Image processor class for Flava."""
if is_vision_available():
    ...
logger = ...
FLAVA_IMAGE_MEAN = ...
FLAVA_IMAGE_STD = ...
FLAVA_CODEBOOK_MEAN = ...
FLAVA_CODEBOOK_STD = ...
LOGIT_LAPLACE_EPS: float = ...
class FlavaMaskingGenerator:
    def __init__(self, input_size: Union[int, Tuple[int, int]] = ..., total_mask_patches: int = ..., mask_group_max_patches: Optional[int] = ..., mask_group_min_patches: int = ..., mask_group_min_aspect_ratio: Optional[float] = ..., mask_group_max_aspect_ratio: float = ...) -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def get_shape(self): # -> tuple[Any | int, Any | int]:
        ...
    
    def __call__(self): # -> NDArray[Any]:
        ...
    


class FlavaImageProcessor(BaseImageProcessor):
    r"""
    Constructs a Flava image processor.

    Args:
        do_resize (`bool`, *optional*, defaults to `True`):
            Whether to resize the image's (height, width) dimensions to the specified `size`. Can be overridden by the
            `do_resize` parameter in `preprocess`.
        size (`Dict[str, int]` *optional*, defaults to `{"height": 224, "width": 224}`):
            Size of the image after resizing. Can be overridden by the `size` parameter in `preprocess`.
        resample (`PILImageResampling`, *optional*, defaults to `PILImageResampling.BICUBIC`):
            Resampling filter to use if resizing the image. Can be overridden by the `resample` parameter in
            `preprocess`.
        do_center_crop (`bool`, *optional*, defaults to `True`):
            Whether to center crop the images. Can be overridden by the `do_center_crop` parameter in `preprocess`.
        crop_size (`Dict[str, int]` *optional*, defaults to `{"height": 224, "width": 224}`):
            Size of image after the center crop `(crop_size["height"], crop_size["width"])`. Can be overridden by the
            `crop_size` parameter in `preprocess`.
        do_rescale (`bool`, *optional*, defaults to `True`):
            Whether to rescale the image by the specified scale `rescale_factor`. Can be overridden by the `do_rescale`
            parameter in `preprocess`.
        rescale_factor (`int` or `float`, *optional*, defaults to `1/255`):
            Scale factor to use if rescaling the image. Can be overridden by the `rescale_factor` parameter in
            `preprocess`.
        do_normalize (`bool`, *optional*, defaults to `True`):
            Whether to normalize the image. Can be overridden by the `do_normalize` parameter in `preprocess`.
        image_mean (`float` or `List[float]`, *optional*, defaults to `IMAGENET_STANDARD_MEAN`):
            Mean to use if normalizing the image. This is a float or list of floats the length of the number of
            channels in the image. Can be overridden by the `image_mean` parameter in the `preprocess` method.
        image_std (`float` or `List[float]`, *optional*, defaults to `IMAGENET_STANDARD_STD`):
            Standard deviation to use if normalizing the image. This is a float or list of floats the length of the
            number of channels in the image. Can be overridden by the `image_std` parameter in the `preprocess` method.
        return_image_mask (`bool`, *optional*, defaults to `False`):
            Whether to return the image mask. Can be overridden by the `return_image_mask` parameter in `preprocess`.
        input_size_patches (`int`, *optional*, defaults to 14):
            Number of patches in the image in height and width direction. 14x14 = 196 total patches. Can be overridden
            by the `input_size_patches` parameter in `preprocess`.
        total_mask_patches (`int`, *optional*, defaults to 75):
            Total number of patches that should be masked. Can be overridden by the `total_mask_patches` parameter in
            `preprocess`.
        mask_group_min_patches (`int`, *optional*, defaults to 16):
            Minimum number of patches that should be masked. Can be overridden by the `mask_group_min_patches`
            parameter in `preprocess`.
        mask_group_max_patches (`int`, *optional*):
            Maximum number of patches that should be masked. Can be overridden by the `mask_group_max_patches`
            parameter in `preprocess`.
        mask_group_min_aspect_ratio (`float`, *optional*, defaults to 0.3):
            Minimum aspect ratio of the mask window. Can be overridden by the `mask_group_min_aspect_ratio` parameter
            in `preprocess`.
        mask_group_max_aspect_ratio (`float`, *optional*):
            Maximum aspect ratio of the mask window. Can be overridden by the `mask_group_max_aspect_ratio` parameter
            in `preprocess`.
        codebook_do_resize (`bool`, *optional*, defaults to `True`):
            Whether to resize the input for codebook to a certain. Can be overridden by the `codebook_do_resize`
            parameter in `preprocess`. `codebook_size`.
        codebook_size (`Dict[str, int]`, *optional*, defaults to `{"height": 224, "width": 224}`):
            Resize the input for codebook to the given size. Can be overridden by the `codebook_size` parameter in
            `preprocess`.
        codebook_resample (`PILImageResampling`, *optional*, defaults to `PILImageResampling.LANCZOS`):
            Resampling filter to use if resizing the codebook image. Can be overridden by the `codebook_resample`
            parameter in `preprocess`.
        codebook_do_center_crop (`bool`, *optional*, defaults to `True`):
            Whether to crop the input for codebook at the center. If the input size is smaller than
            `codebook_crop_size` along any edge, the image is padded with 0's and then center cropped. Can be
            overridden by the `codebook_do_center_crop` parameter in `preprocess`.
        codebook_crop_size (`Dict[str, int]`, *optional*, defaults to `{"height": 224, "width": 224}`):
            Desired output size for codebook input when applying center-cropping. Can be overridden by the
            `codebook_crop_size` parameter in `preprocess`.
        codebook_do_rescale (`bool`, *optional*, defaults to `True`):
            Whether to rescale the input for codebook by the specified scale `codebook_rescale_factor`. Can be
            overridden by the `codebook_do_rescale` parameter in `preprocess`.
        codebook_rescale_factor (`int` or `float`, *optional*, defaults to `1/255`):
            Defines the scale factor to use if rescaling the codebook image. Can be overridden by the
            `codebook_rescale_factor` parameter in `preprocess`.
        codebook_do_map_pixels (`bool`, *optional*, defaults to `True`):
            Whether to map the pixel values of the codebook input to (1 - 2e)x + e. Can be overridden by the
            `codebook_do_map_pixels` parameter in `preprocess`.
        codebook_do_normalize (`bool`, *optional*, defaults to `True`):
            Whether or not to normalize the input for codebook with `codebook_image_mean` and `codebook_image_std`. Can
            be overridden by the `codebook_do_normalize` parameter in `preprocess`.
        codebook_image_mean (`Optional[Union[float, Iterable[float]]]`, *optional*, defaults to `[0, 0, 0]`):
            The sequence of means for each channel, to be used when normalizing images for codebook. Can be overridden
            by the `codebook_image_mean` parameter in `preprocess`.
        codebook_image_std (`Optional[Union[float, Iterable[float]]]`, *optional*, defaults to `[0.5, 0.5, 0.5]`):
            The sequence of standard deviations for each channel, to be used when normalizing images for codebook. Can
            be overridden by the `codebook_image_std` parameter in `preprocess`.
    """
    model_input_names = ...
    def __init__(self, do_resize: bool = ..., size: Dict[str, int] = ..., resample: PILImageResampling = ..., do_center_crop: bool = ..., crop_size: Dict[str, int] = ..., do_rescale: bool = ..., rescale_factor: Union[int, float] = ..., do_normalize: bool = ..., image_mean: Optional[Union[float, Iterable[float]]] = ..., image_std: Optional[Union[float, Iterable[float]]] = ..., return_image_mask: bool = ..., input_size_patches: int = ..., total_mask_patches: int = ..., mask_group_min_patches: int = ..., mask_group_max_patches: Optional[int] = ..., mask_group_min_aspect_ratio: float = ..., mask_group_max_aspect_ratio: Optional[float] = ..., return_codebook_pixels: bool = ..., codebook_do_resize: bool = ..., codebook_size: bool = ..., codebook_resample: int = ..., codebook_do_center_crop: bool = ..., codebook_crop_size: int = ..., codebook_do_rescale: bool = ..., codebook_rescale_factor: Union[int, float] = ..., codebook_do_map_pixels: bool = ..., codebook_do_normalize: bool = ..., codebook_image_mean: Optional[Union[float, Iterable[float]]] = ..., codebook_image_std: Optional[Union[float, Iterable[float]]] = ..., **kwargs) -> None:
        ...
    
    @classmethod
    def from_dict(cls, image_processor_dict: Dict[str, Any], **kwargs): # -> tuple[Self, dict[str, Any]] | Self:
        """
        Overrides the `from_dict` method from the base class to make sure parameters are updated if image processor is
        created using from_dict and kwargs e.g. `FlavaImageProcessor.from_pretrained(checkpoint, codebook_size=600)`
        """
        ...
    
    @lru_cache()
    def masking_generator(self, input_size_patches, total_mask_patches, mask_group_min_patches, mask_group_max_patches, mask_group_min_aspect_ratio, mask_group_max_aspect_ratio) -> FlavaMaskingGenerator:
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
    
    def map_pixels(self, image: np.ndarray) -> np.ndarray:
        ...
    
    @filter_out_non_signature_kwargs()
    def preprocess(self, images: ImageInput, do_resize: Optional[bool] = ..., size: Dict[str, int] = ..., resample: PILImageResampling = ..., do_center_crop: Optional[bool] = ..., crop_size: Optional[Dict[str, int]] = ..., do_rescale: Optional[bool] = ..., rescale_factor: Optional[float] = ..., do_normalize: Optional[bool] = ..., image_mean: Optional[Union[float, List[float]]] = ..., image_std: Optional[Union[float, List[float]]] = ..., return_image_mask: Optional[bool] = ..., input_size_patches: Optional[int] = ..., total_mask_patches: Optional[int] = ..., mask_group_min_patches: Optional[int] = ..., mask_group_max_patches: Optional[int] = ..., mask_group_min_aspect_ratio: Optional[float] = ..., mask_group_max_aspect_ratio: Optional[float] = ..., return_codebook_pixels: Optional[bool] = ..., codebook_do_resize: Optional[bool] = ..., codebook_size: Optional[Dict[str, int]] = ..., codebook_resample: Optional[int] = ..., codebook_do_center_crop: Optional[bool] = ..., codebook_crop_size: Optional[Dict[str, int]] = ..., codebook_do_rescale: Optional[bool] = ..., codebook_rescale_factor: Optional[float] = ..., codebook_do_map_pixels: Optional[bool] = ..., codebook_do_normalize: Optional[bool] = ..., codebook_image_mean: Optional[Iterable[float]] = ..., codebook_image_std: Optional[Iterable[float]] = ..., return_tensors: Optional[Union[str, TensorType]] = ..., data_format: ChannelDimension = ..., input_data_format: Optional[Union[str, ChannelDimension]] = ...) -> PIL.Image.Image:
        """
        Preprocess an image or batch of images.

        Args:
            images (`ImageInput`):
                Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If
                passing in images with pixel values between 0 and 1, set `do_rescale=False`.
            do_resize (`bool`, *optional*, defaults to `self.do_resize`):
                Whether to resize the image.
            size (`Dict[str, int]`, *optional*, defaults to `self.size`):
                Size of the image.
            resample (`int`, *optional*, defaults to `self.resample`):
                Resampling filter to use if resizing the image. This can be one of the enum `PILImageResampling`, Only
                has an effect if `do_resize` is set to `True`.
            do_center_crop (`bool`, *optional*, defaults to `self.do_center_crop`):
                Whether to center crop the image.
            crop_size (`Dict[str, int]`, *optional*, defaults to `self.crop_size`):
                Size of the center crop. Only has an effect if `do_center_crop` is set to `True`.
            do_rescale (`bool`, *optional*, defaults to `self.do_rescale`):
                Whether to rescale the image values between [0 - 1].
            rescale_factor (`float`, *optional*, defaults to `self.rescale_factor`):
                Rescale factor to rescale the image by if `do_rescale` is set to `True`.
            do_normalize (`bool`, *optional*, defaults to `self.do_normalize`):
                Whether to normalize the image.
            image_mean (`float` or `List[float]`, *optional*, defaults to `self.image_mean`):
                Image mean.
            image_std (`float` or `List[float]`, *optional*, defaults to `self.image_std`):
                Image standard deviation.
            return_image_mask (`bool`, *optional*, defaults to `self.return_image_mask`):
                Whether to return the image mask.
            input_size_patches (`int`, *optional*, defaults to `self.input_size_patches`):
                Size of the patches to extract from the image.
            total_mask_patches (`int`, *optional*, defaults to `self.total_mask_patches`):
                Total number of patches to extract from the image.
            mask_group_min_patches (`int`, *optional*, defaults to `self.mask_group_min_patches`):
                Minimum number of patches to extract from the image.
            mask_group_max_patches (`int`, *optional*, defaults to `self.mask_group_max_patches`):
                Maximum number of patches to extract from the image.
            mask_group_min_aspect_ratio (`float`, *optional*, defaults to `self.mask_group_min_aspect_ratio`):
                Minimum aspect ratio of the patches to extract from the image.
            mask_group_max_aspect_ratio (`float`, *optional*, defaults to `self.mask_group_max_aspect_ratio`):
                Maximum aspect ratio of the patches to extract from the image.
            return_codebook_pixels (`bool`, *optional*, defaults to `self.return_codebook_pixels`):
                Whether to return the codebook pixels.
            codebook_do_resize (`bool`, *optional*, defaults to `self.codebook_do_resize`):
                Whether to resize the codebook pixels.
            codebook_size (`Dict[str, int]`, *optional*, defaults to `self.codebook_size`):
                Size of the codebook pixels.
            codebook_resample (`int`, *optional*, defaults to `self.codebook_resample`):
                Resampling filter to use if resizing the codebook pixels. This can be one of the enum
                `PILImageResampling`, Only has an effect if `codebook_do_resize` is set to `True`.
            codebook_do_center_crop (`bool`, *optional*, defaults to `self.codebook_do_center_crop`):
                Whether to center crop the codebook pixels.
            codebook_crop_size (`Dict[str, int]`, *optional*, defaults to `self.codebook_crop_size`):
                Size of the center crop of the codebook pixels. Only has an effect if `codebook_do_center_crop` is set
                to `True`.
            codebook_do_rescale (`bool`, *optional*, defaults to `self.codebook_do_rescale`):
                Whether to rescale the codebook pixels values between [0 - 1].
            codebook_rescale_factor (`float`, *optional*, defaults to `self.codebook_rescale_factor`):
                Rescale factor to rescale the codebook pixels by if `codebook_do_rescale` is set to `True`.
            codebook_do_map_pixels (`bool`, *optional*, defaults to `self.codebook_do_map_pixels`):
                Whether to map the codebook pixels values.
            codebook_do_normalize (`bool`, *optional*, defaults to `self.codebook_do_normalize`):
                Whether to normalize the codebook pixels.
            codebook_image_mean (`float` or `List[float]`, *optional*, defaults to `self.codebook_image_mean`):
                Codebook pixels mean to normalize the codebook pixels by if `codebook_do_normalize` is set to `True`.
            codebook_image_std (`float` or `List[float]`, *optional*, defaults to `self.codebook_image_std`):
                Codebook pixels standard deviation to normalize the codebook pixels by if `codebook_do_normalize` is
                set to `True`.
            return_tensors (`str` or `TensorType`, *optional*):
                The type of tensors to return. Can be one of:
                    - Unset: Return a list of `np.ndarray`.
                    - `TensorType.TENSORFLOW` or `'tf'`: Return a batch of type `tf.Tensor`.
                    - `TensorType.PYTORCH` or `'pt'`: Return a batch of type `torch.Tensor`.
                    - `TensorType.NUMPY` or `'np'`: Return a batch of type `np.ndarray`.
                    - `TensorType.JAX` or `'jax'`: Return a batch of type `jax.numpy.ndarray`.
            data_format (`ChannelDimension` or `str`, *optional*, defaults to `ChannelDimension.FIRST`):
                The channel dimension format for the output image. Can be one of:
                    - `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                    - `ChannelDimension.LAST`: image in (height, width, num_channels) format.
            input_data_format (`ChannelDimension` or `str`, *optional*):
                The channel dimension format for the input image. If unset, the channel dimension format is inferred
                from the input image. Can be one of:
                - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
                - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.
        """
        ...
    


