"""
This type stub file was generated by pyright.
"""

import torch
from typing import List, Optional, Tuple, Union
from torch import nn
from ...modeling_outputs import SemanticSegmenterOutput
from ...modeling_utils import PreTrainedModel
from ...utils import add_start_docstrings, add_start_docstrings_to_model_forward, replace_return_docstrings
from .configuration_upernet import UperNetConfig

"""PyTorch UperNet model. Based on OpenMMLab's implementation, found in https://github.com/open-mmlab/mmsegmentation."""
_CONFIG_FOR_DOC = ...
class UperNetConvModule(nn.Module):
    """
    A convolutional block that bundles conv/norm/activation layers. This block simplifies the usage of convolution
    layers, which are commonly used with a norm layer (e.g., BatchNorm) and activation layer (e.g., ReLU).
    """
    def __init__(self, in_channels: int, out_channels: int, kernel_size: Union[int, Tuple[int, int]], padding: Union[int, Tuple[int, int], str] = ..., bias: bool = ..., dilation: Union[int, Tuple[int, int]] = ...) -> None:
        ...
    
    def forward(self, input: torch.Tensor) -> torch.Tensor:
        ...
    


class UperNetPyramidPoolingBlock(nn.Module):
    def __init__(self, pool_scale: int, in_channels: int, channels: int) -> None:
        ...
    
    def forward(self, input: torch.Tensor) -> torch.Tensor:
        ...
    


class UperNetPyramidPoolingModule(nn.Module):
    """
    Pyramid Pooling Module (PPM) used in PSPNet.

    Args:
        pool_scales (`Tuple[int]`):
            Pooling scales used in Pooling Pyramid Module.
        in_channels (`int`):
            Input channels.
        channels (`int`):
            Channels after modules, before conv_seg.
        align_corners (`bool`):
            align_corners argument of F.interpolate.
    """
    def __init__(self, pool_scales: Tuple[int, ...], in_channels: int, channels: int, align_corners: bool) -> None:
        ...
    
    def forward(self, x: torch.Tensor) -> List[torch.Tensor]:
        ...
    


class UperNetHead(nn.Module):
    """
    Unified Perceptual Parsing for Scene Understanding. This head is the implementation of
    [UPerNet](https://arxiv.org/abs/1807.10221).
    """
    def __init__(self, config, in_channels) -> None:
        ...
    
    def init_weights(self): # -> None:
        ...
    
    def psp_forward(self, inputs): # -> Any:
        ...
    
    def forward(self, encoder_hidden_states: torch.Tensor) -> torch.Tensor:
        ...
    


class UperNetFCNHead(nn.Module):
    """
    Fully Convolution Networks for Semantic Segmentation. This head is the implementation of
    [FCNNet](https://arxiv.org/abs/1411.4038>).

    Args:
        config:
            Configuration.
        in_channels (int):
            Number of input channels.
        kernel_size (int):
            The kernel size for convs in the head. Default: 3.
        dilation (int):
            The dilation rate for convs in the head. Default: 1.
    """
    def __init__(self, config, in_index: int = ..., kernel_size: int = ..., dilation: Union[int, Tuple[int, int]] = ...) -> None:
        ...
    
    def init_weights(self): # -> None:
        ...
    
    def forward(self, encoder_hidden_states: torch.Tensor) -> torch.Tensor:
        ...
    


class UperNetPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = UperNetConfig
    main_input_name = ...
    _no_split_modules = ...
    def init_weights(self): # -> None:
        """Initialize the weights"""
        ...
    


UPERNET_START_DOCSTRING = ...
UPERNET_INPUTS_DOCSTRING = ...
@add_start_docstrings("""UperNet framework leveraging any vision backbone e.g. for ADE20k, CityScapes.""", UPERNET_START_DOCSTRING)
class UperNetForSemanticSegmentation(UperNetPreTrainedModel):
    def __init__(self, config) -> None:
        ...
    
    @add_start_docstrings_to_model_forward(UPERNET_INPUTS_DOCSTRING.format("batch_size, sequence_length"))
    @replace_return_docstrings(output_type=SemanticSegmenterOutput, config_class=_CONFIG_FOR_DOC)
    def forward(self, pixel_values: Optional[torch.Tensor] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., labels: Optional[torch.Tensor] = ..., return_dict: Optional[bool] = ...) -> Union[tuple, SemanticSegmenterOutput]:
        r"""
        labels (`torch.LongTensor` of shape `(batch_size, height, width)`, *optional*):
            Ground truth semantic segmentation maps for computing the loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels > 1`, a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:
        ```python
        >>> from transformers import AutoImageProcessor, UperNetForSemanticSegmentation
        >>> from PIL import Image
        >>> from huggingface_hub import hf_hub_download

        >>> image_processor = AutoImageProcessor.from_pretrained("openmmlab/upernet-convnext-tiny")
        >>> model = UperNetForSemanticSegmentation.from_pretrained("openmmlab/upernet-convnext-tiny")

        >>> filepath = hf_hub_download(
        ...     repo_id="hf-internal-testing/fixtures_ade20k", filename="ADE_val_00000001.jpg", repo_type="dataset"
        ... )
        >>> image = Image.open(filepath).convert("RGB")

        >>> inputs = image_processor(images=image, return_tensors="pt")

        >>> outputs = model(**inputs)

        >>> logits = outputs.logits  # shape (batch_size, num_labels, height, width)
        >>> list(logits.shape)
        [1, 150, 512, 512]
        ```"""
        ...
    

