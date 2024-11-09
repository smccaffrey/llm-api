"""
This type stub file was generated by pyright.
"""

import torch
from typing import Optional, Tuple
from torch import Tensor, nn
from ...modeling_outputs import BackboneOutput, BaseModelOutputWithNoAttention, BaseModelOutputWithPoolingAndNoAttention, ImageClassifierOutputWithNoAttention
from ...modeling_utils import PreTrainedModel
from ...utils import add_code_sample_docstrings, add_start_docstrings, add_start_docstrings_to_model_forward, replace_return_docstrings
from ...utils.backbone_utils import BackboneMixin
from .configuration_bit import BitConfig

"""PyTorch BiT model. Also supports backbone for ViT hybrid."""
logger = ...
_CONFIG_FOR_DOC = ...
_CHECKPOINT_FOR_DOC = ...
_EXPECTED_OUTPUT_SHAPE = ...
_IMAGE_CLASS_CHECKPOINT = ...
_IMAGE_CLASS_EXPECTED_OUTPUT = ...
def get_padding_value(padding=..., kernel_size=..., stride=..., dilation=...) -> Tuple[Tuple, bool]:
    r"""
    Utility function to get the tuple padding value given the kernel_size and padding.

    Args:
        padding (Union[`str`, `int`], *optional*):
            Padding value, can be either `"same"`, `"valid"`. If a different value is provided the default padding from
            PyTorch is used.
        kernel_size (`int`, *optional*, defaults to 7):
            Kernel size of the convolution layers.
        stride (`int`, *optional*, defaults to 1):
            Stride value of the convolution layers.
        dilation (`int`, *optional*, defaults to 1):
            Dilation value of the convolution layers.
    """
    ...

class WeightStandardizedConv2d(nn.Conv2d):
    """Conv2d with Weight Standardization. Includes TensorFlow compatible SAME padding. Used for ViT Hybrid model.

    Paper: [Micro-Batch Training with Batch-Channel Normalization and Weight
    Standardization](https://arxiv.org/abs/1903.10520v2)
    """
    def __init__(self, in_channel, out_channels, kernel_size, stride=..., padding=..., dilation=..., groups=..., bias=..., eps=...) -> None:
        ...
    
    def forward(self, hidden_state): # -> Tensor:
        ...
    


class BitGroupNormActivation(nn.GroupNorm):
    r"""
    A module that combines group normalization with an activation function.
    """
    def __init__(self, config, num_channels, eps=..., affine=..., apply_activation=...) -> None:
        ...
    
    def forward(self, hidden_state): # -> Any:
        ...
    


class DynamicPad2d(nn.Module):
    r"""
    A module that wraps dynamic padding of any input, given the parameters of the convolutional layer and the input
    hidden states.
    """
    def __init__(self, kernel_size, stride, dilation, value=...) -> None:
        ...
    
    def __call__(self, input): # -> Tensor:
        ...
    


class BitMaxPool2d(nn.MaxPool2d):
    """Tensorflow like 'SAME' wrapper for 2D max pooling"""
    def __init__(self, kernel_size: int, stride=..., dilation=..., ceil_mode=..., padding=..., padding_value=..., use_dynamic_padding=...) -> None:
        ...
    
    def forward(self, hidden_states): # -> Tensor:
        ...
    


class BitEmbeddings(nn.Module):
    """
    BiT Embeddings (stem) composed of a single aggressive convolution.
    """
    def __init__(self, config: BitConfig) -> None:
        ...
    
    def forward(self, pixel_values: Tensor) -> Tensor:
        ...
    


def drop_path(input: torch.Tensor, drop_prob: float = ..., training: bool = ...) -> torch.Tensor:
    """
    Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks).

    Comment by Ross Wightman: This is the same as the DropConnect impl I created for EfficientNet, etc networks,
    however, the original name is misleading as 'Drop Connect' is a different form of dropout in a separate paper...
    See discussion: https://github.com/tensorflow/tpu/issues/494#issuecomment-532968956 ... I've opted for changing the
    layer and argument names to 'drop path' rather than mix DropConnect as a layer name and use 'survival rate' as the
    argument.
    """
    ...

class BitDropPath(nn.Module):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks)."""
    def __init__(self, drop_prob: Optional[float] = ...) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
        ...
    
    def extra_repr(self) -> str:
        ...
    


def make_div(value, divisor=...): # -> int:
    ...

class BitPreActivationBottleneckLayer(nn.Module):
    """Pre-activation (v2) bottleneck block.
    Follows the implementation of "Identity Mappings in Deep Residual Networks":
    https://github.com/KaimingHe/resnet-1k-layers/blob/master/resnet-pre-act.lua

    Except it puts the stride on 3x3 conv when available.
    """
    def __init__(self, config, in_channels, out_channels=..., bottle_ratio=..., stride=..., dilation=..., first_dilation=..., groups=..., drop_path_rate=..., is_first_layer=...) -> None:
        ...
    
    def forward(self, hidden_states): # -> Any:
        ...
    


class BitBottleneckLayer(nn.Module):
    """Non Pre-activation bottleneck block, equivalent to V1.5/V1b bottleneck. Used for ViT Hybrid."""
    def __init__(self, config, in_channels, out_channels=..., bottle_ratio=..., stride=..., dilation=..., first_dilation=..., groups=..., drop_path_rate=..., is_first_layer=...) -> None:
        ...
    
    def forward(self, hidden_states):
        ...
    


class BitDownsampleConv(nn.Module):
    def __init__(self, config, in_channels, out_channels, stride=..., preact=...) -> None:
        ...
    
    def forward(self, x): # -> Any:
        ...
    


class BitStage(nn.Module):
    """
    A ResNet v2 stage composed by stacked layers.
    """
    def __init__(self, config, in_channels, out_channels, stride, dilation, depth, bottle_ratio=..., layer_dropout=...) -> None:
        ...
    
    def forward(self, input: Tensor) -> Tensor:
        ...
    


class BitEncoder(nn.Module):
    def __init__(self, config: BitConfig) -> None:
        ...
    
    def forward(self, hidden_state: Tensor, output_hidden_states: bool = ..., return_dict: bool = ...) -> BaseModelOutputWithNoAttention:
        ...
    


class BitPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = BitConfig
    base_model_prefix = ...
    main_input_name = ...
    _no_split_modules = ...


BIT_START_DOCSTRING = ...
BIT_INPUTS_DOCSTRING = ...
@add_start_docstrings("The bare BiT model outputting raw features without any specific head on top.", BIT_START_DOCSTRING)
class BitModel(BitPreTrainedModel):
    def __init__(self, config) -> None:
        ...
    
    @add_start_docstrings_to_model_forward(BIT_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(checkpoint=_CHECKPOINT_FOR_DOC, output_type=BaseModelOutputWithPoolingAndNoAttention, config_class=_CONFIG_FOR_DOC, modality="vision", expected_output=_EXPECTED_OUTPUT_SHAPE)
    def forward(self, pixel_values: Tensor, output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> BaseModelOutputWithPoolingAndNoAttention:
        ...
    


@add_start_docstrings("""
    BiT Model with an image classification head on top (a linear layer on top of the pooled features), e.g. for
    ImageNet.
    """, BIT_START_DOCSTRING)
class BitForImageClassification(BitPreTrainedModel):
    def __init__(self, config) -> None:
        ...
    
    @add_start_docstrings_to_model_forward(BIT_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(checkpoint=_IMAGE_CLASS_CHECKPOINT, output_type=ImageClassifierOutputWithNoAttention, config_class=_CONFIG_FOR_DOC, expected_output=_IMAGE_CLASS_EXPECTED_OUTPUT)
    def forward(self, pixel_values: Optional[torch.FloatTensor] = ..., labels: Optional[torch.LongTensor] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> ImageClassifierOutputWithNoAttention:
        r"""
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
        ...
    


@add_start_docstrings("""
    BiT backbone, to be used with frameworks like DETR and MaskFormer.
    """, BIT_START_DOCSTRING)
class BitBackbone(BitPreTrainedModel, BackboneMixin):
    def __init__(self, config) -> None:
        ...
    
    @add_start_docstrings_to_model_forward(BIT_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=BackboneOutput, config_class=_CONFIG_FOR_DOC)
    def forward(self, pixel_values: Tensor, output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> BackboneOutput:
        """
        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, AutoBackbone
        >>> import torch
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> processor = AutoImageProcessor.from_pretrained("google/bit-50")
        >>> model = AutoBackbone.from_pretrained("google/bit-50")

        >>> inputs = processor(image, return_tensors="pt")
        >>> outputs = model(**inputs)
        ```"""
        ...
    


