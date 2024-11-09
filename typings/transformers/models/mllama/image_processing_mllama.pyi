"""
This type stub file was generated by pyright.
"""

import numpy as np
from functools import lru_cache
from typing import Dict, List, Optional, Tuple, Union
from ...image_processing_utils import BaseImageProcessor
from ...image_utils import ChannelDimension, ImageInput, PILImageResampling, is_vision_available
from ...utils import TensorType

if is_vision_available():
    ...
logger = ...
@lru_cache(maxsize=10)
def get_all_supported_aspect_ratios(max_image_tiles: int) -> List[Tuple[int, int]]:
    """
    Computes all allowed aspect ratios for a given maximum number of input tiles.

    This function calculates all possible arrangements of tiles that can be formed
    within the constraint of the maximum number of tiles. Each arrangement is
    represented by its aspect ratio (width/height) and the corresponding tile configuration.

    Args:
        max_image_tiles (`int`):
            The maximum number of tiles allowed.

    Returns:
        `List[Tuple[int, int]]`: A list of tuples, each tuple representing a valid (width, height)
        configuration in terms of number of tiles.

    Example:
        >>> get_all_supported_aspect_ratios(4)
        [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (3, 1), (4, 1)]

    """
    ...

def get_image_size_fit_to_canvas(image_height: int, image_width: int, canvas_height: int, canvas_width: int, tile_size: int) -> Tuple[int, int]:
    """
    Calculates the new size of an image to fit within a canvas while maintaining aspect ratio.

    This function calculates the optimal size for an image to fit within a canvas defined by
    canvas_height and canvas_width, while ensuring that the image dimensions are not smaller than
    tile_size. If the image is larger than the canvas, the returned size will fit within the canvas.
    If the image already fits within the canvas, the size remains unchanged.
    The aspect ratio of the original image is preserved.

    Args:
        image_height (`int`):
            The height of the original image.
        image_width (`int`):
            The width of the original image.
        canvas_height (`int`):
            The height of the canvas.
        canvas_width (`int`):
            The width of the canvas.
        tile_size (`int`):
            The tile size.

    Returns:
        `Tuple[int, int]`: A tuple containing the new height and width of the image.

    """
    ...

@lru_cache(maxsize=100)
def get_optimal_tiled_canvas(image_height: int, image_width: int, max_image_tiles: int, tile_size: int) -> Tuple[int, int]:
    r"""
    Determines the best canvas based on image and tile size and maximum number of tiles.

    First, calculates possible resolutions based on the maximum number of tiles and tile size.
    For example for max_image_tiles=2, tile_size=100, possible tile arrangements are:
    [(1, 1), (1, 2), (2, 1)] and corresponding canvas sizes are:
    [(100, 100), (100, 200), (200, 100)]

    For each possible resolution, calculates the scaling factors for
    width and height, and selects the smallest one, which is the limiting side.
    E.g. to match the canvas you can upscale height by 2x, and width by 1.5x,
    therefore, the maximum upscaling you can do is min(2, 1.5) = 1.5.

    If upscaling is possible (any of the scaling factors is greater than 1),
    then picks the smallest upscaling factor > 1.

    If upscaling is not possible, then picks the largest scaling factor <= 1, i.e.
    reduce downscaling as much as possible.

    If there are multiple resolutions with the same max scale, we pick the one with the lowest area,
    to minimize padding. E.g., the same image can be upscaled to 224x224 and 224x448, but the latter
    has more padding.

    Example of canvases made from tiles:

    To visualize how the image can fit onto different tile grids, let's try fitting an ASCII cat into the tiles.

    Here's an ASCII cat image you want to fit into the tiles:

       /\_/\
      ( o.o )
       > ^ <

    If `num_tiles=6`, possible tile grids would look like this:

    **2x3 Canvas (2 tiles wide, 3 tiles tall)**: -> total of 6 tiles
    +-------+-------+
    | /\_/\ |   0   |   <- Cat image split across two tiles horizontally
    +-------+-------+
    | > ^ < |   0   |   <- Remaining part of the cat occupies the left tile
    +-------+-------+
    |( o.o )|   0   |
    +-------+-------+

    **3x2 Canvas (3 tiles wide, 2 tiles tall)**: -> total of 6 tiles
    +-------+-------+-------+
    | /\_/\ |( o.o )|   0   |   <- Cat image occupies the first two tiles, 1 tile remains empty
    +-------+-------+-------+
    | > ^ < |   0   |   0   |   <- Remaining part of the cat occupies the left tile
    +-------+-------+-------+

    **1x6 Canvas (1 tile wide, 6 tiles tall)**: -> total of 6 tiles
    +-------+
    | /\_/\ |   <- Top part of the cat
    +-------+
    |( o.o )|   <- Middle part of the cat
    +-------+
    | > ^ < |   <- Bottom part of the cat
    +-------+
    |   0   |
    +-------+
    |   0   |
    +-------+
    |   0   |
    +-------+

    Given that the tiles you get depend on the chosen aspect ratio, you have to add
    embedding in the modeling code to help it know if it got a 3x2 or a 1x6 or a 2x3
    aspect ratio.

    The function tests these arrangements to find the smallest canvas where the image fits.
    If multiple canvases fit, it selects the one where the dimensions are closest to the image size.

    In this case the first canvas is the closest to the original image.

    You then feed all of the tiles to the model:

        +-------+-------+-------+-------+-------+-------+
    -   | /\_/\ |( o.o )| > ^ < |   0   |   0   |   0   |  <- Last canvas
        +-------+-------+-------+-------+-------+-------+

        +-------+-------+-------+-------+-------+-------+
    -   | /\_/\ | 0     |( o.o )|   0   | > ^ < |   0   | <- First canvas
        +-------+-------+-------+-------+-------+-------+

        +-------+-------+-------+-------+-------+-------+
    -   | /\_/\ |( o.o )|   0   | > ^ < |   0   |   0   | <- second canvas
        +-------+-------+-------+-------+-------+-------+

    For each tile, you have num_channels (usually RGB so 3), tile_width, tile_height

    Args:
        image_height (`int`):
            The height of the image.
        image_width (`int`):
            The width of the image.
        max_image_tiles (`int`):
            The maximum number of tiles any image can be split into.
        tile_size (`int`):
            The tile size.

    Returns:
        `Tuple[int, int]`: The best canvas resolution [height, width] for the given image.
    """
    ...

def split_to_tiles(image: np.ndarray, num_tiles_height: int, num_tiles_width: int) -> np.ndarray:
    """
    Split an image into a specified number of tiles along its width and height dimensions.

    Args:
        image (`np.ndarray`):
            Input image with shape (num_channels, height, width).
        num_tiles_height (`int`):
            Number of tiles to split the image into along its height.
        num_tiles_width (`int`):
            Number of tiles to split the image into along its width.

    Returns:
        `np.ndarray`:
            Array of image tiles with shape (num_tiles_width * num_tiles_height, num_channels, tile_height, tile_width).
    """
    ...

def build_aspect_ratio_mask(aspect_ratios: List[List[Tuple[int, int]]], max_image_tiles: int) -> np.ndarray:
    """
    Builds a mask for the aspect ratios of the images.

    Args:
        aspect_ratios (`List[List[Tuple[int, int]]]`):
            A list of lists containing aspect ratios for each image in the batch.
            Each aspect ratio is represented as a tuple of (width, height) in terms of number of tiles.
        max_image_tiles (`int`):
            The maximum number of tiles any image can be split into.

    Returns:
        `np.ndarray`: A 3D numpy array of shape (batch_size, max_num_images, max_image_tiles).
            The mask contains 1s for valid tiles and 0s for padding.
    """
    ...

def pack_images(batch_images: List[List[np.ndarray]], max_image_tiles: int) -> Tuple[np.ndarray, List[List[int]]]:
    """
    Stack a list of lists of images with variable lengths into a numpy array, applying zero padding as needed.
    Each list in the input represents a batch sample, and each image within a list is expected to be
    pre-split into tiles. The resulting array will have a shape of
    (batch_size, max_num_images, max_image_tiles, channels, tile_height, tile_width).

    Args:
        batch_images (`List[List[np.ndarray]]`):
            A list of lists of image tiles. Each inner list represents
            a batch sample containing multiple images, where each image is pre-split into tiles.
            The shape of each tile array is (num_tiles, channels, tile_height, tile_width).
        max_image_tiles (int):
            The maximum number of tiles any image was potantially split.

    Returns:
        `Tuple[np.ndarray, List[List[int]]]`: A tuple containing:
            - stacked_images (`np.ndarray`):
                A numpy array of stacked images with shape
                (batch_size, max_num_images, max_image_tiles, channels, tile_height, tile_width).
            - all_num_tiles (`List[List[int]]`):
                A list of lists containing the number of tiles
                for each image in each batch sample.
    """
    ...

def pack_aspect_ratios(aspect_ratios: List[List[Tuple[int, int]]], pad_value: int = ...) -> np.ndarray:
    """
    Stack a list of aspect ratios into a numpy array.

    Args:
        aspect_ratios (`List[List[Tuple[int, int]]]`):
            A list of aspect ratios.
        pad_value (`int`, *optional*, defaults to 1):
            The value to pad the aspect ratios with.

    Returns:
        `np.ndarray`:
            The aspect ratios stacked into a numpy array with shape (batch_size, max_num_images, 2).
    """
    ...

def convert_aspect_ratios_to_ids(aspect_ratios: List[List[Tuple[int, int]]], max_image_tiles: int) -> np.ndarray:
    """
    Convert aspect ratio tuples to unique ids.

    For batch padding we use 0, because there might be different number of images in each batch.
    The aspect ratio ids start from 1, with 1 corresponding to the first supported aspect ratio.

    Args:
        aspect_ratios (`List[List[Tuple[int, int]]]`):
            A list of aspect ratios for each image in the batch.
        max_image_tiles (`int`):
            The maximum number of tiles any image can be split into.

    Returns:
        `np.ndarray`:
            The aspect ratios ids as a numpy array with shape (batch_size, max_num_images).
            Each id corresponds to the index of the aspect ratio in the list of supported aspect ratios,
            offset by 1 (so 0 can be used for padding).
    """
    ...

def to_channel_dimension_format(image: np.ndarray, channel_dim: Union[ChannelDimension, str], input_channel_dim: Optional[Union[ChannelDimension, str]] = ...) -> np.ndarray:
    """
    Converts `image` to the channel dimension format specified by `channel_dim`.

    Args:
        image (`numpy.ndarray`):
            The image to have its channel dimension set.
        channel_dim (`ChannelDimension`):
            The channel dimension format to use.
        input_channel_dim (`ChannelDimension`, *optional*):
            The channel dimension format of the input image. If not provided, it will be inferred from the input image.

    Returns:
        `np.ndarray`:
            The image with the channel dimension set to `channel_dim`.
    """
    ...

def convert_to_rgb(image: ImageInput) -> ImageInput:
    """
    Converts an image to RGB format. Only converts if the image is of type PIL.Image.Image, otherwise returns the image
    as is.
    Args:
        image (Image):
            The image to convert.
    """
    ...

def make_list_of_images(images: ImageInput) -> List[List[Optional[np.ndarray]]]:
    """
    Convert a single image or a list of images to a list of numpy arrays.

    Args:
        images (`ImageInput`):
            A single image or a list of images.

    Returns:
        A list of numpy arrays.
    """
    ...

def is_valid_list_of_images(images: List): # -> List[Any] | bool:
    ...

class MllamaImageProcessor(BaseImageProcessor):
    """
    Constructs a Mllama image processor.

    Args:
        do_convert_rgb (`bool`, *optional*, defaults to `True`):
            Whether to convert the image to RGB. This is useful if the input image is of a different format e.g. RGBA.
            Only has an effect if the input image is in the PIL format.
        do_resize (`bool`, *optional*, defaults to `True`):
            Whether to resize the image.
        size (`Dict[str, int]`, *optional*, defaults to `self.size`):
            Size of the image tile. Should be a dictionary containing 'height' and 'width' keys, both with integer values.
            The height and width values should be equal.
        resample (`int`, *optional*, defaults to `Resampling.BILINEAR`):
            Resampling filter to use if resizing the image. This can be one of the enum `PILImageResampling`. Only
            has an effect if `do_resize` is set to `True`.
        do_rescale (`bool`, *optional*, defaults to `True`):
            Whether to rescale the image.
        rescale_factor (`float`, *optional*, defaults to 0.0):
            Rescale factor to rescale the image by if `do_rescale` is set to `True`.
        do_normalize (`bool`, *optional*, defaults to `True`):
            Whether to normalize the image.
        image_mean (`float` or `List[float]`, *optional*, defaults to `self.image_mean`):
            Image mean to use for normalization. Only has an effect if `do_normalize` is set to `True`.
        image_std (`float` or `List[float]`, *optional*, defaults to `self.image_std`):
            Image standard deviation to use for normalization. Only has an effect if `do_normalize` is set to
            `True`.
        do_pad (`bool`, *optional*, defaults to `True`):
            Whether or not to pad the images to the largest height and width in the batch.
        max_image_tiles (`int`, *optional*, defaults to 4):
            The maximum number of tiles to split the image into.
    """
    model_input_names = ...
    def __init__(self, do_convert_rgb: bool = ..., do_resize: bool = ..., size: Optional[Dict[str, int]] = ..., resample: PILImageResampling = ..., do_rescale: bool = ..., rescale_factor: float = ..., do_normalize: bool = ..., image_mean: Optional[Union[float, List[float]]] = ..., image_std: Optional[Union[float, List[float]]] = ..., do_pad: bool = ..., max_image_tiles: int = ..., **kwargs) -> None:
        ...
    
    def preprocess(self, images: ImageInput, do_convert_rgb: Optional[bool] = ..., do_resize: Optional[bool] = ..., size: Optional[Dict[str, int]] = ..., resample: Optional[PILImageResampling] = ..., do_rescale: Optional[bool] = ..., rescale_factor: Optional[float] = ..., do_normalize: Optional[bool] = ..., image_mean: Optional[Union[float, List[float]]] = ..., image_std: Optional[Union[float, List[float]]] = ..., do_pad: Optional[bool] = ..., max_image_tiles: Optional[int] = ..., input_data_format: Optional[Union[str, ChannelDimension]] = ..., return_tensors: Optional[Union[str, TensorType]] = ...): # -> BatchFeature:
        """
        Preprocess a batch of images.

        Args:
            images (`ImageInput`):
                A list of images to preprocess.
            do_convert_rgb (`bool`, *optional*, defaults to `self.do_convert_rgb`):
                Whether to convert the image to RGB.
            do_resize (`bool`, *optional*, defaults to `self.do_resize`):
                Whether to resize the image.
            size (`Dict[str, int]`, *optional*, defaults to `self.size`):
                Size of the image tile. Should be a dictionary containing 'height' and 'width' keys, both with integer values.
                The height and width values should be equal.
            resample (`int`, *optional*, defaults to `self.resample`):
                Resampling filter to use if resizing the image. This can be one of the enum `PILImageResampling`. Only
                has an effect if `do_resize` is set to `True`.
            do_rescale (`bool`, *optional*, defaults to `self.do_rescale`):
                Whether to rescale the image.
            rescale_factor (`float`, *optional*, defaults to `self.rescale_factor`):
                Rescale factor to rescale the image by if `do_rescale` is set to `True`.
            do_normalize (`bool`, *optional*, defaults to `self.do_normalize`):
                Whether to normalize the image.
            image_mean (`float` or `List[float]`, *optional*, defaults to `self.image_mean`):
                Image mean to use for normalization. Only has an effect if `do_normalize` is set to `True`.
            image_std (`float` or `List[float]`, *optional*, defaults to `self.image_std`):
                Image standard deviation to use for normalization. Only has an effect if `do_normalize` is set to
                `True`.
            do_pad (`bool`, *optional*, defaults to `self.do_pad`):
                Whether or not to pad the images to the largest height and width in the batch.
            max_image_tiles (`int`, *optional*, defaults to `self.max_image_tiles`):
                The maximum number of tiles to split the image into.
            input_data_format (`ChannelDimension` or `str`, *optional*):
                The channel dimension format for the input image. If unset, the channel dimension format is inferred
                from the input image. Can be one of:
                - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
                - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.
            return_tensors (`str` or `TensorType`, *optional*):
                The type of tensors to return. Can be one of:
                - Unset: Return a list of `np.ndarray`.
                - `TensorType.TENSORFLOW` or `'tf'`: Return a batch of type `tf.Tensor`.
                - `TensorType.PYTORCH` or `'pt'`: Return a batch of type `torch.Tensor`.
                - `TensorType.NUMPY` or `'np'`: Return a batch of type `np.ndarray`.
                - `TensorType.JAX` or `'jax'`: Return a batch of type `jax.numpy.ndarray`.

        Returns:
            `BatchFeature` of the following structure:
                - **pixel_values** (`TensorType`): The preprocessed pixel values.
                - **aspect_ratio_ids** (`TensorType`): The aspect ratio ids of the images.
                - **num_tiles** (`List[List[int]]`): The number of tiles for each image in the batch.
        """
        ...
    
    def pad(self, image: np.ndarray, size: Dict[str, int], aspect_ratio: Tuple[int, int], data_format: Optional[Union[str, ChannelDimension]] = ..., input_data_format: Optional[Union[str, ChannelDimension]] = ...) -> np.ndarray:
        """
        Pad an image to the `size` x `aspect_ratio`. For example, if size is {height: 224, width: 224} and aspect ratio is
        (1, 2), the image will be padded to 224x448.

        Args:
            image (`np.ndarray`):
                Image to resize.
            size (`Dict[str, int]`):
                Size of the output image.
            aspect_ratio (`Tuple[int, int]`):
                The aspect ratio of the image.
            data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format of the image. If not provided, it will be the same as the input image.
            input_data_format (`ChannelDimension` or `str`, *optional*):
                The channel dimension format of the input image. If not provided, it will be inferred.

        Returns:
            `np.ndarray`: The padded image.
        """
        ...
    
    def resize(self, image: np.ndarray, size: Dict[str, int], max_image_tiles: int, resample: PILImageResampling = ..., data_format: Optional[Union[str, ChannelDimension]] = ..., input_data_format: Optional[Union[str, ChannelDimension]] = ...) -> Union[np.ndarray, Tuple[int, int]]:
        """
        Resizes an image to fit within a tiled canvas while maintaining its aspect ratio.
        The optimal canvas size is calculated based on the maximum number of tiles and the tile size.

        The function first determines the best tile arrangement for the image, then resizes the image
        to fit within this canvas. The resized image and the number of tiles along the height and width
        dimensions are returned.

        Args:
            image (`np.ndarray`):
                Image to resize.
            size (`Dict[str, int]`):
                Size of the output image.
            max_image_tiles (`int`):
                The maximum number of tiles to split the image into.
            resample (`PILImageResampling`, *optional*, defaults to `PILImageResampling.BICUBIC`):
                Resampling filter to use when resizing the image.
            data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format of the image. If not provided, it will be the same as the input image.
            input_data_format (`ChannelDimension` or `str`, *optional*):
                The channel dimension format of the input image. If not provided, it will be inferred.

        Returns:
            `Union[np.ndarray, Tuple[int, int]]`: The resized image and a tuple containing the number of tiles
            along the height and width dimensions.
        """
        ...
    

