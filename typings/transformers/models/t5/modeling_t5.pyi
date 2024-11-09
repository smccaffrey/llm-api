"""
This type stub file was generated by pyright.
"""

import torch
from typing import List, Optional, Tuple, Union
from torch import nn
from ...generation import GenerationMixin
from ...modeling_outputs import BaseModelOutput, Seq2SeqLMOutput, Seq2SeqModelOutput, Seq2SeqQuestionAnsweringModelOutput, Seq2SeqSequenceClassifierOutput, TokenClassifierOutput
from ...modeling_utils import PreTrainedModel
from ...utils import add_start_docstrings, add_start_docstrings_to_model_forward, replace_return_docstrings
from .configuration_t5 import T5Config

"""PyTorch T5 model."""
logger = ...
_CONFIG_FOR_DOC = ...
_CHECKPOINT_FOR_DOC = ...
def load_tf_weights_in_t5(model, config, tf_checkpoint_path):
    """Load tf checkpoints in a pytorch model."""
    ...

PARALLELIZE_DOCSTRING = ...
DEPARALLELIZE_DOCSTRING = ...
class T5LayerNorm(nn.Module):
    def __init__(self, hidden_size, eps=...) -> None:
        """
        Construct a layernorm module in the T5 style. No bias and no subtraction of mean.
        """
        ...
    
    def forward(self, hidden_states):
        ...
    


T5LayerNorm = ...
class T5DenseActDense(nn.Module):
    def __init__(self, config: T5Config) -> None:
        ...
    
    def forward(self, hidden_states): # -> Any:
        ...
    


class T5DenseGatedActDense(nn.Module):
    def __init__(self, config: T5Config) -> None:
        ...
    
    def forward(self, hidden_states): # -> Any:
        ...
    


class T5LayerFF(nn.Module):
    def __init__(self, config: T5Config) -> None:
        ...
    
    def forward(self, hidden_states):
        ...
    


class T5Attention(nn.Module):
    def __init__(self, config: T5Config, has_relative_attention_bias=..., layer_idx: Optional[int] = ...) -> None:
        ...
    
    def prune_heads(self, heads): # -> None:
        ...
    
    def compute_bias(self, query_length, key_length, device=..., cache_position=...): # -> Any:
        """Compute binned relative position bias"""
        ...
    
    def forward(self, hidden_states, mask=..., key_value_states=..., position_bias=..., past_key_value=..., layer_head_mask=..., query_length=..., use_cache=..., output_attentions=..., cache_position=...): # -> tuple[Any, Any | None, Any | Tensor, Any | Tensor] | tuple[Any, Any | None, Any | Tensor]:
        """
        Self-attention (if key_value_states is None) or attention over source sentence (provided by key_value_states).
        """
        ...
    


class T5LayerSelfAttention(nn.Module):
    def __init__(self, config, has_relative_attention_bias=..., layer_idx: Optional[int] = ...) -> None:
        ...
    
    def forward(self, hidden_states, attention_mask=..., position_bias=..., layer_head_mask=..., past_key_value=..., use_cache=..., output_attentions=..., cache_position=...): # -> Any:
        ...
    


class T5LayerCrossAttention(nn.Module):
    def __init__(self, config, layer_idx: Optional[int] = ...) -> None:
        ...
    
    def forward(self, hidden_states, key_value_states, attention_mask=..., position_bias=..., layer_head_mask=..., past_key_value=..., use_cache=..., query_length=..., output_attentions=..., cache_position=...): # -> Any:
        ...
    


class T5Block(nn.Module):
    def __init__(self, config, has_relative_attention_bias=..., layer_idx: Optional[int] = ...) -> None:
        ...
    
    def forward(self, hidden_states, attention_mask=..., position_bias=..., encoder_hidden_states=..., encoder_attention_mask=..., encoder_decoder_position_bias=..., layer_head_mask=..., cross_attn_layer_head_mask=..., past_key_value=..., use_cache=..., output_attentions=..., return_dict=..., cache_position=...): # -> Any:
        ...
    


class T5ClassificationHead(nn.Module):
    """Head for sentence-level classification tasks."""
    def __init__(self, config: T5Config) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
        ...
    


class T5PreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = T5Config
    load_tf_weights = ...
    base_model_prefix = ...
    is_parallelizable = ...
    supports_gradient_checkpointing = ...
    _supports_quantized_cache = ...
    _supports_static_cache = ...
    _supports_cache_class = ...
    _no_split_modules = ...
    _keep_in_fp32_modules = ...
    @property
    def dummy_inputs(self): # -> dict[str, Tensor]:
        ...
    


class T5Stack(T5PreTrainedModel):
    def __init__(self, config, embed_tokens=...) -> None:
        ...
    
    @add_start_docstrings(PARALLELIZE_DOCSTRING)
    def parallelize(self, device_map=...): # -> None:
        ...
    
    @add_start_docstrings(DEPARALLELIZE_DOCSTRING)
    def deparallelize(self): # -> None:
        ...
    
    def get_input_embeddings(self): # -> None:
        ...
    
    def set_input_embeddings(self, new_embeddings): # -> None:
        ...
    
    def forward(self, input_ids=..., attention_mask=..., encoder_hidden_states=..., encoder_attention_mask=..., inputs_embeds=..., head_mask=..., cross_attn_head_mask=..., past_key_values=..., use_cache=..., output_attentions=..., output_hidden_states=..., return_dict=..., cache_position=...):
        ...
    


T5_START_DOCSTRING = ...
T5_INPUTS_DOCSTRING = ...
T5_ENCODER_INPUTS_DOCSTRING = ...
__HEAD_MASK_WARNING_MSG = ...
@add_start_docstrings("The bare T5 Model transformer outputting raw hidden-states without any specific head on top.", T5_START_DOCSTRING)
class T5Model(T5PreTrainedModel):
    _keys_to_ignore_on_load_unexpected = ...
    _tied_weights_keys = ...
    def __init__(self, config: T5Config) -> None:
        ...
    
    @add_start_docstrings(PARALLELIZE_DOCSTRING)
    def parallelize(self, device_map=...): # -> None:
        ...
    
    @add_start_docstrings(DEPARALLELIZE_DOCSTRING)
    def deparallelize(self): # -> None:
        ...
    
    def get_input_embeddings(self): # -> Embedding:
        ...
    
    def set_input_embeddings(self, new_embeddings): # -> None:
        ...
    
    def get_encoder(self): # -> T5Stack:
        ...
    
    def get_decoder(self): # -> T5Stack:
        ...
    
    @add_start_docstrings_to_model_forward(T5_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=Seq2SeqModelOutput, config_class=_CONFIG_FOR_DOC)
    def forward(self, input_ids: Optional[torch.LongTensor] = ..., attention_mask: Optional[torch.FloatTensor] = ..., decoder_input_ids: Optional[torch.LongTensor] = ..., decoder_attention_mask: Optional[torch.BoolTensor] = ..., head_mask: Optional[torch.FloatTensor] = ..., decoder_head_mask: Optional[torch.FloatTensor] = ..., cross_attn_head_mask: Optional[torch.Tensor] = ..., encoder_outputs: Optional[Tuple[Tuple[torch.FloatTensor]]] = ..., past_key_values: Optional[Tuple[Tuple[torch.FloatTensor]]] = ..., inputs_embeds: Optional[torch.Tensor] = ..., decoder_inputs_embeds: Optional[torch.Tensor] = ..., use_cache: Optional[bool] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., cache_position: Optional[torch.LongTensor] = ...) -> Union[Tuple[torch.FloatTensor], Seq2SeqModelOutput]:
        r"""
        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, T5Model

        >>> tokenizer = AutoTokenizer.from_pretrained("google-t5/t5-small")
        >>> model = T5Model.from_pretrained("google-t5/t5-small")

        >>> input_ids = tokenizer(
        ...     "Studies have been shown that owning a dog is good for you", return_tensors="pt"
        ... ).input_ids  # Batch size 1
        >>> decoder_input_ids = tokenizer("Studies show that", return_tensors="pt").input_ids  # Batch size 1

        >>> # preprocess: Prepend decoder_input_ids with start token which is pad token for T5Model.
        >>> # This is not needed for torch's T5ForConditionalGeneration as it does this internally using labels arg.
        >>> decoder_input_ids = model._shift_right(decoder_input_ids)

        >>> # forward pass
        >>> outputs = model(input_ids=input_ids, decoder_input_ids=decoder_input_ids)
        >>> last_hidden_states = outputs.last_hidden_state
        ```"""
        ...
    


@add_start_docstrings("""T5 Model with a `language modeling` head on top.""", T5_START_DOCSTRING)
class T5ForConditionalGeneration(T5PreTrainedModel, GenerationMixin):
    _keys_to_ignore_on_load_unexpected = ...
    _tied_weights_keys = ...
    def __init__(self, config: T5Config) -> None:
        ...
    
    @add_start_docstrings(PARALLELIZE_DOCSTRING)
    def parallelize(self, device_map=...): # -> None:
        ...
    
    @add_start_docstrings(DEPARALLELIZE_DOCSTRING)
    def deparallelize(self): # -> None:
        ...
    
    def get_input_embeddings(self): # -> Embedding:
        ...
    
    def set_input_embeddings(self, new_embeddings): # -> None:
        ...
    
    def set_output_embeddings(self, new_embeddings): # -> None:
        ...
    
    def get_output_embeddings(self): # -> Linear:
        ...
    
    def get_encoder(self): # -> T5Stack:
        ...
    
    def get_decoder(self): # -> T5Stack:
        ...
    
    @add_start_docstrings_to_model_forward(T5_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=Seq2SeqLMOutput, config_class=_CONFIG_FOR_DOC)
    def forward(self, input_ids: Optional[torch.LongTensor] = ..., attention_mask: Optional[torch.FloatTensor] = ..., decoder_input_ids: Optional[torch.LongTensor] = ..., decoder_attention_mask: Optional[torch.BoolTensor] = ..., head_mask: Optional[torch.FloatTensor] = ..., decoder_head_mask: Optional[torch.FloatTensor] = ..., cross_attn_head_mask: Optional[torch.Tensor] = ..., encoder_outputs: Optional[Tuple[Tuple[torch.Tensor]]] = ..., past_key_values: Optional[Tuple[Tuple[torch.Tensor]]] = ..., inputs_embeds: Optional[torch.FloatTensor] = ..., decoder_inputs_embeds: Optional[torch.FloatTensor] = ..., labels: Optional[torch.LongTensor] = ..., use_cache: Optional[bool] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., cache_position: Optional[torch.LongTensor] = ...) -> Union[Tuple[torch.FloatTensor], Seq2SeqLMOutput]:
        r"""
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[-100, 0, ...,
            config.vocab_size - 1]`. All labels set to `-100` are ignored (masked), the loss is only computed for
            labels in `[0, ..., config.vocab_size]`

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, T5ForConditionalGeneration

        >>> tokenizer = AutoTokenizer.from_pretrained("google-t5/t5-small")
        >>> model = T5ForConditionalGeneration.from_pretrained("google-t5/t5-small")

        >>> # training
        >>> input_ids = tokenizer("The <extra_id_0> walks in <extra_id_1> park", return_tensors="pt").input_ids
        >>> labels = tokenizer("<extra_id_0> cute dog <extra_id_1> the <extra_id_2>", return_tensors="pt").input_ids
        >>> outputs = model(input_ids=input_ids, labels=labels)
        >>> loss = outputs.loss
        >>> logits = outputs.logits

        >>> # inference
        >>> input_ids = tokenizer(
        ...     "summarize: studies have shown that owning a dog is good for you", return_tensors="pt"
        ... ).input_ids  # Batch size 1
        >>> outputs = model.generate(input_ids)
        >>> print(tokenizer.decode(outputs[0], skip_special_tokens=True))
        >>> # studies have shown that owning a dog is good for you.
        ```"""
        ...
    
    def prepare_decoder_input_ids_from_labels(self, labels: torch.Tensor): # -> Tensor:
        ...
    


@add_start_docstrings("The bare T5 Model transformer outputting encoder's raw hidden-states without any specific head on top.", T5_START_DOCSTRING)
class T5EncoderModel(T5PreTrainedModel):
    _tied_weights_keys = ...
    _keys_to_ignore_on_load_unexpected = ...
    def __init__(self, config: T5Config) -> None:
        ...
    
    @add_start_docstrings(PARALLELIZE_DOCSTRING)
    def parallelize(self, device_map=...): # -> None:
        ...
    
    @add_start_docstrings(DEPARALLELIZE_DOCSTRING)
    def deparallelize(self): # -> None:
        ...
    
    def get_input_embeddings(self): # -> Embedding:
        ...
    
    def set_input_embeddings(self, new_embeddings): # -> None:
        ...
    
    def get_encoder(self): # -> T5Stack:
        ...
    
    @add_start_docstrings_to_model_forward(T5_ENCODER_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=BaseModelOutput, config_class=_CONFIG_FOR_DOC)
    def forward(self, input_ids: Optional[torch.LongTensor] = ..., attention_mask: Optional[torch.FloatTensor] = ..., head_mask: Optional[torch.FloatTensor] = ..., inputs_embeds: Optional[torch.FloatTensor] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple[torch.FloatTensor], BaseModelOutput]:
        r"""
        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, T5EncoderModel

        >>> tokenizer = AutoTokenizer.from_pretrained("google-t5/t5-small")
        >>> model = T5EncoderModel.from_pretrained("google-t5/t5-small")
        >>> input_ids = tokenizer(
        ...     "Studies have been shown that owning a dog is good for you", return_tensors="pt"
        ... ).input_ids  # Batch size 1
        >>> outputs = model(input_ids=input_ids)
        >>> last_hidden_states = outputs.last_hidden_state
        ```"""
        ...
    


@add_start_docstrings("""
    T5 model with a sequence classification/head on top (a linear layer on top of the pooled output) e.g. for GLUE
    tasks.
    """, T5_START_DOCSTRING)
class T5ForSequenceClassification(T5PreTrainedModel):
    _keys_to_ignore_on_load_unexpected = ...
    _tied_weights_keys = ...
    def __init__(self, config: T5Config) -> None:
        ...
    
    @add_start_docstrings_to_model_forward(T5_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=Seq2SeqSequenceClassifierOutput, config_class=_CONFIG_FOR_DOC)
    def forward(self, input_ids: torch.LongTensor = ..., attention_mask: Optional[torch.Tensor] = ..., decoder_input_ids: Optional[torch.LongTensor] = ..., decoder_attention_mask: Optional[torch.LongTensor] = ..., head_mask: Optional[torch.Tensor] = ..., decoder_head_mask: Optional[torch.Tensor] = ..., cross_attn_head_mask: Optional[torch.Tensor] = ..., encoder_outputs: Optional[List[torch.FloatTensor]] = ..., inputs_embeds: Optional[torch.FloatTensor] = ..., decoder_inputs_embeds: Optional[torch.FloatTensor] = ..., labels: Optional[torch.LongTensor] = ..., use_cache: Optional[bool] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple, Seq2SeqSequenceClassifierOutput]:
        r"""
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        Returns:
        """
        ...
    


@add_start_docstrings("""
    T5 Encoder Model with a token classification head on top (a linear layer on top of the hidden-states output)
    e.g. for Named-Entity-Recognition (NER) tasks.
    """, T5_START_DOCSTRING)
class T5ForTokenClassification(T5PreTrainedModel):
    _tied_weights_keys = ...
    def __init__(self, config: T5Config) -> None:
        ...
    
    @add_start_docstrings_to_model_forward(T5_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=TokenClassifierOutput, config_class=_CONFIG_FOR_DOC)
    def forward(self, input_ids: Optional[torch.Tensor] = ..., attention_mask: Optional[torch.Tensor] = ..., head_mask: Optional[torch.Tensor] = ..., inputs_embeds: Optional[torch.Tensor] = ..., labels: Optional[torch.Tensor] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple[torch.Tensor], TokenClassifierOutput]:
        r"""
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.
        Returns:
        """
        ...
    


@add_start_docstrings("""
    T5 Model with a span classification head on top for extractive question-answering tasks like SQuAD (linear layers
    on top of the hidden-states output to compute `span start logits` and `span end logits`).
    """, T5_START_DOCSTRING)
class T5ForQuestionAnswering(T5PreTrainedModel):
    _keys_to_ignore_on_load_unexpected = ...
    _tied_weights_keys = ...
    def __init__(self, config: T5Config) -> None:
        ...
    
    def get_input_embeddings(self): # -> Embedding:
        ...
    
    def set_input_embeddings(self, new_embeddings): # -> None:
        ...
    
    def get_encoder(self): # -> T5Stack:
        ...
    
    def get_decoder(self): # -> T5Stack:
        ...
    
    @add_start_docstrings_to_model_forward(T5_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=Seq2SeqQuestionAnsweringModelOutput, config_class=_CONFIG_FOR_DOC)
    def forward(self, input_ids: Optional[torch.LongTensor] = ..., attention_mask: Optional[torch.FloatTensor] = ..., decoder_input_ids: Optional[torch.LongTensor] = ..., decoder_attention_mask: Optional[torch.BoolTensor] = ..., head_mask: Optional[torch.FloatTensor] = ..., decoder_head_mask: Optional[torch.FloatTensor] = ..., cross_attn_head_mask: Optional[torch.Tensor] = ..., encoder_outputs: Optional[Tuple[Tuple[torch.Tensor]]] = ..., start_positions: Optional[torch.LongTensor] = ..., end_positions: Optional[torch.LongTensor] = ..., inputs_embeds: Optional[torch.FloatTensor] = ..., decoder_inputs_embeds: Optional[torch.FloatTensor] = ..., use_cache: Optional[bool] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple[torch.FloatTensor], Seq2SeqQuestionAnsweringModelOutput]:
        r"""
        start_positions (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the start of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (*sequence_length*). Position outside of the sequence
            are not taken into account for computing the loss.
        end_positions (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the end of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (*sequence_length*). Position outside of the sequence
            are not taken into account for computing the loss.
        Returns:
        """
        ...
    

