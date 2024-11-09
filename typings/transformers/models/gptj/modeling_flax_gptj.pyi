"""
This type stub file was generated by pyright.
"""

import flax.linen as nn
import jax
import jax.numpy as jnp
from typing import Optional, Tuple
from flax.core.frozen_dict import FrozenDict
from ...modeling_flax_utils import FlaxPreTrainedModel
from ...utils import add_start_docstrings, add_start_docstrings_to_model_forward
from .configuration_gptj import GPTJConfig

logger = ...
_CHECKPOINT_FOR_DOC = ...
_CONFIG_FOR_DOC = ...
GPTJ_START_DOCSTRING = ...
GPTJ_INPUTS_DOCSTRING = ...
def create_sinusoidal_positions(num_pos, dim):
    ...

def rotate_every_two(tensor):
    ...

def apply_rotary_pos_emb(tensor, sincos):
    ...

class FlaxGPTJAttention(nn.Module):
    config: GPTJConfig
    dtype: jnp.dtype = ...
    causal: bool = ...
    is_cross_attention: bool = ...
    def setup(self): # -> None:
        ...
    
    def __call__(self, hidden_states, attention_mask, position_ids, deterministic: bool = ..., init_cache: bool = ..., output_attentions: bool = ...): # -> tuple[Any, Any] | tuple[Any]:
        ...
    


class FlaxGPTJMLP(nn.Module):
    config: GPTJConfig
    intermediate_size: int
    dtype: jnp.dtype = ...
    def setup(self): # -> None:
        ...
    
    def __call__(self, hidden_states, deterministic: bool = ...):
        ...
    


class FlaxGPTJBlock(nn.Module):
    config: GPTJConfig
    dtype: jnp.dtype = ...
    def setup(self): # -> None:
        ...
    
    def __call__(self, hidden_states, attention_mask=..., position_ids=..., deterministic: bool = ..., init_cache: bool = ..., output_attentions: bool = ...): # -> tuple[Any, Any] | tuple[Any]:
        ...
    


class FlaxGPTJPreTrainedModel(FlaxPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = GPTJConfig
    base_model_prefix = ...
    module_class: nn.Module = ...
    def __init__(self, config: GPTJConfig, input_shape: Tuple = ..., seed: int = ..., dtype: jnp.dtype = ..., _do_init: bool = ..., **kwargs) -> None:
        ...
    
    def init_weights(self, rng: jax.random.PRNGKey, input_shape: Tuple, params: FrozenDict = ...) -> FrozenDict:
        ...
    
    def init_cache(self, batch_size, max_length):
        r"""
        Args:
            batch_size (`int`):
                batch_size used for fast auto-regressive decoding. Defines the batch size of the initialized cache.
            max_length (`int`):
                maximum possible length for auto-regressive decoding. Defines the sequence length of the initialized
                cache.
        """
        ...
    
    @add_start_docstrings_to_model_forward(GPTJ_INPUTS_DOCSTRING)
    def __call__(self, input_ids, attention_mask=..., position_ids=..., params: dict = ..., past_key_values: dict = ..., dropout_rng: jax.random.PRNGKey = ..., train: bool = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...):
        ...
    


class FlaxGPTJBlockCollection(nn.Module):
    config: GPTJConfig
    dtype: jnp.dtype = ...
    def setup(self): # -> None:
        ...
    
    def __call__(self, hidden_states, attention_mask=..., position_ids=..., deterministic: bool = ..., init_cache: bool = ..., output_attentions: bool = ..., output_hidden_states: bool = ..., return_dict: bool = ...): # -> tuple[Any, tuple[()] | tuple[Any, ...] | None, tuple[()] | tuple[Any, ...] | None]:
        ...
    


class FlaxGPTJModule(nn.Module):
    config: GPTJConfig
    dtype: jnp.dtype = ...
    def setup(self): # -> None:
        ...
    
    def __call__(self, input_ids, attention_mask, position_ids, deterministic=..., init_cache: bool = ..., output_attentions: bool = ..., output_hidden_states: bool = ..., return_dict: bool = ...): # -> tuple[Any | tuple[Any, ...] | tuple[()], ...] | FlaxBaseModelOutput:
        ...
    


@add_start_docstrings("The bare GPTJ Model transformer outputting raw hidden-states without any specific head on top.", GPTJ_START_DOCSTRING)
class FlaxGPTJModel(FlaxGPTJPreTrainedModel):
    module_class = ...


class FlaxGPTJForCausalLMModule(nn.Module):
    config: GPTJConfig
    dtype: jnp.dtype = ...
    def setup(self): # -> None:
        ...
    
    def __call__(self, input_ids, attention_mask, position_ids, deterministic: bool = ..., init_cache: bool = ..., output_attentions: bool = ..., output_hidden_states: bool = ..., return_dict: bool = ...): # -> tuple[Any, *tuple[Any | tuple[Any, ...] | tuple[()], ...]] | Any | FlaxCausalLMOutput:
        ...
    


@add_start_docstrings("""
    The GPTJ Model transformer with a language modeling head on top.
    """, GPTJ_START_DOCSTRING)
class FlaxGPTJForCausalLM(FlaxGPTJPreTrainedModel):
    module_class = ...
    def prepare_inputs_for_generation(self, input_ids, max_length, attention_mask: Optional[jax.Array] = ...): # -> dict[str, Any]:
        ...
    
    def update_inputs_for_generation(self, model_outputs, model_kwargs):
        ...
    

