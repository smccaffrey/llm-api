"""
This type stub file was generated by pyright.
"""

import torch
from typing import List, Optional, Tuple, Union
from torch import nn
from ...generation import GenerationMixin
from ...modeling_outputs import BaseModelOutputWithPastAndCrossAttentions, CausalLMOutputWithCrossAttentions, SequenceClassifierOutputWithPast, TokenClassifierOutput
from ...modeling_utils import PreTrainedModel
from ...utils import add_code_sample_docstrings, add_start_docstrings, add_start_docstrings_to_model_forward, is_flash_attn_2_available
from .configuration_gpt_bigcode import GPTBigCodeConfig

"""PyTorch GPTBigCode model."""
if is_flash_attn_2_available():
    ...
logger = ...
_CHECKPOINT_FOR_DOC = ...
_CONFIG_FOR_DOC = ...
@torch.jit.script
def upcast_masked_softmax(x: torch.Tensor, mask: torch.Tensor, mask_value: torch.Tensor, scale: float, softmax_dtype: torch.dtype): # -> Tensor:
    ...

@torch.jit.script
def upcast_softmax(x: torch.Tensor, scale: float, softmax_dtype: torch.dtype): # -> Tensor:
    ...

@torch.jit.script
def masked_softmax(x: torch.Tensor, mask: torch.Tensor, mask_value: torch.Tensor): # -> Tensor:
    ...

class GPTBigCodeAttention(nn.Module):
    def __init__(self, config, is_cross_attention=..., layer_idx=...) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor, layer_past: Optional[torch.Tensor] = ..., attention_mask: Optional[torch.Tensor] = ..., head_mask: Optional[torch.Tensor] = ..., encoder_hidden_states: Optional[torch.Tensor] = ..., encoder_attention_mask: Optional[torch.Tensor] = ..., use_cache: Optional[bool] = ..., output_attentions: Optional[bool] = ...) -> Union[Tuple[torch.Tensor, Optional[torch.Tensor]], Tuple[torch.Tensor, Optional[torch.Tensor], Tuple[torch.Tensor, ...]],]:
        ...
    


class GPTBigCodeFlashAttention2(GPTBigCodeAttention):
    """
    GPTBigCode flash attention module. This module inherits from `GPTBigCodeAttention` as the weights of the module
    stays untouched. The only required change would be on the forward pass where it needs to correctly call the public
    API of flash attention and deal with padding tokens in case the input contains any of them.
    """
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor, layer_past: Optional[torch.Tensor] = ..., attention_mask: Optional[torch.Tensor] = ..., head_mask: Optional[torch.Tensor] = ..., encoder_hidden_states: Optional[torch.Tensor] = ..., encoder_attention_mask: Optional[torch.Tensor] = ..., use_cache: Optional[bool] = ..., output_attentions: Optional[bool] = ...) -> Union[Tuple[torch.Tensor, Optional[torch.Tensor]], Tuple[torch.Tensor, Optional[torch.Tensor], Tuple[torch.Tensor, ...]],]:
        ...
    


class GPTBigCodeSdpaAttention(GPTBigCodeAttention):
    def forward(self, hidden_states: torch.Tensor, layer_past: Optional[torch.Tensor] = ..., attention_mask: Optional[torch.Tensor] = ..., head_mask: Optional[torch.Tensor] = ..., encoder_hidden_states: Optional[torch.Tensor] = ..., encoder_attention_mask: Optional[torch.Tensor] = ..., use_cache: Optional[bool] = ..., output_attentions: Optional[bool] = ...) -> Union[Tuple[torch.Tensor, Optional[torch.Tensor]], Tuple[torch.Tensor, Optional[torch.Tensor], Tuple[torch.Tensor, ...]],]:
        ...
    


class GPTBigCodeMLP(nn.Module):
    def __init__(self, intermediate_size, config) -> None:
        ...
    
    def forward(self, hidden_states: Optional[Tuple[torch.FloatTensor]]) -> torch.FloatTensor:
        ...
    


GPTBIGCODE_ATTENTION_CLASSES = ...
class GPTBigCodeBlock(nn.Module):
    def __init__(self, config, layer_idx=...) -> None:
        ...
    
    def forward(self, hidden_states: Optional[Tuple[torch.Tensor]], layer_past: Optional[torch.Tensor] = ..., attention_mask: Optional[torch.Tensor] = ..., head_mask: Optional[torch.Tensor] = ..., encoder_hidden_states: Optional[torch.Tensor] = ..., encoder_attention_mask: Optional[torch.Tensor] = ..., use_cache: Optional[bool] = ..., output_attentions: Optional[bool] = ..., **kwargs) -> Union[Tuple[torch.Tensor], Tuple[torch.Tensor, torch.Tensor], Tuple[torch.Tensor, torch.Tensor, torch.Tensor]]:
        ...
    


class GPTBigCodePreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = GPTBigCodeConfig
    base_model_prefix = ...
    supports_gradient_checkpointing = ...
    _no_split_modules = ...
    _skip_keys_device_placement = ...
    _supports_flash_attn_2 = ...
    _supports_sdpa = ...
    def __init__(self, *inputs, **kwargs) -> None:
        ...
    


GPT_BIGCODE_START_DOCSTRING = ...
GPT_BIGCODE_INPUTS_DOCSTRING = ...
@add_start_docstrings("The bare GPT_BIGCODE Model transformer outputting raw hidden-states without any specific head on top.", GPT_BIGCODE_START_DOCSTRING)
class GPTBigCodeModel(GPTBigCodePreTrainedModel):
    def __init__(self, config) -> None:
        ...
    
    def get_input_embeddings(self): # -> Embedding:
        ...
    
    def set_input_embeddings(self, new_embeddings): # -> None:
        ...
    
    @add_start_docstrings_to_model_forward(GPT_BIGCODE_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(checkpoint=_CHECKPOINT_FOR_DOC, output_type=BaseModelOutputWithPastAndCrossAttentions, config_class=_CONFIG_FOR_DOC)
    def forward(self, input_ids: Optional[torch.Tensor] = ..., past_key_values: Optional[List[torch.Tensor]] = ..., attention_mask: Optional[torch.Tensor] = ..., token_type_ids: Optional[torch.Tensor] = ..., position_ids: Optional[torch.Tensor] = ..., head_mask: Optional[torch.Tensor] = ..., inputs_embeds: Optional[torch.Tensor] = ..., encoder_hidden_states: Optional[torch.Tensor] = ..., encoder_attention_mask: Optional[torch.Tensor] = ..., use_cache: Optional[bool] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple, BaseModelOutputWithPastAndCrossAttentions]:
        ...
    


@add_start_docstrings("""
    The GPT_BIGCODE Model transformer with a language modeling head on top (linear layer with weights tied to the input
    embeddings).
    """, GPT_BIGCODE_START_DOCSTRING)
class GPTBigCodeForCausalLM(GPTBigCodePreTrainedModel, GenerationMixin):
    _tied_weights_keys = ...
    def __init__(self, config) -> None:
        ...
    
    def get_output_embeddings(self): # -> Linear:
        ...
    
    def set_output_embeddings(self, new_embeddings): # -> None:
        ...
    
    def prepare_inputs_for_generation(self, input_ids, past_key_values=..., inputs_embeds=..., **kwargs): # -> dict[str, Any]:
        ...
    
    @add_start_docstrings_to_model_forward(GPT_BIGCODE_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(checkpoint=_CHECKPOINT_FOR_DOC, output_type=CausalLMOutputWithCrossAttentions, config_class=_CONFIG_FOR_DOC)
    def forward(self, input_ids: Optional[torch.Tensor] = ..., past_key_values: Optional[Tuple[Tuple[torch.Tensor]]] = ..., attention_mask: Optional[torch.Tensor] = ..., token_type_ids: Optional[torch.Tensor] = ..., position_ids: Optional[torch.Tensor] = ..., head_mask: Optional[torch.Tensor] = ..., inputs_embeds: Optional[torch.Tensor] = ..., encoder_hidden_states: Optional[torch.Tensor] = ..., encoder_attention_mask: Optional[torch.Tensor] = ..., labels: Optional[torch.Tensor] = ..., use_cache: Optional[bool] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple, CausalLMOutputWithCrossAttentions]:
        r"""
        labels (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for language modeling. Note that the labels **are shifted** inside the model, i.e. you can set
            `labels = input_ids` Indices are selected in `[-100, 0, ..., config.vocab_size]` All labels set to `-100`
            are ignored (masked), the loss is only computed for labels in `[0, ..., config.vocab_size]`
        """
        ...
    


@add_start_docstrings("""
    The GPTBigCode Model transformer with a sequence classification head on top (linear layer).

    [`GPTBigCodeForSequenceClassification`] uses the last token in order to do the classification, as other causal
    models (e.g. GPT-1) do.

    Since it does classification on the last token, it requires to know the position of the last token. If a
    `pad_token_id` is defined in the configuration, it finds the last token that is not a padding token in each row. If
    no `pad_token_id` is defined, it simply takes the last value in each row of the batch. Since it cannot guess the
    padding tokens when `inputs_embeds` are passed instead of `input_ids`, it does the same (take the last value in
    each row of the batch).
    """, GPT_BIGCODE_START_DOCSTRING)
class GPTBigCodeForSequenceClassification(GPTBigCodePreTrainedModel):
    def __init__(self, config) -> None:
        ...
    
    @add_start_docstrings_to_model_forward(GPT_BIGCODE_INPUTS_DOCSTRING)
    def forward(self, input_ids: Optional[torch.Tensor] = ..., past_key_values: Optional[Tuple[Tuple[torch.Tensor]]] = ..., attention_mask: Optional[torch.Tensor] = ..., token_type_ids: Optional[torch.Tensor] = ..., position_ids: Optional[torch.Tensor] = ..., head_mask: Optional[torch.Tensor] = ..., inputs_embeds: Optional[torch.Tensor] = ..., labels: Optional[torch.Tensor] = ..., use_cache: Optional[bool] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple, SequenceClassifierOutputWithPast]:
        r"""
        labels (`torch.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
        ...
    


@add_start_docstrings("""
    GPT_BIGCODE Model with a token classification head on top (a linear layer on top of the hidden-states output) e.g.
    for Named-Entity-Recognition (NER) tasks.
    """, GPT_BIGCODE_START_DOCSTRING)
class GPTBigCodeForTokenClassification(GPTBigCodePreTrainedModel):
    def __init__(self, config) -> None:
        ...
    
    @add_start_docstrings_to_model_forward(GPT_BIGCODE_INPUTS_DOCSTRING)
    def forward(self, input_ids: Optional[torch.Tensor] = ..., past_key_values: Optional[Tuple[Tuple[torch.Tensor]]] = ..., attention_mask: Optional[torch.Tensor] = ..., token_type_ids: Optional[torch.Tensor] = ..., position_ids: Optional[torch.Tensor] = ..., head_mask: Optional[torch.Tensor] = ..., inputs_embeds: Optional[torch.Tensor] = ..., labels: Optional[torch.Tensor] = ..., use_cache: Optional[bool] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple, TokenClassifierOutput]:
        r"""
        labels (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
        ...
    


