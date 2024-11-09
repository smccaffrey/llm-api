"""
This type stub file was generated by pyright.
"""

import torch
import torch.nn as nn
from typing import Optional, Tuple, Union
from ...generation import GenerationMixin
from ...modeling_outputs import MoEModelOutput, Seq2SeqMoEModelOutput, Seq2SeqMoEOutput
from ...modeling_utils import PreTrainedModel
from ...utils import add_start_docstrings, add_start_docstrings_to_model_forward, replace_return_docstrings
from .configuration_switch_transformers import SwitchTransformersConfig

"""PyTorch SwitchTransformers model."""
logger = ...
_CONFIG_FOR_DOC = ...
_CHECKPOINT_FOR_DOC = ...
def router_z_loss_func(router_logits: torch.Tensor) -> float:
    r"""
    Compute the router z-loss implemented in PyTorch.

    The router z-loss was introduced in [Designing Effective Sparse Expert Models](https://arxiv.org/abs/2202.08906).
    It encourages router logits to remain small in an effort to improve stability.

    Args:
        router_logits (`float`):
            Input logits of shape [batch_size, sequence_length, num_experts]

    Returns:
        Scalar router z-loss.
    """
    ...

def load_balancing_loss_func(router_probs: torch.Tensor, expert_indices: torch.Tensor) -> float:
    r"""
    Computes auxiliary load balancing loss as in Switch Transformer - implemented in Pytorch.

    See Switch Transformer (https://arxiv.org/abs/2101.03961) for more details. This function implements the loss
    function presented in equations (4) - (6) of the paper. It aims at penalizing cases where the routing between
    experts is too unbalanced.

    Args:
        router_probs (`torch.Tensor`):
            Probability assigned to each expert per token. Shape: [batch_size, seqeunce_length, num_experts].
        expert_indices (`torch.Tensor`):
            Indices tensor of shape [batch_size, seqeunce_length] identifying the selected expert for a given token.

    Returns:
        The auxiliary loss.
    """
    ...

class SwitchTransformersTop1Router(nn.Module):
    """
    Router using tokens choose top-1 experts assignment.

    This router uses the same mechanism as in Switch Transformer (https://arxiv.org/abs/2101.03961) and V-MoE
    (https://arxiv.org/abs/2106.05974): tokens choose their top experts. Items are sorted by router_probs and then
    routed to their choice of expert until the expert's expert_capacity is reached. **There is no guarantee that each
    token is processed by an expert**, or that each expert receives at least one token.

    """
    def __init__(self, config: SwitchTransformersConfig) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor) -> Tuple:
        r"""
        Generic forward function for every Router class. Each Router expects to have the same input hidden states
        (`hidden_states`) corresponding to the hidden states for each token, the `expert_capacity` corresponding to the
        number of tokens the Router will send to each expert, some Routers can send up to few tokens to each expert.

        Each Router works as the following: it expects the hidden states for each token, gets the `router_probs` and
        `router_logits` from the `router_weights`. This will assign for each token, the raw probability to be assigned
        to an expert. Then each Router class will have to define its own `_compute_routing_instructions`.

        Args:
            hidden_states (`torch.Tensor`) :
                [num_groups, tokens_per_group, hidden_dim] inputs to send to experts.
        Returns:
            Tuple[`torch.Tensor`, `torch.Tensor`, `torch.Tensor`] Tuple containing the expert index, the router probs
            and the router logits. The router probabilities and logits are required to compute the loss.
        """
        ...
    


class SwitchTransformersLayerNorm(nn.Module):
    def __init__(self, hidden_size, eps=...) -> None:
        """
        Construct a layernorm module in the SwitchTransformers style. No bias and no subtraction of mean.
        """
        ...
    
    def forward(self, hidden_states):
        ...
    


class SwitchTransformersDenseActDense(nn.Module):
    def __init__(self, config: SwitchTransformersConfig) -> None:
        ...
    
    def forward(self, hidden_states): # -> Any:
        ...
    


class SwitchTransformersSparseMLP(nn.Module):
    r"""
    Implementation of the Switch Transformers Sparse MLP module.
    """
    def __init__(self, config: SwitchTransformersConfig, expert_class: nn.Module = ...) -> None:
        ...
    
    def forward(self, hidden_states): # -> tuple[Any, tuple[Any, Tensor]]:
        r"""
        Hold on, this will be slightly tricky to understand In the correct order, a MoE layer does the following:

        1- Gets the `router_mask` from the router. The shape of the mask is `(batch_size, sequence_length, num_expert)`
        and corresponds to the argmax of the `router_probs`. The probabilities are needed in the computation of the
        hidden states : they are broadcasted to the hidden states values (can be interpreted as a scaling factor).

        2- Dispatch the tokens to its associated experts. We do a classic for loop over the experts and assign for each
        expert the corresponding hidden states.

        """
        ...
    


class SwitchTransformersLayerFF(nn.Module):
    r"""
    Switch Transformers Feed Forward layer module. This is a wrapper around the Mixture of Experts module.

    Parameters:
        config : ([`SwitchTransformersConfig`]): Model configuration class with all the parameters of the model.
            Initializing with a config file does not load the weights associated with the model, only the
            configuration. Check out the [`~PreTrainedModel.from_pretrained`] method to load the model weights.
        is_sparse (`bool`):
            Whether the MLP layer is a `Sparse` layer (contains a Mixture of Experts) or not
    """
    def __init__(self, config: SwitchTransformersConfig, is_sparse=...) -> None:
        ...
    
    def forward(self, hidden_states, output_router_logits): # -> tuple[Any, Any]:
        ...
    


class SwitchTransformersAttention(nn.Module):
    def __init__(self, config: SwitchTransformersConfig, has_relative_attention_bias=..., layer_idx: Optional[int] = ...) -> None:
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
    


class SwitchTransformersLayerSelfAttention(nn.Module):
    def __init__(self, config, has_relative_attention_bias=..., layer_idx: Optional[int] = ...) -> None:
        ...
    
    def forward(self, hidden_states, attention_mask=..., position_bias=..., layer_head_mask=..., past_key_value=..., use_cache=..., output_attentions=..., cache_position=...): # -> Any:
        ...
    


class SwitchTransformersLayerCrossAttention(nn.Module):
    def __init__(self, config, layer_idx: Optional[int] = ...) -> None:
        ...
    
    def forward(self, hidden_states, key_value_states, attention_mask=..., position_bias=..., layer_head_mask=..., past_key_value=..., use_cache=..., query_length=..., output_attentions=..., cache_position=...): # -> Any:
        ...
    


class SwitchTransformersBlock(nn.Module):
    def __init__(self, config, has_relative_attention_bias=..., is_sparse=..., layer_idx: Optional[int] = ...) -> None:
        ...
    
    def forward(self, hidden_states, attention_mask=..., position_bias=..., encoder_hidden_states=..., encoder_attention_mask=..., encoder_decoder_position_bias=..., layer_head_mask=..., cross_attn_layer_head_mask=..., past_key_value=..., use_cache=..., output_attentions=..., output_router_logits=..., return_dict=..., cache_position=...): # -> Any:
        ...
    


class SwitchTransformersPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = SwitchTransformersConfig
    base_model_prefix = ...
    supports_gradient_checkpointing = ...
    _supports_cache_class = ...
    _supports_static_cache = ...
    _no_split_modules = ...
    @property
    def dummy_inputs(self): # -> dict[str, Tensor]:
        ...
    


class SwitchTransformersStack(SwitchTransformersPreTrainedModel):
    def __init__(self, config, embed_tokens=...) -> None:
        ...
    
    def get_input_embeddings(self): # -> Embedding:
        ...
    
    def set_input_embeddings(self, new_embeddings): # -> None:
        ...
    
    def forward(self, input_ids=..., attention_mask=..., encoder_hidden_states=..., encoder_attention_mask=..., inputs_embeds=..., head_mask=..., cross_attn_head_mask=..., past_key_values=..., use_cache=..., output_attentions=..., output_hidden_states=..., output_router_logits=..., return_dict=..., cache_position=...):
        ...
    


SWITCH_TRANSFORMERS_START_DOCSTRING = ...
SWITCH_TRANSFORMERS_INPUTS_DOCSTRING = ...
SWITCH_TRANSFORMERS_ENCODER_INPUTS_DOCSTRING = ...
__HEAD_MASK_WARNING_MSG = ...
@add_start_docstrings("The bare SWITCH_TRANSFORMERS Model transformer outputting raw hidden-states without any specific head on top.", SWITCH_TRANSFORMERS_START_DOCSTRING)
class SwitchTransformersModel(SwitchTransformersPreTrainedModel):
    _tied_weights_keys = ...
    def __init__(self, config: SwitchTransformersConfig) -> None:
        ...
    
    def get_input_embeddings(self): # -> Embedding:
        ...
    
    def set_input_embeddings(self, new_embeddings): # -> None:
        ...
    
    def get_encoder(self): # -> SwitchTransformersStack:
        ...
    
    def get_decoder(self): # -> SwitchTransformersStack:
        ...
    
    @add_start_docstrings_to_model_forward(SWITCH_TRANSFORMERS_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=Seq2SeqMoEModelOutput, config_class=_CONFIG_FOR_DOC)
    def forward(self, input_ids: Optional[torch.LongTensor] = ..., attention_mask: Optional[torch.FloatTensor] = ..., decoder_input_ids: Optional[torch.LongTensor] = ..., decoder_attention_mask: Optional[torch.BoolTensor] = ..., head_mask: Optional[torch.FloatTensor] = ..., decoder_head_mask: Optional[torch.FloatTensor] = ..., cross_attn_head_mask: Optional[torch.Tensor] = ..., encoder_outputs: Optional[Tuple[Tuple[torch.FloatTensor]]] = ..., past_key_values: Optional[Tuple[Tuple[torch.FloatTensor]]] = ..., inputs_embeds: Optional[torch.Tensor] = ..., decoder_inputs_embeds: Optional[torch.Tensor] = ..., use_cache: Optional[bool] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., output_router_logits: Optional[bool] = ..., return_dict: Optional[bool] = ..., cache_position: Optional[torch.LongTensor] = ...) -> Union[Tuple[torch.FloatTensor], Seq2SeqMoEModelOutput]:
        r"""
        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, SwitchTransformersModel

        >>> tokenizer = AutoTokenizer.from_pretrained("google/switch-base-8")
        >>> model = SwitchTransformersModel.from_pretrained("google/switch-base-8")

        >>> input_ids = tokenizer(
        ...     "Studies have been shown that owning a dog is good for you", return_tensors="pt"
        ... ).input_ids  # Batch size 1
        >>> decoder_input_ids = tokenizer("Studies show that", return_tensors="pt").input_ids  # Batch size 1

        >>> # preprocess: Prepend decoder_input_ids with start token which is pad token for SwitchTransformersModel.
        >>> # This is not needed for torch's SwitchTransformersForConditionalGeneration as it does this internally using labels arg.
        >>> decoder_input_ids = model._shift_right(decoder_input_ids)

        >>> # forward pass
        >>> outputs = model(input_ids=input_ids, decoder_input_ids=decoder_input_ids)
        >>> last_hidden_states = outputs.last_hidden_state
        ```"""
        ...
    


@add_start_docstrings("""SWITCH_TRANSFORMERS Model with a `language modeling` head on top.""", SWITCH_TRANSFORMERS_START_DOCSTRING)
class SwitchTransformersForConditionalGeneration(SwitchTransformersPreTrainedModel, GenerationMixin):
    _tied_weights_keys = ...
    def __init__(self, config: SwitchTransformersConfig) -> None:
        ...
    
    def get_input_embeddings(self): # -> Embedding:
        ...
    
    def set_input_embeddings(self, new_embeddings): # -> None:
        ...
    
    def set_output_embeddings(self, new_embeddings): # -> None:
        ...
    
    def get_output_embeddings(self): # -> Linear:
        ...
    
    def get_encoder(self): # -> SwitchTransformersStack:
        ...
    
    def get_decoder(self): # -> SwitchTransformersStack:
        ...
    
    @add_start_docstrings_to_model_forward(SWITCH_TRANSFORMERS_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=Seq2SeqMoEOutput, config_class=_CONFIG_FOR_DOC)
    def forward(self, input_ids: Optional[torch.LongTensor] = ..., attention_mask: Optional[torch.FloatTensor] = ..., decoder_input_ids: Optional[torch.LongTensor] = ..., decoder_attention_mask: Optional[torch.BoolTensor] = ..., head_mask: Optional[torch.FloatTensor] = ..., decoder_head_mask: Optional[torch.FloatTensor] = ..., cross_attn_head_mask: Optional[torch.Tensor] = ..., encoder_outputs: Optional[Tuple[Tuple[torch.Tensor]]] = ..., past_key_values: Optional[Tuple[Tuple[torch.Tensor]]] = ..., inputs_embeds: Optional[torch.FloatTensor] = ..., decoder_inputs_embeds: Optional[torch.FloatTensor] = ..., labels: Optional[torch.LongTensor] = ..., use_cache: Optional[bool] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., output_router_logits: Optional[bool] = ..., return_dict: Optional[bool] = ..., cache_position: Optional[torch.LongTensor] = ...) -> Union[Tuple[torch.FloatTensor], Seq2SeqMoEOutput]:
        r"""
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[-100, 0, ...,
            config.vocab_size - 1]`. All labels set to `-100` are ignored (masked), the loss is only computed for
            labels in `[0, ..., config.vocab_size]`

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, SwitchTransformersForConditionalGeneration

        >>> tokenizer = AutoTokenizer.from_pretrained("google/switch-base-8")
        >>> model = SwitchTransformersForConditionalGeneration.from_pretrained("google/switch-base-8")

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
        >>> # . To, let’s say you have a dog. To summarize:
        >>> # Since the model has been trained on MLM, this will output gibberish
        ```"""
        ...
    
    def prepare_decoder_input_ids_from_labels(self, labels: torch.Tensor): # -> Tensor:
        ...
    


@add_start_docstrings("The bare SWITCH_TRANSFORMERS Model transformer outputting encoder's raw hidden-states without any specific head" " on top.", SWITCH_TRANSFORMERS_START_DOCSTRING)
class SwitchTransformersEncoderModel(SwitchTransformersPreTrainedModel):
    _tied_weights_keys = ...
    def __init__(self, config: SwitchTransformersConfig) -> None:
        ...
    
    def get_input_embeddings(self): # -> Embedding:
        ...
    
    def set_input_embeddings(self, new_embeddings): # -> None:
        ...
    
    def get_encoder(self): # -> SwitchTransformersStack:
        ...
    
    @add_start_docstrings_to_model_forward(SWITCH_TRANSFORMERS_ENCODER_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=MoEModelOutput, config_class=_CONFIG_FOR_DOC)
    def forward(self, input_ids: Optional[torch.LongTensor] = ..., attention_mask: Optional[torch.FloatTensor] = ..., head_mask: Optional[torch.FloatTensor] = ..., inputs_embeds: Optional[torch.FloatTensor] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., output_router_logits: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple[torch.FloatTensor], MoEModelOutput]:
        r"""
        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, SwitchTransformersEncoderModel

        >>> tokenizer = AutoTokenizer.from_pretrained("google/switch-base-8")
        >>> model = SwitchTransformersEncoderModel.from_pretrained("google/switch-base-8")
        >>> input_ids = tokenizer(
        ...     "Studies have been shown that owning a dog is good for you", return_tensors="pt"
        ... ).input_ids  # Batch size 1
        >>> outputs = model(input_ids=input_ids)
        >>> last_hidden_states = outputs.last_hidden_state
        ```"""
        ...
    

