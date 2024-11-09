"""
This type stub file was generated by pyright.
"""

import torch
from dataclasses import dataclass
from typing import Optional, Tuple, Union
from torch import nn
from ...modeling_utils import PreTrainedModel
from ...utils import ModelOutput, add_code_sample_docstrings, add_start_docstrings, add_start_docstrings_to_model_forward
from .configuration_donut_swin import DonutSwinConfig

"""PyTorch Donut Swin Transformer model.

This implementation is identical to a regular Swin Transformer, without final layer norm on top of the final hidden
states."""
logger = ...
_CONFIG_FOR_DOC = ...
_CHECKPOINT_FOR_DOC = ...
_EXPECTED_OUTPUT_SHAPE = ...
@dataclass
class DonutSwinEncoderOutput(ModelOutput):
    """
    DonutSwin encoder's outputs, with potential hidden states and attentions.

    Args:
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each stage) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
        reshaped_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, hidden_size, height, width)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs reshaped to
            include the spatial dimensions.
    """
    last_hidden_state: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor, ...]] = ...
    attentions: Optional[Tuple[torch.FloatTensor, ...]] = ...
    reshaped_hidden_states: Optional[Tuple[torch.FloatTensor, ...]] = ...


@dataclass
class DonutSwinModelOutput(ModelOutput):
    """
    DonutSwin model's outputs that also contains a pooling of the last hidden states.

    Args:
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        pooler_output (`torch.FloatTensor` of shape `(batch_size, hidden_size)`, *optional*, returned when `add_pooling_layer=True` is passed):
            Average pooling of the last layer hidden-state.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each stage) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
        reshaped_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, hidden_size, height, width)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs reshaped to
            include the spatial dimensions.
    """
    last_hidden_state: torch.FloatTensor = ...
    pooler_output: Optional[torch.FloatTensor] = ...
    hidden_states: Optional[Tuple[torch.FloatTensor, ...]] = ...
    attentions: Optional[Tuple[torch.FloatTensor, ...]] = ...
    reshaped_hidden_states: Optional[Tuple[torch.FloatTensor, ...]] = ...


def window_partition(input_feature, window_size):
    """
    Partitions the given input into windows.
    """
    ...

def window_reverse(windows, window_size, height, width):
    """
    Merges windows to produce higher resolution features.
    """
    ...

class DonutSwinEmbeddings(nn.Module):
    """
    Construct the patch and position embeddings. Optionally, also the mask token.
    """
    def __init__(self, config, use_mask_token=...) -> None:
        ...
    
    def interpolate_pos_encoding(self, embeddings: torch.Tensor, height: int, width: int) -> torch.Tensor:
        """
        This method allows to interpolate the pre-trained position encodings, to be able to use the model on higher resolution
        images. This method is also adapted to support torch.jit tracing.

        Adapted from:
        - https://github.com/facebookresearch/dino/blob/de9ee3df6cf39fac952ab558447af1fa1365362a/vision_transformer.py#L174-L194, and
        - https://github.com/facebookresearch/dinov2/blob/e1277af2ba9496fbadf7aec6eba56e8d882d1e35/dinov2/models/vision_transformer.py#L179-L211
        """
        ...
    
    def forward(self, pixel_values: Optional[torch.FloatTensor], bool_masked_pos: Optional[torch.BoolTensor] = ..., interpolate_pos_encoding: bool = ...) -> Tuple[torch.Tensor]:
        ...
    


class DonutSwinPatchEmbeddings(nn.Module):
    """
    This class turns `pixel_values` of shape `(batch_size, num_channels, height, width)` into the initial
    `hidden_states` (patch embeddings) of shape `(batch_size, seq_length, hidden_size)` to be consumed by a
    Transformer.
    """
    def __init__(self, config) -> None:
        ...
    
    def maybe_pad(self, pixel_values, height, width): # -> Tensor:
        ...
    
    def forward(self, pixel_values: Optional[torch.FloatTensor]) -> Tuple[torch.Tensor, Tuple[int]]:
        ...
    


class DonutSwinPatchMerging(nn.Module):
    """
    Patch Merging Layer.

    Args:
        input_resolution (`Tuple[int]`):
            Resolution of input feature.
        dim (`int`):
            Number of input channels.
        norm_layer (`nn.Module`, *optional*, defaults to `nn.LayerNorm`):
            Normalization layer class.
    """
    def __init__(self, input_resolution: Tuple[int], dim: int, norm_layer: nn.Module = ...) -> None:
        ...
    
    def maybe_pad(self, input_feature, height, width): # -> Tensor:
        ...
    
    def forward(self, input_feature: torch.Tensor, input_dimensions: Tuple[int, int]) -> torch.Tensor:
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

class DonutSwinDropPath(nn.Module):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks)."""
    def __init__(self, drop_prob: Optional[float] = ...) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
        ...
    
    def extra_repr(self) -> str:
        ...
    


class DonutSwinSelfAttention(nn.Module):
    def __init__(self, config, dim, num_heads, window_size) -> None:
        ...
    
    def transpose_for_scores(self, x):
        ...
    
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = ..., head_mask: Optional[torch.FloatTensor] = ..., output_attentions: Optional[bool] = ...) -> Tuple[torch.Tensor]:
        ...
    


class DonutSwinSelfOutput(nn.Module):
    def __init__(self, config, dim) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor:
        ...
    


class DonutSwinAttention(nn.Module):
    def __init__(self, config, dim, num_heads, window_size) -> None:
        ...
    
    def prune_heads(self, heads): # -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = ..., head_mask: Optional[torch.FloatTensor] = ..., output_attentions: Optional[bool] = ...) -> Tuple[torch.Tensor]:
        ...
    


class DonutSwinIntermediate(nn.Module):
    def __init__(self, config, dim) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
        ...
    


class DonutSwinOutput(nn.Module):
    def __init__(self, config, dim) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
        ...
    


class DonutSwinLayer(nn.Module):
    def __init__(self, config, dim, input_resolution, num_heads, shift_size=...) -> None:
        ...
    
    def set_shift_and_window_size(self, input_resolution): # -> None:
        ...
    
    def get_attn_mask(self, height, width, dtype, device): # -> Tensor | None:
        ...
    
    def maybe_pad(self, hidden_states, height, width): # -> tuple[Tensor, tuple[Literal[0], Literal[0], Literal[0], Any, Literal[0], Any]]:
        ...
    
    def forward(self, hidden_states: torch.Tensor, input_dimensions: Tuple[int, int], head_mask: Optional[torch.FloatTensor] = ..., output_attentions: Optional[bool] = ..., always_partition: Optional[bool] = ...) -> Tuple[torch.Tensor, torch.Tensor]:
        ...
    


class DonutSwinStage(nn.Module):
    def __init__(self, config, dim, input_resolution, depth, num_heads, drop_path, downsample) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor, input_dimensions: Tuple[int, int], head_mask: Optional[torch.FloatTensor] = ..., output_attentions: Optional[bool] = ..., always_partition: Optional[bool] = ...) -> Tuple[torch.Tensor]:
        ...
    


class DonutSwinEncoder(nn.Module):
    def __init__(self, config, grid_size) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor, input_dimensions: Tuple[int, int], head_mask: Optional[torch.FloatTensor] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., output_hidden_states_before_downsampling: Optional[bool] = ..., always_partition: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple, DonutSwinEncoderOutput]:
        ...
    


class DonutSwinPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = DonutSwinConfig
    base_model_prefix = ...
    main_input_name = ...
    supports_gradient_checkpointing = ...
    _no_split_modules = ...


SWIN_START_DOCSTRING = ...
SWIN_INPUTS_DOCSTRING = ...
@add_start_docstrings("The bare Donut Swin Model transformer outputting raw hidden-states without any specific head on top.", SWIN_START_DOCSTRING)
class DonutSwinModel(DonutSwinPreTrainedModel):
    def __init__(self, config, add_pooling_layer=..., use_mask_token=...) -> None:
        ...
    
    def get_input_embeddings(self): # -> DonutSwinPatchEmbeddings:
        ...
    
    @add_start_docstrings_to_model_forward(SWIN_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(checkpoint=_CHECKPOINT_FOR_DOC, output_type=DonutSwinModelOutput, config_class=_CONFIG_FOR_DOC, modality="vision", expected_output=_EXPECTED_OUTPUT_SHAPE)
    def forward(self, pixel_values: Optional[torch.FloatTensor] = ..., bool_masked_pos: Optional[torch.BoolTensor] = ..., head_mask: Optional[torch.FloatTensor] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., interpolate_pos_encoding: bool = ..., return_dict: Optional[bool] = ...) -> Union[Tuple, DonutSwinModelOutput]:
        r"""
        bool_masked_pos (`torch.BoolTensor` of shape `(batch_size, num_patches)`):
            Boolean masked positions. Indicates which patches are masked (1) and which aren't (0).
        """
        ...
    

