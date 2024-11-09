"""
This type stub file was generated by pyright.
"""

import torch
from typing import Optional, Tuple, Union
from torch import nn
from ...modeling_outputs import BaseModelOutput, CausalLMOutput, SequenceClassifierOutput
from ...modeling_utils import PreTrainedModel
from ...utils import add_code_sample_docstrings, add_start_docstrings, add_start_docstrings_to_model_forward
from .configuration_sew_d import SEWDConfig

"""PyTorch SEW model."""
logger = ...
_HIDDEN_STATES_START_POSITION = ...
_CONFIG_FOR_DOC = ...
_CHECKPOINT_FOR_DOC = ...
_EXPECTED_OUTPUT_SHAPE = ...
_CTC_EXPECTED_OUTPUT = ...
_CTC_EXPECTED_LOSS = ...
_SEQ_CLASS_CHECKPOINT = ...
_SEQ_CLASS_EXPECTED_OUTPUT = ...
_SEQ_CLASS_EXPECTED_LOSS = ...
def make_log_bucket_position(relative_pos, bucket_size, max_position): # -> Tensor:
    ...

def build_relative_position(query_size, key_size, bucket_size=..., max_position=..., device=...): # -> Tensor:
    """
    Build relative position according to the query and key

    We assume the absolute position of query \\(P_q\\) is range from (0, query_size) and the absolute position of key
    \\(P_k\\) is range from (0, key_size), The relative positions from query to key is \\(R_{q \\rightarrow k} = P_q -
    P_k\\)

    Args:
        query_size (int): the length of query
        key_size (int): the length of key
        bucket_size (int): the size of position bucket
        max_position (int): the maximum allowed absolute position
        device (`torch.device`): the device on which tensors will be created.

    Return:
        `torch.LongTensor`: A tensor with shape [1, query_size, key_size]
    """
    ...

@torch.jit.script
def c2p_dynamic_expand(c2p_pos, query_layer, relative_pos):
    ...

@torch.jit.script
def p2c_dynamic_expand(c2p_pos, query_layer, key_layer):
    ...

@torch.jit.script
def pos_dynamic_expand(pos_index, p2c_att, key_layer):
    ...

def get_mask(input, local_context): # -> tuple[Tensor | None, Any | int]:
    ...

class SEWDNoLayerNormConvLayer(nn.Module):
    def __init__(self, config, layer_id=...) -> None:
        ...
    
    def forward(self, hidden_states):
        ...
    


class SEWDLayerNormConvLayer(nn.Module):
    def __init__(self, config, layer_id=...) -> None:
        ...
    
    def forward(self, hidden_states):
        ...
    


class SEWDGroupNormConvLayer(nn.Module):
    def __init__(self, config, layer_id=...) -> None:
        ...
    
    def forward(self, hidden_states):
        ...
    


class SEWDPositionalConvEmbedding(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def forward(self, hidden_states):
        ...
    


class SEWDSamePadLayer(nn.Module):
    def __init__(self, num_conv_pos_embeddings) -> None:
        ...
    
    def forward(self, hidden_states):
        ...
    


class SEWDUpsampling(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def forward(self, hidden_states):
        ...
    


class SEWDFeatureEncoder(nn.Module):
    """Construct the features from raw audio waveform"""
    def __init__(self, config) -> None:
        ...
    
    def forward(self, input_values): # -> Any:
        ...
    


class SEWDFeatureExtractor(SEWDFeatureEncoder):
    def __init__(self, config) -> None:
        ...
    


class ContextPooler(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def forward(self, hidden_states):
        ...
    
    @property
    def output_dim(self):
        ...
    


class XSoftmax(torch.autograd.Function):
    """
    Masked Softmax which is optimized for saving memory

    Args:
        input (`torch.tensor`): The input tensor that will apply softmax.
        mask (`torch.IntTensor`):
            The mask matrix where 0 indicate that element will be ignored in the softmax calculation.
        dim (int): The dimension that will apply softmax

    Example:

    ```python
    >>> import torch
    >>> from transformers.models.deberta_v2.modeling_deberta_v2 import XSoftmax

    >>> # Make a tensor
    >>> x = torch.randn([4, 20, 100])

    >>> # Create a mask
    >>> mask = (x > 0).int()

    >>> # Specify the dimension to apply softmax
    >>> dim = -1

    >>> y = XSoftmax.apply(x, mask, dim)
    ```"""
    @staticmethod
    def forward(ctx, input, mask, dim): # -> Tensor:
        ...
    
    @staticmethod
    def backward(ctx, grad_output): # -> tuple[Tensor, None, None]:
        ...
    
    @staticmethod
    def symbolic(g, self, mask, dim): # -> Value | tuple[Value, ...]:
        ...
    


class DropoutContext:
    def __init__(self) -> None:
        ...
    


class XDropout(torch.autograd.Function):
    """Optimized dropout function to save computation and memory by using mask operation instead of multiplication."""
    @staticmethod
    def forward(ctx, input, local_ctx):
        ...
    
    @staticmethod
    def backward(ctx, grad_output): # -> tuple[Any, None]:
        ...
    
    @staticmethod
    def symbolic(g: torch._C.Graph, input: torch._C.Value, local_ctx: Union[float, DropoutContext]) -> torch._C.Value:
        ...
    


class StableDropout(nn.Module):
    """
    Optimized dropout module for stabilizing the training

    Args:
        drop_prob (float): the dropout probabilities
    """
    def __init__(self, drop_prob) -> None:
        ...
    
    def forward(self, x): # -> Any | None:
        """
        Call the module

        Args:
            x (`torch.tensor`): The input tensor to apply dropout
        """
        ...
    
    def clear_context(self): # -> None:
        ...
    
    def init_context(self, reuse_mask=..., scale=...): # -> None:
        ...
    
    def get_context(self): # -> Any:
        ...
    


class SEWDSelfOutput(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def forward(self, hidden_states, input_tensor): # -> Any:
        ...
    


class DisentangledSelfAttention(nn.Module):
    """
    Disentangled self-attention module

    Parameters:
        config (`DebertaV2Config`):
            A model config class instance with the configuration to build a new model. The schema is similar to
            *BertConfig*, for more details, please refer [`DebertaV2Config`]

    """
    def __init__(self, config) -> None:
        ...
    
    def transpose_for_scores(self, x, attention_heads):
        ...
    
    def forward(self, hidden_states, attention_mask, output_attentions=..., query_states=..., relative_pos=..., rel_embeddings=...): # -> tuple[Tensor, Any] | Tensor:
        """
        Call the module

        Args:
            hidden_states (`torch.FloatTensor`):
                Input states to the module usually the output from previous layer, it will be the Q,K and V in
                *Attention(Q,K,V)*

            attention_mask (`torch.BoolTensor`):
                An attention mask matrix of shape [*B*, *N*, *N*] where *B* is the batch size, *N* is the maximum
                sequence length in which element [i,j] = *1* means the *i* th token in the input can attend to the *j*
                th token.

            output_attentions (`bool`, *optional*):
                Whether return the attention matrix.

            query_states (`torch.FloatTensor`, *optional*):
                The *Q* state in *Attention(Q,K,V)*.

            relative_pos (`torch.LongTensor`):
                The relative position encoding between the tokens in the sequence. It's of shape [*B*, *N*, *N*] with
                values ranging in [*-max_relative_positions*, *max_relative_positions*].

            rel_embeddings (`torch.FloatTensor`):
                The embedding of relative distances. It's a tensor of shape [\\(2 \\times
                \\text{max_relative_positions}\\), *hidden_size*].


        """
        ...
    
    def disentangled_attention_bias(self, query_layer, key_layer, relative_pos, rel_embeddings, scale_factor): # -> Tensor | Literal[0]:
        ...
    


class SEWDAttention(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def forward(self, hidden_states, attention_mask, output_attentions=..., query_states=..., relative_pos=..., rel_embeddings=...): # -> tuple[Any, Any] | Any:
        ...
    


class SEWDIntermediate(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
        ...
    


class SEWDOutput(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def forward(self, hidden_states, input_tensor): # -> Any:
        ...
    


class SEWDLayer(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def forward(self, hidden_states, attention_mask, query_states=..., relative_pos=..., rel_embeddings=..., output_attentions=...): # -> tuple[Any, Any] | Any:
        ...
    


class ConvLayer(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def forward(self, hidden_states, residual_states, input_mask): # -> Any:
        ...
    


class SEWDTransformerEncoder(nn.Module):
    """Modified BertEncoder with relative position bias support"""
    def __init__(self, config) -> None:
        ...
    
    def get_rel_embedding(self): # -> Any | Tensor | None:
        ...
    
    def get_attention_mask(self, attention_mask):
        ...
    
    def get_rel_pos(self, hidden_states, query_states=..., relative_pos=...): # -> Tensor | None:
        ...
    
    def forward(self, hidden_states, attention_mask, output_hidden_states=..., output_attentions=..., query_states=..., relative_pos=..., return_dict=...): # -> tuple[Any, ...] | BaseModelOutput:
        ...
    


class SEWDEncoder(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def forward(self, hidden_states: torch.tensor, attention_mask: Optional[torch.Tensor] = ..., output_attentions: bool = ..., output_hidden_states: bool = ..., return_dict: bool = ...): # -> tuple[Any, ...] | BaseModelOutput:
        ...
    


class SEWDPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = SEWDConfig
    base_model_prefix = ...
    main_input_name = ...
    supports_gradient_checkpointing = ...


SEWD_START_DOCSTRING = ...
SEWD_INPUTS_DOCSTRING = ...
@add_start_docstrings("The bare SEW-D Model transformer outputting raw hidden-states without any specific head on top.", SEWD_START_DOCSTRING)
class SEWDModel(SEWDPreTrainedModel):
    def __init__(self, config: SEWDConfig) -> None:
        ...
    
    @add_start_docstrings_to_model_forward(SEWD_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(checkpoint=_CHECKPOINT_FOR_DOC, output_type=BaseModelOutput, config_class=_CONFIG_FOR_DOC, modality="audio", expected_output=_EXPECTED_OUTPUT_SHAPE)
    def forward(self, input_values: Optional[torch.Tensor], attention_mask: Optional[torch.Tensor] = ..., mask_time_indices: Optional[torch.FloatTensor] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple, BaseModelOutput]:
        ...
    


@add_start_docstrings("""SEW-D Model with a `language modeling` head on top for Connectionist Temporal Classification (CTC).""", SEWD_START_DOCSTRING)
class SEWDForCTC(SEWDPreTrainedModel):
    def __init__(self, config, target_lang: Optional[str] = ...) -> None:
        ...
    
    def tie_weights(self): # -> None:
        """
        This method overwrites [`~PreTrainedModel.tie_weights`] so that adapter weights can be correctly loaded when
        passing `target_lang=...` to `from_pretrained(...)`.

        This method is **not** supposed to be called by the user and is prone to be changed in the future.
        """
        ...
    
    def freeze_feature_extractor(self): # -> None:
        """
        Calling this function will disable the gradient computation for the feature encoder so that its parameter will
        not be updated during training.
        """
        ...
    
    def freeze_feature_encoder(self): # -> None:
        """
        Calling this function will disable the gradient computation for the feature encoder so that its parameter will
        not be updated during training.
        """
        ...
    
    def freeze_base_model(self): # -> None:
        """
        Calling this function will disable the gradient computation for the base model so that its parameters will not
        be updated during training. Only the classification head will be updated.
        """
        ...
    
    @add_start_docstrings_to_model_forward(SEWD_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(checkpoint=_CHECKPOINT_FOR_DOC, output_type=CausalLMOutput, config_class=_CONFIG_FOR_DOC, expected_output=_CTC_EXPECTED_OUTPUT, expected_loss=_CTC_EXPECTED_LOSS)
    def forward(self, input_values: Optional[torch.Tensor], attention_mask: Optional[torch.Tensor] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., labels: Optional[torch.Tensor] = ...) -> Union[Tuple, CausalLMOutput]:
        r"""
        labels (`torch.LongTensor` of shape `(batch_size, target_length)`, *optional*):
            Labels for connectionist temporal classification. Note that `target_length` has to be smaller or equal to
            the sequence length of the output logits. Indices are selected in `[-100, 0, ..., config.vocab_size - 1]`.
            All labels set to `-100` are ignored (masked), the loss is only computed for labels in `[0, ...,
            config.vocab_size - 1]`.
        """
        ...
    


@add_start_docstrings("""
    SEWD Model with a sequence classification head on top (a linear layer over the pooled output) for tasks like SUPERB
    Keyword Spotting.
    """, SEWD_START_DOCSTRING)
class SEWDForSequenceClassification(SEWDPreTrainedModel):
    def __init__(self, config) -> None:
        ...
    
    def freeze_feature_extractor(self): # -> None:
        """
        Calling this function will disable the gradient computation for the feature encoder so that its parameters will
        not be updated during training.
        """
        ...
    
    def freeze_feature_encoder(self): # -> None:
        """
        Calling this function will disable the gradient computation for the feature encoder so that its parameter will
        not be updated during training.
        """
        ...
    
    def freeze_base_model(self): # -> None:
        """
        Calling this function will disable the gradient computation for the base model so that its parameters will not
        be updated during training. Only the classification head will be updated.
        """
        ...
    
    @add_start_docstrings_to_model_forward(SEWD_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(checkpoint=_SEQ_CLASS_CHECKPOINT, output_type=SequenceClassifierOutput, config_class=_CONFIG_FOR_DOC, modality="audio", expected_output=_SEQ_CLASS_EXPECTED_OUTPUT, expected_loss=_SEQ_CLASS_EXPECTED_LOSS)
    def forward(self, input_values: Optional[torch.Tensor], attention_mask: Optional[torch.Tensor] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., labels: Optional[torch.Tensor] = ...) -> Union[Tuple, SequenceClassifierOutput]:
        r"""
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
        ...
    

