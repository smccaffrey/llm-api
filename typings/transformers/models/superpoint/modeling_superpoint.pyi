"""
This type stub file was generated by pyright.
"""

import torch
from dataclasses import dataclass
from typing import Optional, Tuple, Union
from torch import nn
from transformers import PreTrainedModel
from transformers.modeling_outputs import BaseModelOutputWithNoAttention
from transformers.models.superpoint.configuration_superpoint import SuperPointConfig
from ...utils import ModelOutput, add_start_docstrings, add_start_docstrings_to_model_forward

"""PyTorch SuperPoint model."""
logger = ...
_CONFIG_FOR_DOC = ...
_CHECKPOINT_FOR_DOC = ...
def remove_keypoints_from_borders(keypoints: torch.Tensor, scores: torch.Tensor, border: int, height: int, width: int) -> Tuple[torch.Tensor, torch.Tensor]:
    """Removes keypoints (and their associated scores) that are too close to the border"""
    ...

def top_k_keypoints(keypoints: torch.Tensor, scores: torch.Tensor, k: int) -> Tuple[torch.Tensor, torch.Tensor]:
    """Keeps the k keypoints with highest score"""
    ...

def simple_nms(scores: torch.Tensor, nms_radius: int) -> torch.Tensor:
    """Applies non-maximum suppression on scores"""
    ...

@dataclass
class SuperPointKeypointDescriptionOutput(ModelOutput):
    """
    Base class for outputs of image point description models. Due to the nature of keypoint detection, the number of
    keypoints is not fixed and can vary from image to image, which makes batching non-trivial. In the batch of images,
    the maximum number of keypoints is set as the dimension of the keypoints, scores and descriptors tensors. The mask
    tensor is used to indicate which values in the keypoints, scores and descriptors tensors are keypoint information
    and which are padding.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*):
            Loss computed during training.
        keypoints (`torch.FloatTensor` of shape `(batch_size, num_keypoints, 2)`):
            Relative (x, y) coordinates of predicted keypoints in a given image.
        scores (`torch.FloatTensor` of shape `(batch_size, num_keypoints)`):
            Scores of predicted keypoints.
        descriptors (`torch.FloatTensor` of shape `(batch_size, num_keypoints, descriptor_size)`):
            Descriptors of predicted keypoints.
        mask (`torch.BoolTensor` of shape `(batch_size, num_keypoints)`):
            Mask indicating which values in keypoints, scores and descriptors are keypoint information.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or
        when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each stage) of shape `(batch_size, sequence_length, hidden_size)`. Hidden-states
            (also called feature maps) of the model at the output of each stage.
    """
    loss: Optional[torch.FloatTensor] = ...
    keypoints: Optional[torch.IntTensor] = ...
    scores: Optional[torch.FloatTensor] = ...
    descriptors: Optional[torch.FloatTensor] = ...
    mask: Optional[torch.BoolTensor] = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...


class SuperPointConvBlock(nn.Module):
    def __init__(self, config: SuperPointConfig, in_channels: int, out_channels: int, add_pooling: bool = ...) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
        ...
    


class SuperPointEncoder(nn.Module):
    """
    SuperPoint encoder module. It is made of 4 convolutional layers with ReLU activation and max pooling, reducing the
     dimensionality of the image.
    """
    def __init__(self, config: SuperPointConfig) -> None:
        ...
    
    def forward(self, input, output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple, BaseModelOutputWithNoAttention]:
        ...
    


class SuperPointInterestPointDecoder(nn.Module):
    """
    The SuperPointInterestPointDecoder uses the output of the SuperPointEncoder to compute the keypoint with scores.
    The scores are first computed by a convolutional layer, then a softmax is applied to get a probability distribution
    over the 65 possible keypoint classes. The keypoints are then extracted from the scores by thresholding and
    non-maximum suppression. Post-processing is then applied to remove keypoints too close to the image borders as well
    as to keep only the k keypoints with highest score.
    """
    def __init__(self, config: SuperPointConfig) -> None:
        ...
    
    def forward(self, encoded: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        ...
    


class SuperPointDescriptorDecoder(nn.Module):
    """
    The SuperPointDescriptorDecoder uses the outputs of both the SuperPointEncoder and the
    SuperPointInterestPointDecoder to compute the descriptors at the keypoints locations.

    The descriptors are first computed by a convolutional layer, then normalized to have a norm of 1. The descriptors
    are then interpolated at the keypoints locations.
    """
    def __init__(self, config: SuperPointConfig) -> None:
        ...
    
    def forward(self, encoded: torch.Tensor, keypoints: torch.Tensor) -> torch.Tensor:
        """Based on the encoder output and the keypoints, compute the descriptors for each keypoint"""
        ...
    


class SuperPointPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = SuperPointConfig
    base_model_prefix = ...
    main_input_name = ...
    supports_gradient_checkpointing = ...
    def extract_one_channel_pixel_values(self, pixel_values: torch.FloatTensor) -> torch.FloatTensor:
        """
        Assuming pixel_values has shape (batch_size, 3, height, width), and that all channels values are the same,
        extract the first channel value to get a tensor of shape (batch_size, 1, height, width) for SuperPoint. This is
        a workaround for the issue discussed in :
        https://github.com/huggingface/transformers/pull/25786#issuecomment-1730176446

        Args:
            pixel_values: torch.FloatTensor of shape (batch_size, 3, height, width)

        Returns:
            pixel_values: torch.FloatTensor of shape (batch_size, 1, height, width)

        """
        ...
    


SUPERPOINT_START_DOCSTRING = ...
SUPERPOINT_INPUTS_DOCSTRING = ...
@add_start_docstrings("SuperPoint model outputting keypoints and descriptors.", SUPERPOINT_START_DOCSTRING)
class SuperPointForKeypointDetection(SuperPointPreTrainedModel):
    """
    SuperPoint model. It consists of a SuperPointEncoder, a SuperPointInterestPointDecoder and a
    SuperPointDescriptorDecoder. SuperPoint was proposed in `SuperPoint: Self-Supervised Interest Point Detection and
    Description <https://arxiv.org/abs/1712.07629>`__ by Daniel DeTone, Tomasz Malisiewicz, and Andrew Rabinovich. It
    is a fully convolutional neural network that extracts keypoints and descriptors from an image. It is trained in a
    self-supervised manner, using a combination of a photometric loss and a loss based on the homographic adaptation of
    keypoints. It is made of a convolutional encoder and two decoders: one for keypoints and one for descriptors.
    """
    def __init__(self, config: SuperPointConfig) -> None:
        ...
    
    @add_start_docstrings_to_model_forward(SUPERPOINT_INPUTS_DOCSTRING)
    def forward(self, pixel_values: torch.FloatTensor, labels: Optional[torch.LongTensor] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple, SuperPointKeypointDescriptionOutput]:
        """
        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, SuperPointForKeypointDetection
        >>> import torch
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> processor = AutoImageProcessor.from_pretrained("magic-leap-community/superpoint")
        >>> model = SuperPointForKeypointDetection.from_pretrained("magic-leap-community/superpoint")

        >>> inputs = processor(image, return_tensors="pt")
        >>> outputs = model(**inputs)
        ```"""
        ...
    

