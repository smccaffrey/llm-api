"""
This type stub file was generated by pyright.
"""

import torch
from typing import List, Optional, Tuple, Union
from torch import nn
from ...cache_utils import Cache
from ...generation import GenerationMixin
from ...modeling_outputs import BaseModelOutputWithPast, CausalLMOutputWithPast, SequenceClassifierOutputWithPast, TokenClassifierOutput
from ...modeling_utils import PreTrainedModel
from ...utils import add_code_sample_docstrings, add_start_docstrings, add_start_docstrings_to_model_forward, replace_return_docstrings
from .configuration_gemma import GemmaConfig

_CHECKPOINT_FOR_DOC = ...
class GemmaRMSNorm(nn.Module):
    def __init__(self, dim: int, eps: float = ...) -> None:
        ...
    
    def forward(self, x):
        ...
    
    def extra_repr(self): # -> str:
        ...
    


logger = ...
class GemmaRotaryEmbedding(nn.Module):
    def __init__(self, dim, max_position_embeddings=..., base=..., device=...) -> None:
        ...
    
    @torch.no_grad()
    def forward(self, x, position_ids, seq_len=...): # -> tuple[Tensor, Tensor]:
        ...
    


class GemmaLinearScalingRotaryEmbedding(GemmaRotaryEmbedding):
    """GemmaRotaryEmbedding extended with linear scaling. Credits to the Reddit user /u/kaiokendev"""
    def forward(self, x, position_ids): # -> tuple[Tensor, Tensor]:
        ...
    


class GemmaDynamicNTKScalingRotaryEmbedding(GemmaRotaryEmbedding):
    """GemmaRotaryEmbedding extended with Dynamic NTK scaling. Credits to the Reddit users /u/bloc97 and /u/emozilla"""
    def forward(self, x, position_ids): # -> tuple[Tensor, Tensor]:
        ...
    


class GemmaMLP(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def forward(self, x): # -> Any:
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

def repeat_kv(hidden_states: torch.Tensor, n_rep: int) -> torch.Tensor:
    """
    This is the equivalent of torch.repeat_interleave(x, dim=1, repeats=n_rep). The hidden states go from (batch,
    num_key_value_heads, seqlen, head_dim) to (batch, num_attention_heads, seqlen, head_dim)
    """
    ...

class GemmaAttention(nn.Module):
    """Multi-headed attention from 'Attention Is All You Need' paper"""
    def __init__(self, config: GemmaConfig, layer_idx: Optional[int] = ...) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = ..., position_ids: Optional[torch.LongTensor] = ..., past_key_value: Optional[Cache] = ..., output_attentions: bool = ..., use_cache: bool = ..., cache_position: Optional[torch.LongTensor] = ...) -> Tuple[torch.Tensor, Optional[torch.Tensor], Optional[Tuple[torch.Tensor]]]:
        ...
    


class GemmaSdpaAttention(GemmaAttention):
    """
    Gemma attention module using torch.nn.functional.scaled_dot_product_attention. This module inherits from
    `GemmaAttention` as the weights of the module stays untouched. The only changes are on the forward pass to adapt to
    SDPA API.
    """
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = ..., position_ids: Optional[torch.LongTensor] = ..., past_key_value: Optional[Cache] = ..., output_attentions: bool = ..., use_cache: bool = ..., cache_position: Optional[torch.LongTensor] = ..., **kwargs) -> Tuple[torch.Tensor, Optional[torch.Tensor], Optional[Tuple[torch.Tensor]]]:
        ...
    


class GemmaFlashAttention2(GemmaAttention):
    """
    Gemma flash attention module. This module inherits from `GemmaAttention` as the weights of the module stays
    untouched. The only required change would be on the forward pass where it needs to correctly call the public API of
    flash attention and deal with padding tokens in case the input contains any of them.
    """
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.LongTensor] = ..., position_ids: Optional[torch.LongTensor] = ..., past_key_value: Optional[Cache] = ..., output_attentions: bool = ..., use_cache: bool = ..., cache_position: Optional[torch.LongTensor] = ...) -> Tuple[torch.Tensor, Optional[torch.Tensor], Optional[Tuple[torch.Tensor]]]:
        ...
    


GEMMA_ATTENTION_CLASSES = ...
class GemmaDecoderLayer(nn.Module):
    def __init__(self, config: GemmaConfig, layer_idx: int) -> None:
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
    


GEMMA_START_DOCSTRING = ...
@add_start_docstrings("The bare Gemma Model outputting raw hidden-states without any specific head on top.", GEMMA_START_DOCSTRING)
class GemmaPreTrainedModel(PreTrainedModel):
    config_class = GemmaConfig
    base_model_prefix = ...
    supports_gradient_checkpointing = ...
    _no_split_modules = ...
    _skip_keys_device_placement = ...
    _supports_flash_attn_2 = ...
    _supports_sdpa = ...
    _supports_cache_class = ...
    _supports_quantized_cache = ...
    _supports_static_cache = ...


_CONFIG_FOR_DOC = ...
GEMMA_INPUTS_DOCSTRING = ...
@add_start_docstrings("The bare Gemma Model outputting raw hidden-states without any specific head on top.", GEMMA_START_DOCSTRING)
class GemmaModel(GemmaPreTrainedModel):
    """
    Transformer decoder consisting of *config.num_hidden_layers* layers. Each layer is a [`GemmaDecoderLayer`]

    Args:
        config: GemmaConfig
    """
    def __init__(self, config: GemmaConfig) -> None:
        ...
    
    def get_input_embeddings(self): # -> Embedding | Module:
        ...
    
    def set_input_embeddings(self, value): # -> None:
        ...
    
    @add_start_docstrings_to_model_forward(GEMMA_INPUTS_DOCSTRING)
    def forward(self, input_ids: torch.LongTensor = ..., attention_mask: Optional[torch.Tensor] = ..., position_ids: Optional[torch.LongTensor] = ..., past_key_values: Optional[Union[Cache, List[torch.FloatTensor]]] = ..., inputs_embeds: Optional[torch.FloatTensor] = ..., use_cache: Optional[bool] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., cache_position: Optional[torch.LongTensor] = ...) -> Union[Tuple, BaseModelOutputWithPast]:
        ...
    


class GemmaForCausalLM(GemmaPreTrainedModel, GenerationMixin):
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
    
    def get_decoder(self): # -> GemmaModel:
        ...
    
    @add_start_docstrings_to_model_forward(GEMMA_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=CausalLMOutputWithPast, config_class=_CONFIG_FOR_DOC)
    def forward(self, input_ids: torch.LongTensor = ..., attention_mask: Optional[torch.Tensor] = ..., position_ids: Optional[torch.LongTensor] = ..., past_key_values: Optional[Union[Cache, List[torch.FloatTensor]]] = ..., inputs_embeds: Optional[torch.FloatTensor] = ..., labels: Optional[torch.LongTensor] = ..., use_cache: Optional[bool] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., cache_position: Optional[torch.LongTensor] = ..., num_logits_to_keep: int = ..., **loss_kwargs) -> Union[Tuple, CausalLMOutputWithPast]:
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
        >>> from transformers import AutoTokenizer, GemmaForCausalLM

        >>> model = GemmaForCausalLM.from_pretrained("google/gemma-7b")
        >>> tokenizer = AutoTokenizer.from_pretrained("google/gemma-7b")

        >>> prompt = "What is your favorite condiment?"
        >>> inputs = tokenizer(prompt, return_tensors="pt")

        >>> # Generate
        >>> generate_ids = model.generate(inputs.input_ids, max_length=30)
        >>> tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        "What is your favorite condiment?"
        ```"""
        ...
    


@add_start_docstrings("""
    The Gemma Model transformer with a sequence classification head on top (linear layer).

    [`GemmaForSequenceClassification`] uses the last token in order to do the classification, as other causal models
    (e.g. GPT-2) do.

    Since it does classification on the last token, it requires to know the position of the last token. If a
    `pad_token_id` is defined in the configuration, it finds the last token that is not a padding token in each row. If
    no `pad_token_id` is defined, it simply takes the last value in each row of the batch. Since it cannot guess the
    padding tokens when `inputs_embeds` are passed instead of `input_ids`, it does the same (take the last value in
    each row of the batch).
    """, GEMMA_START_DOCSTRING)
class GemmaForSequenceClassification(GemmaPreTrainedModel):
    def __init__(self, config) -> None:
        ...
    
    def get_input_embeddings(self): # -> Embedding | Module:
        ...
    
    def set_input_embeddings(self, value): # -> None:
        ...
    
    @add_start_docstrings_to_model_forward(GEMMA_INPUTS_DOCSTRING)
    def forward(self, input_ids: Optional[torch.LongTensor] = ..., attention_mask: Optional[torch.Tensor] = ..., position_ids: Optional[torch.LongTensor] = ..., past_key_values: Optional[Union[Cache, List[torch.FloatTensor]]] = ..., inputs_embeds: Optional[torch.FloatTensor] = ..., labels: Optional[torch.LongTensor] = ..., use_cache: Optional[bool] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple, SequenceClassifierOutputWithPast]:
        r"""
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
        ...
    


@add_start_docstrings("""
    The Gemma Model transformer with a token classification head on top (a linear layer on top of the hidden-states
    output) e.g. for Named-Entity-Recognition (NER) tasks.
    """, GEMMA_START_DOCSTRING)
class GemmaForTokenClassification(GemmaPreTrainedModel):
    def __init__(self, config) -> None:
        ...
    
    def get_input_embeddings(self): # -> Embedding | Module:
        ...
    
    def set_input_embeddings(self, value): # -> None:
        ...
    
    @add_start_docstrings_to_model_forward(GEMMA_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(checkpoint=_CHECKPOINT_FOR_DOC, output_type=TokenClassifierOutput, config_class=_CONFIG_FOR_DOC)
    def forward(self, input_ids: Optional[torch.LongTensor] = ..., attention_mask: Optional[torch.Tensor] = ..., position_ids: Optional[torch.LongTensor] = ..., past_key_values: Optional[List[torch.FloatTensor]] = ..., inputs_embeds: Optional[torch.FloatTensor] = ..., labels: Optional[torch.LongTensor] = ..., use_cache: Optional[bool] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple, TokenClassifierOutput]:
        r"""
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
        ...
    


__all__ = ["GemmaModel", "GemmaForCausalLM", "GemmaForSequenceClassification", "GemmaForTokenClassification"]
