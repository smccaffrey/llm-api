"""
This type stub file was generated by pyright.
"""

import torch
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Union
from torch import Tensor, nn
from ...modeling_outputs import BaseModelOutput
from ...modeling_utils import PreTrainedModel
from ...utils import ModelOutput, add_start_docstrings, add_start_docstrings_to_model_forward
from .configuration_sam import SamConfig, SamMaskDecoderConfig, SamPromptEncoderConfig, SamVisionConfig

"""PyTorch SAM model."""
logger = ...
_CONFIG_FOR_DOC = ...
_CHECKPOINT_FOR_DOC = ...
@dataclass
class SamVisionEncoderOutput(ModelOutput):
    """
    Base class for sam vision model's outputs that also contains image embeddings obtained by applying the projection
    layer to the pooler_output.

    Args:
        image_embeds (`torch.FloatTensor` of shape `(batch_size, output_dim)` *optional* returned when model is initialized with `with_projection=True`):
            The image embeddings obtained by applying the projection layer to the pooler_output.
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    image_embeds: Optional[torch.FloatTensor] = ...
    last_hidden_state: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor, ...]] = ...
    attentions: Optional[Tuple[torch.FloatTensor, ...]] = ...


@dataclass
class SamImageSegmentationOutput(ModelOutput):
    """
    Base class for Segment-Anything model's output

    Args:
        iou_scores (`torch.FloatTensor` of shape `(batch_size, num_masks)`):
            The iou scores of the predicted masks.
        pred_masks (`torch.FloatTensor` of shape `(batch_size, num_masks, height, width)`):
            The predicted low resolutions masks. Needs to be post-processed by the processor
        vision_hidden_states  (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the vision model at the output of each layer plus the optional initial embedding outputs.
        vision_attentions  (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
        mask_decoder_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    iou_scores: torch.FloatTensor = ...
    pred_masks: torch.FloatTensor = ...
    vision_hidden_states: Optional[Tuple[torch.FloatTensor, ...]] = ...
    vision_attentions: Optional[Tuple[torch.FloatTensor, ...]] = ...
    mask_decoder_attentions: Optional[Tuple[torch.FloatTensor, ...]] = ...


class SamPatchEmbeddings(nn.Module):
    """
    This class turns `pixel_values` of shape `(batch_size, num_channels, height, width)` into the initial
    `hidden_states` (patch embeddings) of shape `(batch_size, seq_length, hidden_size)` to be consumed by a
    Transformer.
    """
    def __init__(self, config) -> None:
        ...
    
    def forward(self, pixel_values): # -> Any:
        ...
    


class SamMLPBlock(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
        ...
    


class SamLayerNorm(nn.Module):
    r"""LayerNorm that supports two data formats: channels_last (default) or channels_first.
    The ordering of the dimensions in the inputs. channels_last corresponds to inputs with shape (batch_size, height,
    width, channels) while channels_first corresponds to inputs with shape (batch_size, channels, height, width).
    """
    def __init__(self, normalized_shape, eps=..., data_format=...) -> None:
        ...
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        ...
    


class SamAttention(nn.Module):
    """
    SAM's attention layer that allows for downscaling the size of the embedding after projection to queries, keys, and
    values.
    """
    def __init__(self, config, downsample_rate=...) -> None:
        ...
    
    def forward(self, query: Tensor, key: Tensor, value: Tensor, attention_similarity: Tensor = ...) -> Tensor:
        ...
    


class SamTwoWayAttentionBlock(nn.Module):
    def __init__(self, config, attention_downsample_rate: int = ..., skip_first_layer_pe: bool = ...) -> None:
        """
        A transformer block with four layers:
            (1) self-attention of sparse inputs (2) cross attention of sparse inputs -> dense inputs (3) mlp block on
            sparse inputs (4) cross attention of dense inputs -> sparse inputs

        Arguments:
            config (`SamMaskDecoderConfig`):
                The configuration file used to instantiate the block
            attention_downsample_rate (*optionalk*, int, defaults to 2):
                The downsample ratio of the block used to reduce the inner dim of the attention.
            skip_first_layer_pe (*optional*, bool, defaults to `False`):
                Whether or not to skip the addition of the query_point_embedding on the first layer.
        """
        ...
    
    def forward(self, queries: Tensor, keys: Tensor, query_point_embedding: Tensor, key_point_embedding: Tensor, attention_similarity: Tensor, output_attentions: bool = ...): # -> tuple[Tensor, Tensor, Any] | tuple[Tensor, Tensor, None]:
        ...
    


class SamTwoWayTransformer(nn.Module):
    def __init__(self, config: SamMaskDecoderConfig) -> None:
        ...
    
    def forward(self, point_embeddings: Tensor, image_embeddings: Tensor, image_positional_embeddings: Tensor, attention_similarity: Tensor, target_embedding=..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple, BaseModelOutput]:
        ...
    


class SamFeedForward(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int, num_layers: int, sigmoid_output: bool = ...) -> None:
        ...
    
    def forward(self, hidden_states): # -> Tensor | Any:
        ...
    


class SamMaskDecoder(nn.Module):
    def __init__(self, config: SamMaskDecoderConfig) -> None:
        ...
    
    def forward(self, image_embeddings: torch.Tensor, image_positional_embeddings: torch.Tensor, sparse_prompt_embeddings: torch.Tensor, dense_prompt_embeddings: torch.Tensor, multimask_output: bool, output_attentions: Optional[bool] = ..., attention_similarity: torch.Tensor = ..., target_embedding: torch.Tensor = ...) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Predict masks given image and prompt embeddings.

        Args:
            image_embeddings (`torch.Tensor`):
                the embeddings from the image encoder
            image_positional_embedding (`torch.Tensor`):
                positional encoding with the shape of image_embeddings
            sparse_prompt_embeddings (`torch.Tensor`):
                The embeddings of the points and boxes
            dense_prompt_embeddings (`torch.Tensor`):
                the embeddings of the mask inputs
            multimask_output (bool):
                Whether to return multiple masks or a single mask.
            output_attentions (bool, *optional*):
                Whether or not to return the attentions tensors of all attention layers.
        """
        ...
    


class SamPositionalEmbedding(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def forward(self, input_coords, input_shape=...): # -> Tensor:
        """Positionally encode points that are normalized to [0,1]."""
        ...
    


class SamMaskEmbedding(nn.Module):
    def __init__(self, config: SamPromptEncoderConfig) -> None:
        ...
    
    def forward(self, masks): # -> Any:
        ...
    


class SamPromptEncoder(nn.Module):
    def __init__(self, config: SamPromptEncoderConfig, shared_patch_embedding) -> None:
        ...
    
    def forward(self, input_points: Optional[Tuple[torch.Tensor, torch.Tensor]], input_labels: Optional[torch.Tensor], input_boxes: Optional[torch.Tensor], input_masks: Optional[torch.Tensor]) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Embeds different types of prompts, returning both sparse and dense embeddings.

        Args:
            points (`torch.Tensor`, *optional*):
                point coordinates and labels to embed.
            boxes (`torch.Tensor`, *optional*):
                boxes to embed
            masks (`torch.Tensor`, *optional*):
                masks to embed
        """
        ...
    


class SamVisionAttention(nn.Module):
    """Multi-head Attention block with relative position embeddings."""
    def __init__(self, config, window_size) -> None:
        ...
    
    def get_rel_pos(self, q_size: int, k_size: int, rel_pos: torch.Tensor) -> torch.Tensor:
        """
        Get relative positional embeddings according to the relative positions of
            query and key sizes.

        Args:
            q_size (int):
                size of the query.
            k_size (int):
                size of key k.
            rel_pos (`torch.Tensor`):
                relative position embeddings (L, channel).

        Returns:
            Extracted positional embeddings according to relative positions.
        """
        ...
    
    def add_decomposed_rel_pos(self, attn: torch.Tensor, query: torch.Tensor, rel_pos_h: torch.Tensor, rel_pos_w: torch.Tensor, q_size: Tuple[int, int], k_size: Tuple[int, int]) -> torch.Tensor:
        """
        Calculate decomposed Relative Positional Embeddings from :paper:`mvitv2`.
        https://github.com/facebookresearch/mvit/blob/19786631e330df9f3622e5402b4a419a263a2c80/mvit/models/attention.py

        Args:
            attn (`torch.Tensor`):
                attention map.
            query (`torch.Tensor`):
                query q in the attention layer with shape (batch_size, query_height * query_width, channel).
            rel_pos_h (`torch.Tensor`):
                relative position embeddings (Lh, channel) for height axis.
            rel_pos_w (`torch.Tensor`):
                relative position embeddings (Lw, channel) for width axis.
            q_size (tuple):
                spatial sequence size of query q with (query_height, query_width).
            k_size (tuple):
                spatial sequence size of key k with (key_height, key_width).

        Returns:
            attn (`torch.Tensor`):
                attention map with added relative positional embeddings.
        """
        ...
    
    def forward(self, hidden_states: torch.Tensor, output_attentions=...) -> torch.Tensor:
        ...
    


class SamVisionLayer(nn.Module):
    def __init__(self, config, window_size) -> None:
        ...
    
    def window_partition(self, hidden_states: torch.Tensor, window_size: int) -> Tuple[torch.Tensor, Tuple[int, int]]:
        """
        Args:
        Partition into non-overlapping windows with padding if needed.
            hidden_states (tensor): input tokens with [batch_size, height, width, channel]. window_size (int): window
            size.

        Returns:
            windows: windows after partition with [batch_size * num_windows, window_size, window_size, channel].
            (pad_height, pad_width): padded height and width before partition
        """
        ...
    
    def window_unpartition(self, windows: torch.Tensor, window_size: int, padding_shape: Tuple[int, int], original_shape: Tuple[int, int]) -> torch.Tensor:
        """
        Args:
        Window unpartition into original sequences and removing padding.
            hidden_states (tensor):
                input tokens with [batch_size * num_windows, window_size, window_size, channel].
            window_size (int):
                window size.
            padding_shape (Tuple):
                padded height and width (pad_height, pad_width).
            original_shape (Tuple): original height and width (height, width) before padding.

        Returns:
            hidden_states: unpartitioned sequences with [batch_size, height, width, channel].
        """
        ...
    
    def forward(self, hidden_states: torch.Tensor, output_attentions: Optional[bool] = ...) -> Tuple[torch.FloatTensor]:
        ...
    


class SamVisionNeck(nn.Module):
    def __init__(self, config: SamVisionConfig) -> None:
        ...
    
    def forward(self, hidden_states): # -> Any:
        ...
    


class SamVisionEncoder(nn.Module):
    def __init__(self, config: SamVisionConfig) -> None:
        ...
    
    def get_input_embeddings(self): # -> SamPatchEmbeddings:
        ...
    
    def forward(self, pixel_values: Optional[torch.FloatTensor] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple, SamVisionEncoderOutput]:
        ...
    


class SamPreTrainedModel(PreTrainedModel):
    config_class = SamConfig
    base_model_prefix = ...
    main_input_name = ...
    _no_split_modules = ...


SAM_START_DOCSTRING = ...
SAM_INPUTS_DOCSTRING = ...
@add_start_docstrings("Segment Anything Model (SAM) for generating segmentation masks, given an input image and ", " optional 2D location and bounding boxes.", SAM_START_DOCSTRING)
class SamModel(SamPreTrainedModel):
    _tied_weights_keys = ...
    def __init__(self, config) -> None:
        ...
    
    def get_input_embeddings(self): # -> SamPatchEmbeddings:
        ...
    
    def get_image_wide_positional_embeddings(self): # -> Any:
        ...
    
    @torch.no_grad()
    def get_image_embeddings(self, pixel_values, output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...): # -> Any:
        r"""
        Returns the image embeddings by passing the pixel values through the vision encoder.

        Args:
            pixel_values (`torch.FloatTensor` of shape `(batch_size, num_channels, height, width)`):
                Input pixel values
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers.
            output_hidden_states (`bool`, *optional*):
                Whether or not to return the hidden states of all layers.
            return_dict (`bool`, *optional*):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.

        """
        ...
    
    @torch.no_grad()
    def get_prompt_embeddings(self, input_points: Optional[torch.FloatTensor] = ..., input_labels: Optional[torch.LongTensor] = ..., input_boxes: Optional[torch.FloatTensor] = ..., input_masks: Optional[torch.LongTensor] = ...): # -> Any:
        r"""
        Returns the prompt embeddings by passing the input points, labels, boxes and masks through the prompt encoder.

        Args:
            input_points (`torch.FloatTensor` of shape `(batch_size, point_batch_size, num_points_per_image, 2)`):
                Optional input points for the prompt encoder. The padding of the point is automatically done by the
                processor. `point_batch_size` refers to the number of masks that we want the model to predict per
                point. The model will output `point_batch_size` times 3 masks in total.
            input_labels (`torch.LongTensor` of shape `(batch_size, point_batch_size, num_points_per_image)`):
                Optional input labels for the prompt encoder. The padding of the labels is automatically done by the
                processor, or can be fed by the user.
            input_boxes (`torch.FloatTensor` of shape `(batch_size, num_boxes_per_image, 4)`):
                Optional input boxes for the prompt encoder. The padding of the boxes is automatically done by the
                processor. users can also pass manually the input boxes.
            input_masks (`torch.LongTensor` of shape `(batch_size, image_size, image_size)`):
                Optional input masks for the prompt encoder.
        """
        ...
    
    @add_start_docstrings_to_model_forward(SAM_INPUTS_DOCSTRING)
    def forward(self, pixel_values: Optional[torch.FloatTensor] = ..., input_points: Optional[torch.FloatTensor] = ..., input_labels: Optional[torch.LongTensor] = ..., input_boxes: Optional[torch.FloatTensor] = ..., input_masks: Optional[torch.LongTensor] = ..., image_embeddings: Optional[torch.FloatTensor] = ..., multimask_output: bool = ..., attention_similarity: Optional[torch.FloatTensor] = ..., target_embedding: Optional[torch.FloatTensor] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., **kwargs) -> List[Dict[str, torch.Tensor]]:
        r"""
        Example:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoModel, AutoProcessor

        >>> model = AutoModel.from_pretrained("facebook/sam-vit-base")
        >>> processor = AutoProcessor.from_pretrained("facebook/sam-vit-base")

        >>> img_url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/model_doc/sam-car.png"
        >>> raw_image = Image.open(requests.get(img_url, stream=True).raw).convert("RGB")
        >>> input_points = [[[400, 650]]]  # 2D location of a window on the car
        >>> inputs = processor(images=raw_image, input_points=input_points, return_tensors="pt")

        >>> # Get segmentation mask
        >>> outputs = model(**inputs)

        >>> # Postprocess masks
        >>> masks = processor.post_process_masks(
        ...     outputs.pred_masks, inputs["original_sizes"], inputs["reshaped_input_sizes"]
        ... )
        ```
        """
        ...
    

