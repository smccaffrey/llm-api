"""
This type stub file was generated by pyright.
"""

import torch
from dataclasses import dataclass
from typing import List, Optional, Tuple, Union
from torch import nn
from ...cache_utils import Cache
from ...modeling_outputs import BaseModelOutputWithPast
from ...modeling_utils import PreTrainedModel
from ...utils import ModelOutput, add_start_docstrings, add_start_docstrings_to_model_forward, is_flash_attn_2_available, replace_return_docstrings
from .configuration_mimi import MimiConfig

"""PyTorch Mimi model."""
if is_flash_attn_2_available():
    ...
logger = ...
_CONFIG_FOR_DOC = ...
@dataclass
class MimiOutput(ModelOutput):
    """
    Args:
        audio_codes (`torch.LongTensor`  of shape `(batch_size, num_quantizers, codes_length)`, *optional*):
            Discret code embeddings computed using `model.encode`.
        audio_values (`torch.FloatTensor` of shape `(batch_size, sequence_length)`, *optional*)
            Decoded audio values, obtained using the decoder part of Mimi.
        encoder_past_key_values (`Cache`, *optional*):
            Pre-computed hidden-states (key and values in the self-attention blocks) that can be used to speed up sequential decoding of the encoder transformer.
            This typically consists in the `past_key_values` returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.

            The model will output the same cache format that is fed as input.

            If `past_key_values` are used, the user can optionally input only the last `audio_values` or `audio_codes (those that don't
            have their past key value states given to this model).
        decoder_past_key_values (`Cache`, *optional*):
            Pre-computed hidden-states (key and values in the self-attention blocks) that can be used to speed up sequential decoding of the decoder transformer.
            This typically consists in the `past_key_values` returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.

            The model will output the same cache format that is fed as input.

            If `past_key_values` are used, the user can optionally input only the last `audio_values` or `audio_codes (those that don't
            have their past key value states given to this model).
    """
    audio_codes: torch.LongTensor = ...
    audio_values: torch.FloatTensor = ...
    encoder_past_key_values: Optional[Union[Cache, List[torch.FloatTensor]]] = ...
    decoder_past_key_values: Optional[Union[Cache, List[torch.FloatTensor]]] = ...


@dataclass
class MimiEncoderOutput(ModelOutput):
    """
    Args:
        audio_codes (`torch.LongTensor`  of shape `(batch_size, num_quantizers, codes_length)`, *optional*):
            Discret code embeddings computed using `model.encode`.
        encoder_past_key_values (`Cache`, *optional*):
            Pre-computed hidden-states (key and values in the self-attention blocks) that can be used to speed up sequential decoding of the encoder transformer.
            This typically consists in the `past_key_values` returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.

            The model will output the same cache format that is fed as input.

            If `past_key_values` are used, the user can optionally input only the last `audio_values` or `audio_codes (those that don't
            have their past key value states given to this model).
    """
    audio_codes: torch.LongTensor = ...
    encoder_past_key_values: Optional[Union[Cache, List[torch.FloatTensor]]] = ...


@dataclass
class MimiDecoderOutput(ModelOutput):
    """
    Args:
        audio_values (`torch.FloatTensor`  of shape `(batch_size, segment_length)`, *optional*):
            Decoded audio values, obtained using the decoder part of Mimi.
        decoder_past_key_values (`Cache`, *optional*):
            Pre-computed hidden-states (key and values in the self-attention blocks) that can be used to speed up sequential decoding of the decoder transformer.
            This typically consists in the `past_key_values` returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.

            The model will output the same cache format that is fed as input.

            If `past_key_values` are used, the user can optionally input only the last `audio_values` or `audio_codes (those that don't
            have their past key value states given to this model).
    """
    audio_values: torch.FloatTensor = ...
    decoder_past_key_values: Optional[Union[Cache, List[torch.FloatTensor]]] = ...


class MimiConv1d(nn.Module):
    """Conv1d with asymmetric or causal padding and normalization."""
    def __init__(self, config, in_channels: int, out_channels: int, kernel_size: int, stride: int = ..., dilation: int = ..., groups: int = ..., pad_mode=..., bias: bool = ...) -> None:
        ...
    
    def apply_weight_norm(self): # -> None:
        ...
    
    def remove_weight_norm(self): # -> None:
        ...
    
    def forward(self, hidden_states): # -> Any:
        ...
    


class MimiConvTranspose1d(nn.Module):
    """ConvTranspose1d with asymmetric or causal padding and normalization."""
    def __init__(self, config, in_channels: int, out_channels: int, kernel_size: int, stride: int = ..., groups: int = ..., bias=...) -> None:
        ...
    
    def apply_weight_norm(self): # -> None:
        ...
    
    def remove_weight_norm(self): # -> None:
        ...
    
    def forward(self, hidden_states): # -> Any:
        ...
    


class MimiResnetBlock(nn.Module):
    """
    Residual block from SEANet model as used by Mimi.
    """
    def __init__(self, config: MimiConfig, dim: int, dilations: List[int]) -> None:
        ...
    
    def forward(self, hidden_states): # -> Any:
        ...
    


class MimiEncoder(nn.Module):
    """SEANet encoder as used by Mimi."""
    def __init__(self, config: MimiConfig) -> None:
        ...
    
    def forward(self, hidden_states): # -> Any:
        ...
    


class MimiLayerScale(nn.Module):
    """Layer scale from [Touvron et al 2021] (https://arxiv.org/pdf/2103.17239.pdf).
    This rescales diagonally the residual outputs close to 0, with a learnt scale.
    """
    def __init__(self, config) -> None:
        ...
    
    def forward(self, x: torch.Tensor): # -> Tensor:
        ...
    


class MimiRotaryEmbedding(nn.Module):
    def __init__(self, dim, max_position_embeddings=..., base=..., device=...) -> None:
        ...
    
    @torch.no_grad()
    def forward(self, x, position_ids): # -> tuple[Tensor, Tensor]:
        ...
    


def rotate_half(x): # -> Tensor:
    """Rotates half the hidden dims of the input."""
    ...

def apply_rotary_pos_emb(q, k, cos, sin, position_ids=..., unsqueeze_dim=...): # -> tuple[Any, Any]:
    """Applies Rotary Position Embedding to the query and key tensors.

    Args:
        q (`torch.Tensor`): The query tensor.
        k (`torch.Tensor`): The key tensor.
        cos (`torch.Tensor`): The cosine part of the rotary embedding.
        sin (`torch.Tensor`): The sine part of the rotary embedding.
        position_ids (`torch.Tensor`, *optional*):
            Deprecated and unused.
        unsqueeze_dim (`int`, *optional*, defaults to 1):
            The 'unsqueeze_dim' argument specifies the dimension along which to unsqueeze cos[position_ids] and
            sin[position_ids] so that they can be properly broadcasted to the dimensions of q and k. For example, note
            that cos[position_ids] and sin[position_ids] have the shape [batch_size, seq_len, head_dim]. Then, if q and
            k have the shape [batch_size, heads, seq_len, head_dim], then setting unsqueeze_dim=1 makes
            cos[position_ids] and sin[position_ids] broadcastable to the shapes of q and k. Similarly, if q and k have
            the shape [batch_size, seq_len, heads, head_dim], then set unsqueeze_dim=2.
    Returns:
        `tuple(torch.Tensor)` comprising of the query and key tensors rotated using the Rotary Position Embedding.
    """
    ...

class MimiMLP(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
        ...
    


def repeat_kv(hidden_states: torch.Tensor, n_rep: int) -> torch.Tensor:
    """
    This is the equivalent of torch.repeat_interleave(x, dim=1, repeats=n_rep). The hidden states go from (batch,
    num_key_value_heads, seqlen, head_dim) to (batch, num_attention_heads, seqlen, head_dim)
    """
    ...

class MimiAttention(nn.Module):
    """Multi-headed attention from 'Attention Is All You Need' paper"""
    def __init__(self, config: MimiConfig, layer_idx: Optional[int] = ...) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = ..., position_ids: Optional[torch.LongTensor] = ..., past_key_value: Optional[Cache] = ..., output_attentions: bool = ..., use_cache: bool = ..., cache_position: Optional[torch.LongTensor] = ...) -> Tuple[torch.Tensor, Optional[torch.Tensor], Optional[Tuple[torch.Tensor]]]:
        ...
    


class MimiFlashAttention2(MimiAttention):
    """
    Mimi flash attention module. This module inherits from `MimiAttention` as the weights of the module stays
    untouched. The only required change would be on the forward pass where it needs to correctly call the public API of
    flash attention and deal with padding tokens in case the input contains any of them.
    """
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.LongTensor] = ..., position_ids: Optional[torch.LongTensor] = ..., past_key_value: Optional[Cache] = ..., output_attentions: bool = ..., use_cache: bool = ..., cache_position: Optional[torch.LongTensor] = ...) -> Tuple[torch.Tensor, Optional[torch.Tensor], Optional[Tuple[torch.Tensor]]]:
        ...
    


class MimiSdpaAttention(MimiAttention):
    """
    Mimi attention module using torch.nn.functional.scaled_dot_product_attention. This module inherits from
    `MimiAttention` as the weights of the module stays untouched. The only changes are on the forward pass to adapt to
    SDPA API.
    """
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = ..., position_ids: Optional[torch.LongTensor] = ..., past_key_value: Optional[Cache] = ..., output_attentions: bool = ..., use_cache: bool = ..., cache_position: Optional[torch.LongTensor] = ..., **kwargs) -> Tuple[torch.Tensor, Optional[torch.Tensor], Optional[Tuple[torch.Tensor]]]:
        ...
    


MIMI_ATTENTION_CLASSES = ...
class MimiTransformerLayer(nn.Module):
    def __init__(self, config: MimiConfig, layer_idx: int) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = ..., position_ids: Optional[torch.LongTensor] = ..., past_key_value: Optional[Cache] = ..., output_attentions: Optional[bool] = ..., use_cache: Optional[bool] = ..., cache_position: Optional[torch.LongTensor] = ..., **kwargs) -> Tuple[torch.FloatTensor, Optional[Tuple[torch.FloatTensor, torch.FloatTensor]]]:
        """
        Args:
            hidden_states (`torch.FloatTensor`): input to the layer of shape `(batch, seq_len, embed_dim)`
            attention_mask (`torch.FloatTensor`, *optional*):
                attention mask of size `(batch_size, sequence_length)` if flash attention is used or `(batch_size, 1,
                query_sequence_length, key_sequence_length)` if default attention is used.
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
            use_cache (`bool`, *optional*):
                If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding
                (see `past_key_values`).
            past_key_value (`Tuple(torch.FloatTensor)`, *optional*): cached past key and value projection states
            cache_position (`torch.LongTensor` of shape `(sequence_length)`, *optional*):
                Indices depicting the position of the input sequence tokens in the sequence
            kwargs (`dict`, *optional*):
                Arbitrary kwargs to be ignored, used for FSDP and other methods that injects code
                into the model
        """
        ...
    


class MimiTransformerModel(nn.Module):
    """
    Transformer decoder consisting of *config.num_hidden_layers* layers. Each layer is a [`MimiTransformerLayer`]

    Args:
        config: MimiConfig
    """
    def __init__(self, config: MimiConfig) -> None:
        ...
    
    def forward(self, hidden_states: torch.LongTensor = ..., attention_mask: Optional[torch.Tensor] = ..., position_ids: Optional[torch.LongTensor] = ..., past_key_values: Optional[Union[Cache, List[torch.FloatTensor]]] = ..., use_cache: Optional[bool] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., cache_position: Optional[torch.LongTensor] = ...) -> Union[Tuple, BaseModelOutputWithPast]:
        """
        Args:
            hidden_states (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
                Embedded representation that will be contextualized by the model
            attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.

                [What are attention masks?](../glossary#attention-mask)

                Indices can be obtained using [`AutoTokenizer`]. See [`PreTrainedTokenizer.encode`] and
                [`PreTrainedTokenizer.__call__`] for details.

                If `past_key_values` is used, optionally only the last `decoder_input_ids` have to be input (see
                `past_key_values`).

                If you want to change padding behavior, you should read [`modeling_opt._prepare_decoder_attention_mask`]
                and modify to your needs. See diagram 1 in [the paper](https://arxiv.org/abs/1910.13461) for more
                information on the default strategy.

                - 1 indicates the head is **not masked**,
                - 0 indicates the head is **masked**.
            position_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
                Indices of positions of each input sequence tokens in the position embeddings. Selected in the range `[0,
                config.n_positions - 1]`.

                [What are position IDs?](../glossary#position-ids)
            past_key_values (`Cache` or `tuple(tuple(torch.FloatTensor))`, *optional*):
                Pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
                blocks) that can be used to speed up sequential decoding. This typically consists in the `past_key_values`
                returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.

                Two formats are allowed:
                - a [`~cache_utils.Cache`] instance;
                - Tuple of `tuple(torch.FloatTensor)` of length `config.n_layers`, with each tuple having 2 tensors of
                shape `(batch_size, num_heads, sequence_length, embed_size_per_head)`). This is also known as the legacy
                cache format.

                The model will output the same cache format that is fed as input. If no `past_key_values` are passed, the
                legacy cache format will be returned.

                If `past_key_values` are used, the user can optionally input only the last `input_ids` (those that don't
                have their past key value states given to this model) of shape `(batch_size, 1)` instead of all `input_ids`
                of shape `(batch_size, sequence_length)`.
            use_cache (`bool`, *optional*):
                If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
                `past_key_values`).
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under returned
                tensors for more detail.
            output_hidden_states (`bool`, *optional*):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
                more detail.
            return_dict (`bool`, *optional*):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
        """
        ...
    


class MimiDecoder(nn.Module):
    """SEANet decoder as used by Mimi."""
    def __init__(self, config: MimiConfig) -> None:
        ...
    
    def forward(self, hidden_states): # -> Any:
        ...
    


class MimiEuclideanCodebook(nn.Module):
    """Codebook with Euclidean distance."""
    def __init__(self, config: MimiConfig, epsilon: float = ...) -> None:
        ...
    
    @property
    def embed(self) -> torch.Tensor:
        ...
    
    def quantize(self, hidden_states): # -> Tensor:
        ...
    
    def encode(self, hidden_states): # -> Tensor:
        ...
    
    def decode(self, embed_ind): # -> Tensor:
        ...
    


class MimiVectorQuantization(nn.Module):
    """
    Vector quantization implementation. Currently supports only euclidean distance.
    """
    def __init__(self, config: MimiConfig) -> None:
        ...
    
    def encode(self, hidden_states): # -> Tensor:
        ...
    
    def decode(self, embed_ind): # -> Tensor:
        ...
    


class MimiResidualVectorQuantizer(nn.Module):
    """Residual Vector Quantizer."""
    def __init__(self, config: MimiConfig, num_quantizers: int = ...) -> None:
        ...
    
    def encode(self, embeddings: torch.Tensor, num_quantizers: Optional[int] = ...) -> torch.Tensor:
        """
        Encode a given input tensor with the specified frame rate at the given number of quantizers / codebooks. The RVQ encode method sets
        the appropriate number of quantizers to use and returns indices for each quantizer.
        """
        ...
    
    def decode(self, codes: torch.Tensor) -> torch.Tensor:
        """Decode the given codes of shape [B, K, T] to the quantized representation."""
        ...
    


class MimiSplitResidualVectorQuantizer(nn.Module):
    """Split Residual Vector Quantizer."""
    def __init__(self, config: MimiConfig) -> None:
        ...
    
    def encode(self, embeddings: torch.Tensor, num_quantizers: Optional[float] = ...) -> torch.Tensor:
        """
        Encode a given input tensor with the specified frame rate at the given number of quantizers / codebooks. The RVQ encode method sets
        the appropriate number of quantizers to use and returns indices for each quantizer.
        """
        ...
    
    def decode(self, codes: torch.Tensor) -> torch.Tensor:
        """Decode the given codes to the quantized representation."""
        ...
    


class MimiPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = MimiConfig
    base_model_prefix = ...
    main_input_name = ...
    supports_gradient_checkpointing = ...
    _no_split_modules = ...
    _skip_keys_device_placement = ...
    _supports_flash_attn_2 = ...
    _supports_sdpa = ...
    _supports_cache_class = ...
    _supports_static_cache = ...


MIMI_START_DOCSTRING = ...
MIMI_INPUTS_DOCSTRING = ...
@add_start_docstrings("The Mimi neural audio codec model.", MIMI_START_DOCSTRING)
class MimiModel(MimiPreTrainedModel):
    def __init__(self, config: MimiConfig) -> None:
        ...
    
    def get_encoder(self): # -> MimiEncoder:
        ...
    
    def get_decoder(self): # -> MimiDecoder:
        ...
    
    def encode(self, input_values: torch.Tensor, padding_mask: torch.Tensor = ..., num_quantizers: Optional[float] = ..., encoder_past_key_values: Optional[Union[Cache, List[torch.FloatTensor]]] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple[torch.Tensor, Optional[torch.Tensor]], MimiEncoderOutput]:
        """
        Encodes the input audio waveform into discrete codes.

        Args:
            input_values (`torch.Tensor` of shape `(batch_size, channels, sequence_length)`):
                Float values of the input audio waveform.
            padding_mask (`torch.Tensor` of shape `(batch_size, channels, sequence_length)`):
                Indicates which inputs are to be ignored due to padding, where elements are either 1 for *not masked* or 0
                for *masked*.
            num_quantizers (`int`, *optional*):
                Number of quantizers (i.e codebooks) to use. By default, all quantizers are used.
            encoder_past_key_values (`Cache`, *optional*):
                Pre-computed hidden-states (key and values in the self-attention blocks) that can be used to speed up sequential decoding of the encoder transformer.
                This typically consists in the `past_key_values` returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.

                The model will output the same cache format that is fed as input.

                If `past_key_values` are used, the user can optionally input only the last `audio_values` or `audio_codes (those that don't
                have their past key value states given to this model).
            return_dict (`bool`, *optional*):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.

        Returns:
            `codebook` of shape `[batch_size, num_codebooks, frames]`, the discrete encoded codes for the input audio waveform.
        """
        ...
    
    def decode(self, audio_codes: torch.Tensor, padding_mask: Optional[torch.Tensor] = ..., decoder_past_key_values: Optional[Union[Cache, List[torch.FloatTensor]]] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple[torch.Tensor, torch.Tensor], MimiDecoderOutput]:
        """
        Decodes the given frames into an output audio waveform.

        Note that the output might be a bit bigger than the input. In that case, any extra steps at the end can be
        trimmed.

        Args:
            audio_codes (`torch.LongTensor`  of shape `(batch_size, num_quantizers, codes_length)`, *optional*):
                Discret code embeddings computed using `model.encode`.
            padding_mask (`torch.Tensor` of shape `(batch_size, channels, sequence_length)`):
                Indicates which inputs are to be ignored due to padding, where elements are either 1 for *not masked* or 0
                for *masked*.
            decoder_past_key_values (`Cache`, *optional*):
                Pre-computed hidden-states (key and values in the self-attention blocks) that can be used to speed up sequential decoding of the decoder transformer.
                This typically consists in the `past_key_values` returned by the model at a previous stage of decoding, when `use_cache=True` or `config.use_cache=True`.

                The model will output the same cache format that is fed as input.

                If `past_key_values` are used, the user can optionally input only the last `audio_values` or `audio_codes (those that don't
                have their past key value states given to this model).
            return_dict (`bool`, *optional*):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.

        """
        ...
    
    @add_start_docstrings_to_model_forward(MIMI_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=MimiOutput, config_class=_CONFIG_FOR_DOC)
    def forward(self, input_values: torch.Tensor, padding_mask: Optional[torch.Tensor] = ..., num_quantizers: Optional[int] = ..., audio_codes: Optional[torch.Tensor] = ..., encoder_past_key_values: Optional[Union[Cache, List[torch.FloatTensor]]] = ..., decoder_past_key_values: Optional[Union[Cache, List[torch.FloatTensor]]] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple[torch.Tensor, torch.Tensor], MimiOutput]:
        r"""
        Returns:

        Examples:

        ```python
        >>> from datasets import load_dataset
        >>> from transformers import AutoFeatureExtractor, MimiModel

        >>> dataset = load_dataset("hf-internal-testing/ashraq-esc50-1-dog-example")
        >>> audio_sample = dataset["train"]["audio"][0]["array"]

        >>> model_id = "kyutai/mimi"
        >>> model = MimiModel.from_pretrained(model_id)
        >>> feature_extractor = AutoFeatureExtractor.from_pretrained(model_id)

        >>> inputs = feature_extractor(raw_audio=audio_sample, return_tensors="pt")

        >>> outputs = model(**inputs)
        >>> audio_codes = outputs.audio_codes
        >>> audio_values = outputs.audio_values
        ```"""
        ...
    


