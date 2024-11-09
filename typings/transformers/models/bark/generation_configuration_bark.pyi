"""
This type stub file was generated by pyright.
"""

from typing import Dict
from ...generation.configuration_utils import GenerationConfig

"""BARK model generation configuration"""
logger = ...
class BarkSemanticGenerationConfig(GenerationConfig):
    model_type = ...
    def __init__(self, eos_token_id=..., renormalize_logits=..., max_new_tokens=..., output_scores=..., return_dict_in_generate=..., output_hidden_states=..., output_attentions=..., temperature=..., do_sample=..., text_encoding_offset=..., text_pad_token=..., semantic_infer_token=..., semantic_vocab_size=..., max_input_semantic_length=..., semantic_rate_hz=..., min_eos_p=..., **kwargs) -> None:
        """Class that holds a generation configuration for [`BarkSemanticModel`].

        This configuration inherit from [`GenerationConfig`] and can be used to control the model generation. Read the
        documentation from [`GenerationConfig`] for more information.

        Args:
            eos_token_id (`int`, *optional*, defaults to 10_000):
                The id of the *end-of-sequence* token.
            renormalize_logits (`bool`, *optional*, defaults to `True`):
                Whether to renormalize the logits after applying all the logits processors (including the
                custom ones). It's highly recommended to set this flag to `True` as the search algorithms suppose the
                score logits are normalized but some logit processors break the normalization.
            max_new_tokens (`int`, *optional*, defaults to 768):
                The maximum numbers of tokens to generate, ignoring the number of tokens in the prompt.
            output_scores (`bool`, *optional*, defaults to `False`):
                Whether or not to return the prediction scores. See `scores` under returned tensors for more details.
            return_dict_in_generate (`bool`, *optional*, defaults to `False`):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
            output_hidden_states (`bool`, *optional*, defaults to `False`):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more details.
            output_attentions (`bool`, *optional*, defaults to `False`):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more details.
            temperature (`float`, *optional*, defaults to 1.0):
                The value used to modulate the next token probabilities.
            do_sample (`bool`, *optional*, defaults to `False`):
                Whether or not to use sampling ; use greedy decoding otherwise.
            text_encoding_offset (`int`, *optional*, defaults to 10_048):
                Text encoding offset.
            text_pad_token (`int`, *optional*, defaults to 129_595):
                Text pad token.
            semantic_infer_token (`int`, *optional*, defaults to 129_599):
                Semantic infer token.
            semantic_vocab_size (`int`, *optional*, defaults to 10_000):
                Semantic vocab size.
            max_input_semantic_length (`int`, *optional*, defaults to 256):
                Max length of semantic input vector.
            semantic_rate_hz (`float`, *optional*, defaults to 49.9):
                Semantic rate in Hertz.
            min_eos_p (`float`, *optional*):
                Minimum threshold of the probability of the EOS token for it to be sampled. This is an early stopping
                strategy to mitigate potential unwanted generations at the end of a prompt. The original implementation
                suggests a default value of 0.2.
        """
        ...
    


class BarkCoarseGenerationConfig(GenerationConfig):
    model_type = ...
    def __init__(self, renormalize_logits=..., output_scores=..., return_dict_in_generate=..., output_hidden_states=..., output_attentions=..., temperature=..., do_sample=..., coarse_semantic_pad_token=..., coarse_rate_hz=..., n_coarse_codebooks=..., coarse_infer_token=..., max_coarse_input_length=..., max_coarse_history: int = ..., sliding_window_len: int = ..., **kwargs) -> None:
        """Class that holds a generation configuration for [`BarkCoarseModel`].

        This configuration inherit from [`GenerationConfig`] and can be used to control the model generation. Read the
        documentation from [`GenerationConfig`] for more information.

        Args:
            renormalize_logits (`bool`, *optional*, defaults to `True`):
                Whether to renormalize the logits after applying all the logits processors (including the
                custom ones). It's highly recommended to set this flag to `True` as the search algorithms suppose the
                score logits are normalized but some logit processors break the normalization.
            output_scores (`bool`, *optional*, defaults to `False`):
                Whether or not to return the prediction scores. See `scores` under returned tensors for more details.
            return_dict_in_generate (`bool`, *optional*, defaults to `False`):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
            output_hidden_states (`bool`, *optional*, defaults to `False`):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more details.
            output_attentions (`bool`, *optional*, defaults to `False`):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more details.
            temperature (`float`, *optional*, defaults to 1.0):
                The value used to modulate the next token probabilities.
            do_sample (`bool`, *optional*, defaults to `False`):
                Whether or not to use sampling ; use greedy decoding otherwise.
            coarse_semantic_pad_token (`int`, *optional*, defaults to 12_048):
                Coarse semantic pad token.
            coarse_rate_hz (`int`, *optional*, defaults to 75):
                Coarse rate in Hertz.
            n_coarse_codebooks (`int`, *optional*, defaults to 2):
                Number of coarse codebooks.
            coarse_infer_token (`int`, *optional*, defaults to 12_050):
                Coarse infer token.
            max_coarse_input_length (`int`, *optional*, defaults to 256):
                Max length of input coarse vector.
            max_coarse_history (`int`, *optional*, defaults to 630):
                Max length of the output of the coarse acoustics model used in the fine generation step.
            sliding_window_len (`int`, *optional*, defaults to 60):
                The coarse generation step uses a sliding window to generate raw audio.
        """
        ...
    


class BarkFineGenerationConfig(GenerationConfig):
    model_type = ...
    def __init__(self, temperature=..., max_fine_history_length=..., max_fine_input_length=..., n_fine_codebooks=..., **kwargs) -> None:
        """Class that holds a generation configuration for [`BarkFineModel`].

        [`BarkFineModel`] is an autoencoder model, so should not usually be used for generation. However, under the
        hood, it uses `temperature` when used by [`BarkModel`]

        This configuration inherit from [`GenerationConfig`] and can be used to control the model generation. Read the
        documentation from [`GenerationConfig`] for more information.

        Args:
            temperature (`float`, *optional*):
                The value used to modulate the next token probabilities.
            max_fine_history_length (`int`, *optional*, defaults to 512):
                Max length of the fine history vector.
            max_fine_input_length (`int`, *optional*, defaults to 1024):
                Max length of fine input vector.
            n_fine_codebooks (`int`, *optional*, defaults to 8):
                Number of codebooks used.
        """
        ...
    
    def validate(self, **kwargs): # -> None:
        """
        Overrides GenerationConfig.validate because BarkFineGenerationConfig don't use any parameters outside
        temperature.
        """
        ...
    


class BarkGenerationConfig(GenerationConfig):
    model_type = ...
    is_composition = ...
    def __init__(self, semantic_config: Dict = ..., coarse_acoustics_config: Dict = ..., fine_acoustics_config: Dict = ..., sample_rate=..., codebook_size=..., **kwargs) -> None:
        """Class that holds a generation configuration for [`BarkModel`].

        The [`BarkModel`] does not have a `generate` method, but uses this class to generate speeches with a nested
        [`BarkGenerationConfig`] which uses [`BarkSemanticGenerationConfig`], [`BarkCoarseGenerationConfig`],
        [`BarkFineGenerationConfig`].

        This configuration inherit from [`GenerationConfig`] and can be used to control the model generation. Read the
        documentation from [`GenerationConfig`] for more information.

        Args:
            semantic_config (`Dict`, *optional*):
                Semantic generation configuration.
            coarse_acoustics_config (`Dict`, *optional*):
                Coarse generation configuration.
            fine_acoustics_config (`Dict`, *optional*):
                Fine generation configuration.
            sample_rate (`int`, *optional*, defaults to 24_000):
                Sample rate.
            codebook_size (`int`, *optional*, defaults to 1024):
                Vector length for each codebook.
        """
        ...
    
    @classmethod
    def from_sub_model_configs(cls, semantic_config: BarkSemanticGenerationConfig, coarse_acoustics_config: BarkCoarseGenerationConfig, fine_acoustics_config: BarkFineGenerationConfig, **kwargs): # -> Self:
        r"""
        Instantiate a [`BarkGenerationConfig`] (or a derived class) from bark sub-models generation configuration.

        Returns:
            [`BarkGenerationConfig`]: An instance of a configuration object
        """
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        """
        Serializes this instance to a Python dictionary. Override the default [`~PretrainedConfig.to_dict`].

        Returns:
            `Dict[str, any]`: Dictionary of all the attributes that make up this configuration instance,
        """
        ...
    

