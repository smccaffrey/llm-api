"""
This type stub file was generated by pyright.
"""

import numpy as np
import tensorflow as tf
from dataclasses import dataclass
from typing import List, Optional, Tuple, Union
from ....modeling_tf_utils import TFModelInputType, TFPreTrainedModel, TFSequenceClassificationLoss, keras, keras_serializable, unpack_inputs
from ....utils import ModelOutput, add_code_sample_docstrings, add_start_docstrings, add_start_docstrings_to_model_forward
from .configuration_transfo_xl import TransfoXLConfig

"""
TF 2.0 Transformer XL model.
"""
logger = ...
_CHECKPOINT_FOR_DOC = ...
_CONFIG_FOR_DOC = ...
class TFPositionalEmbedding(keras.layers.Layer):
    def __init__(self, demb, **kwargs) -> None:
        ...
    
    def call(self, pos_seq, bsz=...):
        ...
    


class TFPositionwiseFF(keras.layers.Layer):
    def __init__(self, d_model, d_inner, dropout, pre_lnorm=..., layer_norm_epsilon=..., init_std=..., **kwargs) -> None:
        ...
    
    def call(self, inp, training=...):
        ...
    


class TFRelPartialLearnableMultiHeadAttn(keras.layers.Layer):
    def __init__(self, n_head, d_model, d_head, dropout, dropatt=..., pre_lnorm=..., r_r_bias=..., r_w_bias=..., layer_norm_epsilon=..., init_std=..., output_attentions=..., **kwargs) -> None:
        ...
    
    def build(self, input_shape): # -> None:
        ...
    
    def call(self, w, r, attn_mask, mems, head_mask, output_attentions, training=...): # -> list[Any]:
        ...
    


class TFRelPartialLearnableDecoderLayer(keras.layers.Layer):
    def __init__(self, n_head, d_model, d_head, d_inner, dropout, dropatt=..., pre_lnorm=..., r_w_bias=..., r_r_bias=..., layer_norm_epsilon=..., init_std=..., output_attentions=..., **kwargs) -> None:
        ...
    
    def call(self, dec_inp, r, dec_attn_mask, mems, head_mask, output_attentions, training=...):
        ...
    


class TFTransfoEmbeddings(keras.layers.Layer):
    def __init__(self, vocab_size, emb_size, init_std, **kwargs) -> None:
        ...
    
    def build(self, input_shape): # -> None:
        ...
    
    def call(self, inputs):
        ...
    


class TFAdaptiveEmbedding(keras.layers.Layer):
    def __init__(self, n_token, d_embed, d_proj, cutoffs, div_val=..., init_std=..., sample_softmax=..., **kwargs) -> None:
        ...
    
    def build(self, input_shape): # -> None:
        ...
    
    def call(self, inp):
        ...
    


@keras_serializable
class TFTransfoXLMainLayer(keras.layers.Layer):
    config_class = TransfoXLConfig
    def __init__(self, config, **kwargs) -> None:
        ...
    
    def build(self, input_shape): # -> None:
        ...
    
    def get_input_embeddings(self): # -> TFAdaptiveEmbedding:
        ...
    
    def set_input_embeddings(self, value):
        ...
    
    def backward_compatible(self): # -> None:
        ...
    
    def reset_memory_length(self, mem_len): # -> None:
        ...
    
    def init_mems(self, bsz): # -> list[Any] | None:
        ...
    
    @unpack_inputs
    def call(self, input_ids: TFModelInputType | None = ..., mems: List[tf.Tensor] | None = ..., head_mask: np.ndarray | tf.Tensor | None = ..., inputs_embeds: np.ndarray | tf.Tensor | None = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., labels: np.ndarray | tf.Tensor | None = ..., training: bool = ...): # -> tuple[Any, ...] | TFTransfoXLModelOutput:
        ...
    


class TFTransfoXLPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = TransfoXLConfig
    base_model_prefix = ...


@dataclass
class TFTransfoXLModelOutput(ModelOutput):
    """
    Base class for model's outputs that may also contain a past key/values (to speed up sequential decoding).

    Args:
        last_hidden_state (`tf.Tensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        mems (`List[tf.Tensor]` of length `config.n_layers`):
            Contains pre-computed hidden-states (key and values in the attention blocks). Can be used (see `mems`
            input) to speed up sequential decoding. The token ids which have their past given to this model should not
            be passed as input ids as they have already been computed.
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    last_hidden_state: tf.Tensor = ...
    mems: List[tf.Tensor] = ...
    hidden_states: Tuple[tf.Tensor] | None = ...
    attentions: Tuple[tf.Tensor] | None = ...


@dataclass
class TFTransfoXLLMHeadModelOutput(ModelOutput):
    """
    Base class for model's outputs that may also contain a past key/values (to speed up sequential decoding).

    Args:
        losses (`tf.Tensor` of shape *(batch_size, sequence_length-1)*, *optional*, returned when `labels` is provided):
            Language modeling losses (not reduced).
        prediction_scores (`tf.Tensor` of shape `(batch_size, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token after SoftMax).
        mems (`List[tf.Tensor]` of length `config.n_layers`):
            Contains pre-computed hidden-states (key and values in the attention blocks). Can be used (see `mems`
            input) to speed up sequential decoding. The token ids which have their past given to this model should not
            be passed as input ids as they have already been computed.
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    prediction_scores: tf.Tensor = ...
    mems: List[tf.Tensor] = ...
    hidden_states: Tuple[tf.Tensor] | None = ...
    attentions: Tuple[tf.Tensor] | None = ...


@dataclass
class TFTransfoXLSequenceClassifierOutputWithPast(ModelOutput):
    """
    Base class for outputs of sentence classification models.

    Args:
        loss (`tf.Tensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Classification (or regression if config.num_labels==1) loss.
        logits (`tf.Tensor` of shape `(batch_size, config.num_labels)`):
            Classification (or regression if config.num_labels==1) scores (before SoftMax).
        mems (`List[tf.Tensor]` of length `config.n_layers`):
            Contains pre-computed hidden-states (key and values in the attention blocks). Can be used (see `mems`
            input) to speed up sequential decoding. The token ids which have their past given to this model should not
            be passed as input ids as they have already been computed.
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    loss: tf.Tensor | None = ...
    logits: tf.Tensor = ...
    mems: List[tf.Tensor] = ...
    hidden_states: Tuple[tf.Tensor] | None = ...
    attentions: Tuple[tf.Tensor] | None = ...


TRANSFO_XL_START_DOCSTRING = ...
TRANSFO_XL_INPUTS_DOCSTRING = ...
@add_start_docstrings("The bare Bert Model transformer outputting raw hidden-states without any specific head on top.", TRANSFO_XL_START_DOCSTRING)
class TFTransfoXLModel(TFTransfoXLPreTrainedModel):
    def __init__(self, config, *inputs, **kwargs) -> None:
        ...
    
    @unpack_inputs
    @add_start_docstrings_to_model_forward(TRANSFO_XL_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(checkpoint=_CHECKPOINT_FOR_DOC, output_type=TFTransfoXLModelOutput, config_class=_CONFIG_FOR_DOC)
    def call(self, input_ids: TFModelInputType | None = ..., mems: List[tf.Tensor] | None = ..., head_mask: np.ndarray | tf.Tensor | None = ..., inputs_embeds: np.ndarray | tf.Tensor | None = ..., output_attentions: bool | None = ..., output_hidden_states: bool | None = ..., return_dict: bool | None = ..., training: bool = ...) -> TFTransfoXLModelOutput | Tuple[tf.Tensor]:
        ...
    


@add_start_docstrings("""
    The Transformer-XL Model with a language modeling head on top (adaptive softmax with weights tied to the adaptive
    input embeddings)
    """, TRANSFO_XL_START_DOCSTRING)
class TFTransfoXLLMHeadModel(TFTransfoXLPreTrainedModel):
    def __init__(self, config) -> None:
        ...
    
    def get_output_embeddings(self): # -> None:
        """Double-check if you are using adaptive softmax."""
        ...
    
    def reset_memory_length(self, mem_len): # -> None:
        ...
    
    def init_mems(self, bsz): # -> list[Any] | None:
        ...
    
    @unpack_inputs
    @add_start_docstrings_to_model_forward(TRANSFO_XL_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(checkpoint=_CHECKPOINT_FOR_DOC, output_type=TFTransfoXLLMHeadModelOutput, config_class=_CONFIG_FOR_DOC)
    def call(self, input_ids: TFModelInputType | None = ..., mems: List[tf.Tensor] | None = ..., head_mask: np.ndarray | tf.Tensor | None = ..., inputs_embeds: np.ndarray | tf.Tensor | None = ..., output_attentions: bool | None = ..., output_hidden_states: bool | None = ..., return_dict: bool | None = ..., labels: np.ndarray | tf.Tensor | None = ..., training: bool = ...) -> TFTransfoXLLMHeadModelOutput | Tuple[tf.Tensor]:
        ...
    
    def prepare_inputs_for_generation(self, input_ids, past_key_values=..., **model_kwargs): # -> dict[Any, Any]:
        ...
    
    def tf_to_pt_weight_rename(self, tf_weight): # -> tuple[Any, Any] | tuple[Any] | None:
        ...
    


@add_start_docstrings("""
    The Transfo XL Model transformer with a sequence classification head on top (linear layer).

    [`TFTransfoXLForSequenceClassification`] uses the last token in order to do the classification, as other causal
    models (e.g. GPT-1,GPT-2) do.

    Since it does classification on the last token, it requires to know the position of the last token. If a
    `pad_token_id` is defined in the configuration, it finds the last token that is not a padding token in each row. If
    no `pad_token_id` is defined, it simply takes the last value in each row of the batch. Since it cannot guess the
    padding tokens when `inputs_embeds` are passed instead of `input_ids`, it does the same (take the last value in
    each row of the batch).
    """, TRANSFO_XL_START_DOCSTRING)
class TFTransfoXLForSequenceClassification(TFTransfoXLPreTrainedModel, TFSequenceClassificationLoss):
    def __init__(self, config, *inputs, **kwargs) -> None:
        ...
    
    def get_output_embeddings(self): # -> TFAdaptiveEmbedding:
        ...
    
    @unpack_inputs
    @add_start_docstrings_to_model_forward(TRANSFO_XL_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(checkpoint=_CHECKPOINT_FOR_DOC, output_type=TFTransfoXLSequenceClassifierOutputWithPast, config_class=_CONFIG_FOR_DOC)
    def call(self, input_ids: TFModelInputType | None = ..., mems: List[tf.Tensor] | None = ..., head_mask: np.ndarray | tf.Tensor | None = ..., inputs_embeds: np.ndarray | tf.Tensor | None = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., labels: np.ndarray | tf.Tensor | None = ..., training: Optional[bool] = ...) -> Union[Tuple, TFTransfoXLSequenceClassifierOutputWithPast]:
        r"""
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the cross entropy classification loss. Indices should be in `[0, ...,
            config.vocab_size - 1]`.
        """
        ...
    

