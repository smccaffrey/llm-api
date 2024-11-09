"""
This type stub file was generated by pyright.
"""

import os
import flax.linen as nn
import jax
import jax.numpy as jnp
from typing import Optional, Tuple, Union
from flax.core.frozen_dict import FrozenDict
from jax.random import PRNGKey
from ...modeling_flax_outputs import FlaxBaseModelOutput, FlaxCausalLMOutputWithCrossAttentions, FlaxSeq2SeqLMOutput
from ...modeling_flax_utils import FlaxPreTrainedModel
from ...utils import add_start_docstrings, add_start_docstrings_to_model_forward, replace_return_docstrings
from .configuration_encoder_decoder import EncoderDecoderConfig

"""Classes to support Flax Encoder-Decoder architectures"""
logger = ...
_CONFIG_FOR_DOC = ...
ENCODER_DECODER_START_DOCSTRING = ...
ENCODER_DECODER_INPUTS_DOCSTRING = ...
ENCODER_DECODER_ENCODE_INPUTS_DOCSTRING = ...
ENCODER_DECODER_DECODE_INPUTS_DOCSTRING = ...
class FlaxEncoderDecoderModule(nn.Module):
    config: EncoderDecoderConfig
    dtype: jnp.dtype = ...
    def setup(self): # -> None:
        ...
    
    def __call__(self, input_ids, attention_mask, decoder_input_ids, decoder_attention_mask, position_ids, decoder_position_ids, output_attentions: bool = ..., output_hidden_states: bool = ..., return_dict: bool = ..., deterministic: bool = ...): # -> Any | FlaxSeq2SeqLMOutput:
        ...
    


@add_start_docstrings(ENCODER_DECODER_START_DOCSTRING)
class FlaxEncoderDecoderModel(FlaxPreTrainedModel):
    r"""
    [`FlaxEncoderDecoderModel`] is a generic model class that will be instantiated as a transformer architecture with
    the module (flax.nn.Module) of one of the base model classes of the library as encoder module and another one as
    decoder module when created with the :meth*~transformers.FlaxAutoModel.from_pretrained* class method for the
    encoder and :meth*~transformers.FlaxAutoModelForCausalLM.from_pretrained* class method for the decoder.
    """
    config_class = EncoderDecoderConfig
    base_model_prefix = ...
    module_class = FlaxEncoderDecoderModule
    def __init__(self, config: EncoderDecoderConfig, input_shape: Optional[Tuple] = ..., seed: int = ..., dtype: jnp.dtype = ..., _do_init: bool = ..., **kwargs) -> None:
        ...
    
    def init_weights(self, rng: jax.random.PRNGKey, input_shape: Tuple, params: FrozenDict = ...) -> FrozenDict:
        ...
    
    def init_cache(self, batch_size, max_length, encoder_outputs):
        r"""
        Args:
            batch_size (`int`):
                batch_size used for fast auto-regressive decoding. Defines the batch size of the initialized cache.
            max_length (`int`):
                maximum possible length for auto-regressive decoding. Defines the sequence length of the initialized
                cache.
            encoder_outputs (`Union[FlaxBaseModelOutput, tuple(tuple(jnp.ndarray)]`):
                `encoder_outputs` consists of (`last_hidden_state`, *optional*: `hidden_states`, *optional*:
                `attentions`). `last_hidden_state` of shape `(batch_size, sequence_length, hidden_size)`, *optional*)
                is a sequence of hidden-states at the output of the last layer of the encoder. Used in the
                cross-attention of the decoder.
        """
        ...
    
    @add_start_docstrings(ENCODER_DECODER_ENCODE_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=FlaxBaseModelOutput, config_class=_CONFIG_FOR_DOC)
    def encode(self, input_ids: jnp.ndarray, attention_mask: Optional[jnp.ndarray] = ..., position_ids: Optional[jnp.ndarray] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., train: bool = ..., params: dict = ..., dropout_rng: PRNGKey = ...): # -> FlaxBaseModelOutput:
        r"""
        Returns:

        Example:

        ```python
        >>> from transformers import FlaxEncoderDecoderModel, BertTokenizer

        >>> # initialize a bert2gpt2 from pretrained BERT and GPT2 models. Note that the cross-attention layers will be randomly initialized
        >>> model = FlaxEncoderDecoderModel.from_encoder_decoder_pretrained("google-bert/bert-base-cased", "openai-community/gpt2")

        >>> tokenizer = BertTokenizer.from_pretrained("google-bert/bert-base-cased")

        >>> text = "My friends are cool but they eat too many carbs."
        >>> input_ids = tokenizer.encode(text, return_tensors="np")
        >>> encoder_outputs = model.encode(input_ids)
        ```"""
        ...
    
    @add_start_docstrings(ENCODER_DECODER_DECODE_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=FlaxCausalLMOutputWithCrossAttentions, config_class=_CONFIG_FOR_DOC)
    def decode(self, decoder_input_ids, encoder_outputs, encoder_attention_mask: Optional[jnp.ndarray] = ..., decoder_attention_mask: Optional[jnp.ndarray] = ..., decoder_position_ids: Optional[jnp.ndarray] = ..., past_key_values: dict = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., train: bool = ..., params: dict = ..., dropout_rng: PRNGKey = ...):
        r"""
        Returns:

        Example:

        ```python
        >>> from transformers import FlaxEncoderDecoderModel, BertTokenizer
        >>> import jax.numpy as jnp

        >>> # initialize a bert2gpt2 from pretrained BERT and GPT2 models. Note that the cross-attention layers will be randomly initialized
        >>> model = FlaxEncoderDecoderModel.from_encoder_decoder_pretrained("google-bert/bert-base-cased", "openai-community/gpt2")

        >>> tokenizer = BertTokenizer.from_pretrained("google-bert/bert-base-cased")

        >>> text = "My friends are cool but they eat too many carbs."
        >>> input_ids = tokenizer.encode(text, max_length=1024, return_tensors="np")
        >>> encoder_outputs = model.encode(input_ids)

        >>> decoder_start_token_id = model.config.decoder.bos_token_id
        >>> decoder_input_ids = jnp.ones((input_ids.shape[0], 1), dtype="i4") * decoder_start_token_id

        >>> outputs = model.decode(decoder_input_ids, encoder_outputs)
        >>> logits = outputs.logits
        ```"""
        ...
    
    @add_start_docstrings_to_model_forward(ENCODER_DECODER_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=FlaxSeq2SeqLMOutput, config_class=_CONFIG_FOR_DOC)
    def __call__(self, input_ids: jnp.ndarray, attention_mask: Optional[jnp.ndarray] = ..., decoder_input_ids: Optional[jnp.ndarray] = ..., decoder_attention_mask: Optional[jnp.ndarray] = ..., position_ids: Optional[jnp.ndarray] = ..., decoder_position_ids: Optional[jnp.ndarray] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., train: bool = ..., params: dict = ..., dropout_rng: PRNGKey = ...):
        r"""
        Returns:

        Examples:

        ```python
        >>> from transformers import FlaxEncoderDecoderModel, BertTokenizer, GPT2Tokenizer

        >>> # load a fine-tuned bert2gpt2 model
        >>> model = FlaxEncoderDecoderModel.from_pretrained("patrickvonplaten/bert2gpt2-cnn_dailymail-fp16")
        >>> # load input & output tokenizer
        >>> tokenizer_input = BertTokenizer.from_pretrained("google-bert/bert-base-cased")
        >>> tokenizer_output = GPT2Tokenizer.from_pretrained("openai-community/gpt2")

        >>> article = '''Sigma Alpha Epsilon is under fire for a video showing party-bound fraternity members
        >>> singing a racist chant. SAE's national chapter suspended the students,
        >>> but University of Oklahoma President David Boren took it a step further,
        >>> saying the university's affiliation with the fraternity is permanently done.'''

        >>> input_ids = tokenizer_input(article, add_special_tokens=True, return_tensors="np").input_ids

        >>> # use GPT2's eos_token as the pad as well as eos token
        >>> model.config.eos_token_id = model.config.decoder.eos_token_id
        >>> model.config.pad_token_id = model.config.eos_token_id

        >>> sequences = model.generate(input_ids, num_beams=4, max_length=12).sequences

        >>> summary = tokenizer_output.batch_decode(sequences, skip_special_tokens=True)[0]
        >>> assert summary == "SAS Alpha Epsilon suspended Sigma Alpha Epsilon members"
        ```
        """
        ...
    
    def prepare_inputs_for_generation(self, decoder_input_ids, max_length, attention_mask: Optional[jax.Array] = ..., decoder_attention_mask: Optional[jax.Array] = ..., encoder_outputs=..., **kwargs): # -> dict[str, Any]:
        ...
    
    def update_inputs_for_generation(self, model_outputs, model_kwargs):
        ...
    
    @classmethod
    def from_encoder_decoder_pretrained(cls, encoder_pretrained_model_name_or_path: Optional[Union[str, os.PathLike]] = ..., decoder_pretrained_model_name_or_path: Optional[Union[str, os.PathLike]] = ..., *model_args, **kwargs) -> FlaxPreTrainedModel:
        r"""
        Instantiate an encoder and a decoder from one or two base classes of the library from pretrained model
        checkpoints.

        Params:
            encoder_pretrained_model_name_or_path (`Union[str, os.PathLike]`, *optional*):
                Information necessary to initiate the encoder. Can be either:

                    - A string, the *model id* of a pretrained model hosted inside a model repo on huggingface.co.
                    - A path to a *directory* containing model weights saved using
                      [`~FlaxPreTrainedModel.save_pretrained`], e.g., `./my_model_directory/`.

            decoder_pretrained_model_name_or_path (`Union[str, os.PathLike]`, *optional*, defaults to `None`):
                Information necessary to initiate the decoder. Can be either:

                    - A string, the *model id* of a pretrained model hosted inside a model repo on huggingface.co.
                    - A path to a *directory* containing model weights saved using
                      [`~FlaxPreTrainedModel.save_pretrained`], e.g., `./my_model_directory/`.

            model_args (remaining positional arguments, *optional*):
                All remaning positional arguments will be passed to the underlying model's `__init__` method.

            kwargs (remaining dictionary of keyword arguments, *optional*):
                Can be used to update the configuration object (after it being loaded) and initiate the model (e.g.,
                `output_attentions=True`).

                - To update the encoder configuration, use the prefix *encoder_* for each configuration parameter.
                - To update the decoder configuration, use the prefix *decoder_* for each configuration parameter.
                - To update the parent model configuration, do not use a prefix for each configuration parameter.

                Behaves differently depending on whether a `config` is provided or automatically loaded.

        Example:

        ```python
        >>> from transformers import FlaxEncoderDecoderModel

        >>> # initialize a bert2gpt2 from pretrained BERT and GPT2 models. Note that the cross-attention layers will be randomly initialized
        >>> model = FlaxEncoderDecoderModel.from_encoder_decoder_pretrained("google-bert/bert-base-cased", "openai-community/gpt2")
        >>> # saving model after fine-tuning
        >>> model.save_pretrained("./bert2gpt2")
        >>> # load fine-tuned model
        >>> model = FlaxEncoderDecoderModel.from_pretrained("./bert2gpt2")
        ```"""
        ...
    

