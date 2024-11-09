"""
This type stub file was generated by pyright.
"""

import torch
from dataclasses import dataclass
from typing import Optional, Tuple, Union
from torch import nn
from ...cache_utils import MambaCache
from ...generation import GenerationMixin
from ...modeling_utils import PreTrainedModel
from ...utils import ModelOutput, add_code_sample_docstrings, add_start_docstrings, add_start_docstrings_to_model_forward
from ...utils.import_utils import is_causal_conv1d_available, is_mamba_ssm_available, is_mambapy_available
from .configuration_falcon_mamba import FalconMambaConfig
from mambapy.pscan import pscan

"""PyTorch FALCONMAMBA model."""
logger = ...
if is_mambapy_available():
    ...
else:
    pscan = ...
if is_mamba_ssm_available():
    ...
else:
    ...
if is_causal_conv1d_available():
    ...
else:
    ...
is_fast_path_available = ...
_CHECKPOINT_FOR_DOC = ...
_CONFIG_FOR_DOC = ...
def rms_forward(hidden_states, variance_epsilon=...):
    """
    Calculates simple RMSNorm with no learnable weights. `MambaRMSNorm` will
    leverage this in order to multiply the final result with the RMSNorm weight

    Args:
        hidden_states (`torch.Tensor`):
            Hidden states to normalize
        variance_epsilon (`float`):
            The eps value to add in the square root scaling factor
    """
    ...

class FalconMambaMixer(nn.Module):
    """
    Compute ∆, A, B, C, and D the state space parameters and compute the `contextualized_states`.
    A, D are input independent (see FalconMamba paper [1] Section 3.5.2 "Interpretation of A" for why A isn't selective)
    ∆, B, C are input-dependent (this is a key difference between FalconMamba and the linear time invariant S4,
    and is why FalconMamba is called **selective** state spaces)
    """
    def __init__(self, config: FalconMambaConfig, layer_idx: int) -> None:
        ...
    
    def cuda_kernels_forward(self, hidden_states: torch.Tensor, cache_params: Optional[MambaCache] = ..., cache_position: Optional[torch.LongTensor] = ..., attention_mask: Optional[torch.LongTensor] = ...): # -> Any | None:
        ...
    
    def slow_forward(self, input_states, cache_params: Optional[MambaCache] = ..., cache_position: Optional[torch.LongTensor] = ..., attention_mask: Optional[torch.LongTensor] = ...): # -> Any:
        ...
    
    def forward(self, hidden_states, cache_params: Optional[MambaCache] = ..., cache_position: Optional[torch.LongTensor] = ..., attention_mask: Optional[torch.LongTensor] = ...): # -> Any | None:
        ...
    


class FalconMambaRMSNorm(nn.Module):
    def __init__(self, hidden_size, eps=...) -> None:
        """
        FalconMambaRMSNorm is equivalent to T5LayerNorm and LlamaRMSNorm
        """
        ...
    
    def extra_repr(self): # -> str:
        ...
    
    def forward(self, hidden_states):
        ...
    


class FalconMambaBlock(nn.Module):
    def __init__(self, config, layer_idx) -> None:
        ...
    
    def forward(self, hidden_states, cache_params: Optional[MambaCache] = ..., cache_position: Optional[torch.LongTensor] = ..., attention_mask: Optional[torch.LongTensor] = ...):
        ...
    


class FalconMambaPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = FalconMambaConfig
    base_model_prefix = ...
    _no_split_modules = ...
    supports_gradient_checkpointing = ...
    _is_stateful = ...


@dataclass
class FalconMambaOutput(ModelOutput):
    """
    Class for the FALCONMAMBA model outputs.

    Args:
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        cache_params (`MambaCache`):
            The state of the model at the last time step. Can be used in a forward method with the next `input_ids` to
            avoid providing the old `input_ids`.

            Includes both the State space model state matrices after the selective scan, and the Convolutional states
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
    """
    last_hidden_state: Optional[torch.FloatTensor] = ...
    cache_params: Optional[MambaCache] = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...


@dataclass
class FalconMambaCausalLMOutput(ModelOutput):
    """
    Base class for causal language model (or autoregressive) outputs.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Language modeling loss (for next-token prediction).
        logits (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
        cache_params (`MambaCache`):
            The state of the model at the last time step. Can be used in a forward method with the next `input_ids` to
            avoid providing the old `input_ids`.

            Includes both the State space model state matrices after the selective scan, and the Convolutional states
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: Optional[torch.FloatTensor] = ...
    cache_params: Optional[MambaCache] = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...


FALCONMAMBA_START_DOCSTRING = ...
FALCONMAMBA_INPUTS_DOCSTRING = ...
@add_start_docstrings("The bare FALCONMAMBA Model transformer outputting raw hidden-states without any specific head on top.", FALCONMAMBA_START_DOCSTRING)
class FalconMambaModel(FalconMambaPreTrainedModel):
    def __init__(self, config) -> None:
        ...
    
    def get_input_embeddings(self): # -> Embedding:
        ...
    
    def set_input_embeddings(self, new_embeddings): # -> None:
        ...
    
    @add_start_docstrings_to_model_forward(FALCONMAMBA_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(checkpoint=_CHECKPOINT_FOR_DOC, output_type=FalconMambaOutput, config_class=_CONFIG_FOR_DOC)
    def forward(self, input_ids: Optional[torch.LongTensor] = ..., inputs_embeds: Optional[torch.LongTensor] = ..., cache_params: Optional[MambaCache] = ..., use_cache: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., cache_position: Optional[torch.LongTensor] = ..., attention_mask: Optional[torch.LongTensor] = ...) -> Union[Tuple, FalconMambaOutput]:
        ...
    


@add_start_docstrings("""
    The FALCONMAMBA Model transformer with a language modeling head on top (linear layer with weights tied to the input
    embeddings).
    """, FALCONMAMBA_START_DOCSTRING)
class FalconMambaForCausalLM(FalconMambaPreTrainedModel, GenerationMixin):
    _tied_weights_keys = ...
    def __init__(self, config) -> None:
        ...
    
    def get_output_embeddings(self): # -> Linear:
        ...
    
    def set_output_embeddings(self, new_embeddings): # -> None:
        ...
    
    def get_input_embeddings(self): # -> Embedding:
        ...
    
    def set_input_embeddings(self, new_embeddings): # -> None:
        ...
    
    def prepare_inputs_for_generation(self, input_ids, inputs_embeds=..., use_cache=..., cache_params: Optional[MambaCache] = ..., cache_position: Optional[torch.LongTensor] = ..., attention_mask: Optional[torch.LongTensor] = ..., **kwargs): # -> dict[str, Any]:
        ...
    
    @add_start_docstrings_to_model_forward(FALCONMAMBA_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(checkpoint=_CHECKPOINT_FOR_DOC, output_type=FalconMambaCausalLMOutput, config_class=_CONFIG_FOR_DOC)
    def forward(self, input_ids: Optional[torch.LongTensor] = ..., attention_mask: Optional[torch.LongTensor] = ..., inputs_embeds: Optional[torch.FloatTensor] = ..., cache_params: Optional[MambaCache] = ..., labels: Optional[torch.LongTensor] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., use_cache: Optional[bool] = ..., cache_position: Optional[torch.Tensor] = ..., **kwargs) -> Union[Tuple, FalconMambaCausalLMOutput]:
        r"""
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for language modeling. Note that the labels **are shifted** inside the model, i.e. you can set
            `labels = input_ids` Indices are selected in `[-100, 0, ..., config.vocab_size]` All labels set to `-100`
            are ignored (masked), the loss is only computed for labels in `[0, ..., config.vocab_size]`
        """
        ...
    

