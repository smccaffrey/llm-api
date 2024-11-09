"""
This type stub file was generated by pyright.
"""

import torch
from typing import List, Optional, Tuple, Union
from torch import nn
from ...cache_utils import Cache
from ...generation import GenerationMixin
from ...modeling_outputs import BaseModelOutputWithPast, CausalLMOutputWithPast
from ...modeling_utils import PreTrainedModel
from ...utils import add_start_docstrings, add_start_docstrings_to_model_forward, is_flash_attn_2_available, replace_return_docstrings
from .configuration_cohere import CohereConfig

"""PyTorch Cohere model."""
if is_flash_attn_2_available():
    ...
logger = ...
_CONFIG_FOR_DOC = ...
class CohereLayerNorm(nn.Module):
    def __init__(self, hidden_size=..., eps=..., bias=...) -> None:
        """The hidden size can be a tuple or an int. The tuple is used for QKNorm to normalize across head_dim"""
        ...
    
    def forward(self, hidden_states):
        ...
    


class CohereRotaryEmbedding(nn.Module):
    def __init__(self, dim=..., max_position_embeddings=..., base=..., device=..., scaling_factor=..., rope_type=..., config: Optional[CohereConfig] = ...) -> None:
        ...
    
    @torch.no_grad()
    def forward(self, x, position_ids): # -> tuple[Any, Any]:
        ...
    


def rotate_half(x): # -> Tensor:
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

class CohereMLP(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def forward(self, x): # -> Any:
        ...
    


def repeat_kv(hidden_states: torch.Tensor, n_rep: int) -> torch.Tensor:
    """
    This is the equivalent of torch.repeat_interleave(x, dim=1, repeats=n_rep). The hidden states go from (batch,
    num_key_value_heads, seqlen, head_dim) to (batch, num_attention_heads, seqlen, head_dim)
    """
    ...

class CohereAttention(nn.Module):
    """Multi-headed attention from 'Attention Is All You Need' paper"""
    def __init__(self, config: CohereConfig, layer_idx: Optional[int] = ...) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = ..., position_ids: Optional[torch.LongTensor] = ..., past_key_value: Optional[Cache] = ..., output_attentions: bool = ..., use_cache: bool = ..., cache_position: Optional[torch.LongTensor] = ..., position_embeddings: Optional[Tuple[torch.Tensor, torch.Tensor]] = ..., **kwargs) -> Tuple[torch.Tensor, Optional[torch.Tensor], Optional[Tuple[torch.Tensor]]]:
        ...
    


class CohereFlashAttention2(CohereAttention):
    """
    Cohere flash attention module. This module inherits from `CohereAttention` as the weights of the module stays
    untouched. The only required change would be on the forward pass where it needs to correctly call the public API of
    flash attention and deal with padding tokens in case the input contains any of them.
    """
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.LongTensor] = ..., position_ids: Optional[torch.LongTensor] = ..., past_key_value: Optional[Cache] = ..., output_attentions: bool = ..., use_cache: bool = ..., cache_position: Optional[torch.LongTensor] = ..., position_embeddings: Optional[Tuple[torch.Tensor, torch.Tensor]] = ..., **kwargs) -> Tuple[torch.Tensor, Optional[torch.Tensor], Optional[Tuple[torch.Tensor]]]:
        ...
    


class CohereSdpaAttention(CohereAttention):
    """
    Cohere attention module using torch.nn.functional.scaled_dot_product_attention. This module inherits from
    `CohereAttention` as the weights of the module stays untouched. The only changes are on the forward pass to adapt to
    SDPA API.
    """
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = ..., position_ids: Optional[torch.LongTensor] = ..., past_key_value: Optional[Cache] = ..., output_attentions: bool = ..., use_cache: bool = ..., cache_position: Optional[torch.LongTensor] = ..., position_embeddings: Optional[Tuple[torch.Tensor, torch.Tensor]] = ...) -> Tuple[torch.Tensor, Optional[torch.Tensor], Optional[Tuple[torch.Tensor]]]:
        ...
    


COHERE_ATTENTION_CLASSES = ...
class CohereDecoderLayer(nn.Module):
    def __init__(self, config: CohereConfig, layer_idx: int) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = ..., position_ids: Optional[torch.LongTensor] = ..., past_key_value: Optional[Tuple[torch.Tensor]] = ..., output_attentions: Optional[bool] = ..., use_cache: Optional[bool] = ..., cache_position: Optional[torch.LongTensor] = ..., position_embeddings: Optional[Tuple[torch.Tensor, torch.Tensor]] = ...) -> Tuple[torch.FloatTensor, Optional[Tuple[torch.FloatTensor, torch.FloatTensor]]]:
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
            position_embeddings (`Tuple[torch.FloatTensor, torch.FloatTensor]`, *optional*):
                Tuple containing the cosine and sine positional embeddings of shape `(batch_size, seq_len, head_dim)`,
                with `head_dim` being the embedding dimension of each attention head.
        """
        ...
    


COHERE_START_DOCSTRING = ...
@add_start_docstrings("The bare Cohere Model outputting raw hidden-states without any specific head on top.", COHERE_START_DOCSTRING)
class CoherePreTrainedModel(PreTrainedModel):
    config_class = CohereConfig
    base_model_prefix = ...
    supports_gradient_checkpointing = ...
    _no_split_modules = ...
    _skip_keys_device_placement = ...
    _supports_flash_attn_2 = ...
    _supports_sdpa = ...
    _supports_cache_class = ...
    _supports_quantized_cache = ...
    _supports_static_cache = ...


COHERE_INPUTS_DOCSTRING = ...
@add_start_docstrings("The bare Cohere Model outputting raw hidden-states without any specific head on top.", COHERE_START_DOCSTRING)
class CohereModel(CoherePreTrainedModel):
    """
    Transformer decoder consisting of *config.num_hidden_layers* layers. Each layer is a [`CohereDecoderLayer`]

    Args:
        config: CohereConfig
    """
    def __init__(self, config: CohereConfig) -> None:
        ...
    
    def get_input_embeddings(self): # -> Embedding | Module:
        ...
    
    def set_input_embeddings(self, value): # -> None:
        ...
    
    @add_start_docstrings_to_model_forward(COHERE_INPUTS_DOCSTRING)
    def forward(self, input_ids: torch.LongTensor = ..., attention_mask: Optional[torch.Tensor] = ..., position_ids: Optional[torch.LongTensor] = ..., past_key_values: Optional[Union[Cache, List[torch.FloatTensor]]] = ..., inputs_embeds: Optional[torch.FloatTensor] = ..., use_cache: Optional[bool] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., cache_position: Optional[torch.LongTensor] = ...) -> Union[Tuple, BaseModelOutputWithPast]:
        ...
    


class CohereForCausalLM(CoherePreTrainedModel, GenerationMixin):
    _tied_weights_keys = ...
    def __init__(self, config) -> None:
        ...
    
    def get_input_embeddings(self): # -> Embedding | Module:
        ...
    
    def set_input_embeddings(self, value): # -> None:
        ...
    
    def get_output_embeddings(self): # -> Linear:
        ...
    
    def set_output_embeddings(self, new_embeddings): # -> None:
        ...
    
    def set_decoder(self, decoder): # -> None:
        ...
    
    def get_decoder(self): # -> CohereModel:
        ...
    
    @add_start_docstrings_to_model_forward(COHERE_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=CausalLMOutputWithPast, config_class=_CONFIG_FOR_DOC)
    def forward(self, input_ids: torch.LongTensor = ..., attention_mask: Optional[torch.Tensor] = ..., position_ids: Optional[torch.LongTensor] = ..., past_key_values: Optional[List[torch.FloatTensor]] = ..., inputs_embeds: Optional[torch.FloatTensor] = ..., labels: Optional[torch.LongTensor] = ..., use_cache: Optional[bool] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., cache_position: Optional[torch.LongTensor] = ..., num_logits_to_keep: int = ..., **loss_kwargs) -> Union[Tuple, CausalLMOutputWithPast]:
        r"""
        Args:
            labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
                Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
                config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
                (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.

            num_logits_to_keep (`int`, *optional*):
                Calculate logits for the last `num_logits_to_keep` tokens. If `0`, calculate logits for all
                `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
                token can save memory, which becomes pretty significant for long sequences or large vocabulary size.

        Returns:

        Example:

        ```python
        >> from transformers import AutoTokenizer, CohereForCausalLM

        >> model = CohereForCausalLM.from_pretrained("CohereForAI/c4ai-command-r-v01")
        >> tokenizer = AutoTokenizer.from_pretrained("CohereForAI/c4ai-command-r-v01")

        >> prompt = "Hey, are you conscious? Can you talk to me?"
        >> inputs = tokenizer(prompt, return_tensors="pt")

        >> # Generate
        >> generate_ids = model.generate(inputs.input_ids, max_length=30)
        >> tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        "Hey, are you conscious? Can you talk to me?\nI'm not conscious, but I can talk to you."
        ```"""
        ...
    

