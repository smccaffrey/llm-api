"""
This type stub file was generated by pyright.
"""

import numpy as np
from typing import Dict, List, Optional, Tuple, Union
from ...image_processing_utils import BaseImageProcessor, BatchFeature
from ...image_utils import ChannelDimension, ImageInput, PILImageResampling
from ...utils import TensorType, filter_out_non_signature_kwargs, is_torch_available

"""Image processor class for OwlViT"""
if is_torch_available():
    ...
logger = ...
def box_area(boxes):
    """
    Computes the area of a set of bounding boxes, which are specified by its (x1, y1, x2, y2) coordinates.

    Args:
        boxes (`torch.FloatTensor` of shape `(number_of_boxes, 4)`):
            Boxes for which the area will be computed. They are expected to be in (x1, y1, x2, y2) format with `0 <= x1
            < x2` and `0 <= y1 < y2`.
    Returns:
        `torch.FloatTensor`: a tensor containing the area for each box.
    """
    ...

def box_iou(boxes1, boxes2): # -> tuple[Any, Any]:
    ...

class OwlViTImageProcessor(BaseImageProcessor):
    r"""
    Constructs an OWL-ViT image processor.

    This image processor inherits from [`ImageProcessingMixin`] which contains most of the main methods. Users should
    refer to this superclass for more information regarding those methods.

    Args:
        do_resize (`bool`, *optional*, defaults to `True`):
            Whether to resize the shorter edge of the input to a certain `size`.
        size (`Dict[str, int]`, *optional*, defaults to {"height": 768, "width": 768}):
            The size to use for resizing the image. Only has an effect if `do_resize` is set to `True`. If `size` is a
            sequence like (h, w), output size will be matched to this. If `size` is an int, then image will be resized
            to (size, size).
        resample (`int`, *optional*, defaults to `Resampling.BICUBIC`):
            An optional resampling filter. This can be one of `PIL.Image.Resampling.NEAREST`,
            `PIL.Image.Resampling.BOX`, `PIL.Image.Resampling.BILINEAR`, `PIL.Image.Resampling.HAMMING`,
            `PIL.Image.Resampling.BICUBIC` or `PIL.Image.Resampling.LANCZOS`. Only has an effect if `do_resize` is set
            to `True`.
        do_center_crop (`bool`, *optional*, defaults to `False`):
            Whether to crop the input at the center. If the input size is smaller than `crop_size` along any edge, the
            image is padded with 0's and then center cropped.
        crop_size (`int`, *optional*, defaults to {"height": 768, "width": 768}):
            The size to use for center cropping the image. Only has an effect if `do_center_crop` is set to `True`.
        do_rescale (`bool`, *optional*, defaults to `True`):
            Whether to rescale the input by a certain factor.
        rescale_factor (`float`, *optional*, defaults to `1/255`):
            The factor to use for rescaling the image. Only has an effect if `do_rescale` is set to `True`.
        do_normalize (`bool`, *optional*, defaults to `True`):
            Whether or not to normalize the input with `image_mean` and `image_std`. Desired output size when applying
            center-cropping. Only has an effect if `do_center_crop` is set to `True`.
        image_mean (`List[int]`, *optional*, defaults to `[0.48145466, 0.4578275, 0.40821073]`):
            The sequence of means for each channel, to be used when normalizing images.
        image_std (`List[int]`, *optional*, defaults to `[0.26862954, 0.26130258, 0.27577711]`):
            The sequence of standard deviations for each channel, to be used when normalizing images.
    """
    model_input_names = ...
    def __init__(self, do_resize=..., size=..., resample=..., do_center_crop=..., crop_size=..., do_rescale=..., rescale_factor=..., do_normalize=..., image_mean=..., image_std=..., **kwargs) -> None:
        ...
    
    def resize(self, image: np.ndarray, size: Dict[str, int], resample: PILImageResampling.BICUBIC, data_format: Optional[Union[str, ChannelDimension]] = ..., input_data_format: Optional[Union[str, ChannelDimension]] = ..., **kwargs) -> np.ndarray:
        """
        Resize an image to a certain size.

        Args:
            image (`np.ndarray`):
                Image to resize.
            size (`Dict[str, int]`):
                The size to resize the image to. Must contain height and width keys.
            resample (`PILImageResampling`, *optional*, defaults to `PILImageResampling.BICUBIC`):
                The resampling filter to use when resizing the input.
            data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format for the output image. If unset, the channel dimension format of the input
                image is used.
            input_data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format of the input image. If not provided, it will be inferred.
        """
        ...
    
    def center_crop(self, image: np.ndarray, crop_size: Dict[str, int], data_format: Optional[Union[str, ChannelDimension]] = ..., input_data_format: Optional[Union[str, ChannelDimension]] = ..., **kwargs) -> np.ndarray:
        """
        Center crop an image to a certain size.

        Args:
            image (`np.ndarray`):
                Image to center crop.
            crop_size (`Dict[str, int]`):
                The size to center crop the image to. Must contain height and width keys.
            data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format for the output image. If unset, the channel dimension format of the input
                image is used.
            input_data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format of the input image. If not provided, it will be inferred.
        """
        ...
    
    def rescale(self, image: np.ndarray, rescale_factor: float, data_format: Optional[Union[str, ChannelDimension]] = ..., input_data_format: Optional[Union[str, ChannelDimension]] = ...) -> np.ndarray:
        """
        Rescale the image by the given factor. image = image * rescale_factor.

        Args:
            image (`np.ndarray`):
                Image to rescale.
            rescale_factor (`float`):
                The value to use for rescaling.
            data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format for the output image. If unset, the channel dimension format of the input
                image is used. Can be one of:
                - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
            input_data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format for the input image. If unset, is inferred from the input image. Can be
                one of:
                - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
        """
        ...
    
    @filter_out_non_signature_kwargs()
    def preprocess(self, images: ImageInput, do_resize: Optional[bool] = ..., size: Optional[Dict[str, int]] = ..., resample: PILImageResampling = ..., do_center_crop: Optional[bool] = ..., crop_size: Optional[Dict[str, int]] = ..., do_rescale: Optional[bool] = ..., rescale_factor: Optional[float] = ..., do_normalize: Optional[bool] = ..., image_mean: Optional[Union[float, List[float]]] = ..., image_std: Optional[Union[float, List[float]]] = ..., return_tensors: Optional[Union[TensorType, str]] = ..., data_format: Union[str, ChannelDimension] = ..., input_data_format: Optional[Union[str, ChannelDimension]] = ...) -> BatchFeature:
        """
        Prepares an image or batch of images for the model.

        Args:
            images (`ImageInput`):
                The image or batch of images to be prepared. Expects a single or batch of images with pixel values
                ranging from 0 to 255. If passing in images with pixel values between 0 and 1, set `do_rescale=False`.
            do_resize (`bool`, *optional*, defaults to `self.do_resize`):
                Whether or not to resize the input. If `True`, will resize the input to the size specified by `size`.
            size (`Dict[str, int]`, *optional*, defaults to `self.size`):
                The size to resize the input to. Only has an effect if `do_resize` is set to `True`.
            resample (`PILImageResampling`, *optional*, defaults to `self.resample`):
                The resampling filter to use when resizing the input. Only has an effect if `do_resize` is set to
                `True`.
            do_center_crop (`bool`, *optional*, defaults to `self.do_center_crop`):
                Whether or not to center crop the input. If `True`, will center crop the input to the size specified by
                `crop_size`.
            crop_size (`Dict[str, int]`, *optional*, defaults to `self.crop_size`):
                The size to center crop the input to. Only has an effect if `do_center_crop` is set to `True`.
            do_rescale (`bool`, *optional*, defaults to `self.do_rescale`):
                Whether or not to rescale the input. If `True`, will rescale the input by dividing it by
                `rescale_factor`.
            rescale_factor (`float`, *optional*, defaults to `self.rescale_factor`):
                The factor to rescale the input by. Only has an effect if `do_rescale` is set to `True`.
            do_normalize (`bool`, *optional*, defaults to `self.do_normalize`):
                Whether or not to normalize the input. If `True`, will normalize the input by subtracting `image_mean`
                and dividing by `image_std`.
            image_mean (`Union[float, List[float]]`, *optional*, defaults to `self.image_mean`):
                The mean to subtract from the input when normalizing. Only has an effect if `do_normalize` is set to
                `True`.
            image_std (`Union[float, List[float]]`, *optional*, defaults to `self.image_std`):
                The standard deviation to divide the input by when normalizing. Only has an effect if `do_normalize` is
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
                - Unset: defaults to the channel dimension format of the input image.
            input_data_format (`ChannelDimension` or `str`, *optional*):
                The channel dimension format for the input image. If unset, the channel dimension format is inferred
                from the input image. Can be one of:
                - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
                - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.
        """
        ...
    
    def post_process(self, outputs, target_sizes): # -> list[dict[str, Any]]:
        """
        Converts the raw output of [`OwlViTForObjectDetection`] into final bounding boxes in (top_left_x, top_left_y,
        bottom_right_x, bottom_right_y) format.

        Args:
            outputs ([`OwlViTObjectDetectionOutput`]):
                Raw outputs of the model.
            target_sizes (`torch.Tensor` of shape `(batch_size, 2)`):
                Tensor containing the size (h, w) of each image of the batch. For evaluation, this must be the original
                image size (before any data augmentation). For visualization, this should be the image size after data
                augment, but before padding.
        Returns:
            `List[Dict]`: A list of dictionaries, each dictionary containing the scores, labels and boxes for an image
            in the batch as predicted by the model.
        """
        ...
    
    def post_process_object_detection(self, outputs, threshold: float = ..., target_sizes: Union[TensorType, List[Tuple]] = ...): # -> list[Any]:
        """
        Converts the raw output of [`OwlViTForObjectDetection`] into final bounding boxes in (top_left_x, top_left_y,
        bottom_right_x, bottom_right_y) format.

        Args:
            outputs ([`OwlViTObjectDetectionOutput`]):
                Raw outputs of the model.
            threshold (`float`, *optional*):
                Score threshold to keep object detection predictions.
            target_sizes (`torch.Tensor` or `List[Tuple[int, int]]`, *optional*):
                Tensor of shape `(batch_size, 2)` or list of tuples (`Tuple[int, int]`) containing the target size
                `(height, width)` of each image in the batch. If unset, predictions will not be resized.
        Returns:
            `List[Dict]`: A list of dictionaries, each dictionary containing the scores, labels and boxes for an image
            in the batch as predicted by the model.
        """
        ...
    
    def post_process_image_guided_detection(self, outputs, threshold=..., nms_threshold=..., target_sizes=...): # -> list[Any]:
        """
        Converts the output of [`OwlViTForObjectDetection.image_guided_detection`] into the format expected by the COCO
        api.

        Args:
            outputs ([`OwlViTImageGuidedObjectDetectionOutput`]):
                Raw outputs of the model.
            threshold (`float`, *optional*, defaults to 0.0):
                Minimum confidence threshold to use to filter out predicted boxes.
            nms_threshold (`float`, *optional*, defaults to 0.3):
                IoU threshold for non-maximum suppression of overlapping boxes.
            target_sizes (`torch.Tensor`, *optional*):
                Tensor of shape (batch_size, 2) where each entry is the (height, width) of the corresponding image in
                the batch. If set, predicted normalized bounding boxes are rescaled to the target sizes. If left to
                None, predictions will not be unnormalized.

        Returns:
            `List[Dict]`: A list of dictionaries, each dictionary containing the scores, labels and boxes for an image
            in the batch as predicted by the model. All labels are set to None as
            `OwlViTForObjectDetection.image_guided_detection` perform one-shot object detection.
        """
        ...
    

