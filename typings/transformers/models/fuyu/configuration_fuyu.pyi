"""
This type stub file was generated by pyright.
"""

from ...configuration_utils import PretrainedConfig

"""Fuyu model configuration"""
logger = ...
class FuyuConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`FuyuForCausalLM`]. It is used to instantiate an
    Fuyu model according to the specified arguments, defining the model architecture. Instantiating a configuration
    with the defaults will yield a similar configuration to that of the
    [adept/fuyu-8b](https://huggingface.co/adept/fuyu-8b).

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 262144):
            Vocabulary size of the Fuyu model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`FuyuForCausalLM`]
        hidden_size (`int`, *optional*, defaults to 4096):
            Dimension of the hidden representations.
        intermediate_size (`int`, *optional*, defaults to 16384):
            Dimension of the MLP representations.
        num_hidden_layers (`int`, *optional*, defaults to 36):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 64):
            Number of attention heads for each attention layer in the Transformer encoder.
        hidden_act (`str` or `function`, *optional*, defaults to `"relu2"`):
            The non-linear activation function (function or string) in the decoder.
        max_position_embeddings (`int`, *optional*, defaults to 16384):
            The maximum sequence length that this model might ever be used with.
        image_size (`int`, *optional*, defaults to 300):
            The input image size.
        patch_size (`int`, *optional*, defaults to 30):
            The input vision transformer encoding patch size.
        num_channels (`int`, *optional*, defaults to 3):
            The input image number of channels.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-05):
            The epsilon used by the rms normalization layers.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models). Only
            relevant if `config.is_decoder=True`. Whether to tie weight embeddings
        tie_word_embeddings (`bool`, *optional*, defaults to `False`):
            Whether to tie input and output embeddings.
        rope_theta (`float`, *optional*, defaults to 25000.0):
            The base period of the RoPE embeddings.
        rope_scaling (`Dict`, *optional*):
            Dictionary containing the scaling configuration for the RoPE embeddings. Currently supports two scaling
            strategies: linear and dynamic. Their scaling factor must be a float greater than 1. The expected format is
            `{"type": strategy name, "factor": scaling factor}`. When using this flag, don't update
            `max_position_embeddings` to the expected new maximum. See the following thread for more information on how
            these scaling strategies behave:
            https://www.reddit.com/r/LocalFuyu/comments/14mrgpr/dynamically_scaled_rope_further_increases/. This is an
            experimental feature, subject to breaking API changes in future versions.
        qk_layernorm (`bool`, *optional*, defaults to `True`):
            Whether or not to normalize the Queries and Keys after projecting the hidden states
        hidden_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio after applying the MLP to the hidden states.
        attention_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio after computing the attention scores.
        partial_rotary_factor (`float`, *optional*, defaults to 0.5):
            Percentage of the query and keys which will have rotary embedding.

        pad_token_id (`int`, *optional*):
            The id of the *padding* token.
        bos_token_id (`int`, *optional*, defaults to 1):
            The id of the *beginning-of-sequence* token.
        eos_token_id (`Union[int, List[int]]`, *optional*, defaults to 2):
            The id of the *end-of-sequence* token. Optionally, use a list to set multiple *end-of-sequence* tokens.
        text_config (`dict`, *optional*):
            Dictionary of configuration options used to initialize the `language``[`Aut`].

    ```python
    >>> from transformers import FuyuConfig

    >>> # Initializing a Fuyu fuyu-7b style configuration
    >>> configuration = FuyuConfig()
    ```"""
    model_type = ...
    keys_to_ignore_at_inference = ...
    def __init__(self, vocab_size=..., hidden_size=..., intermediate_size=..., num_hidden_layers=..., num_attention_heads=..., hidden_act=..., max_position_embeddings=..., image_size=..., patch_size=..., num_channels=..., initializer_range=..., layer_norm_eps=..., use_cache=..., tie_word_embeddings=..., rope_theta=..., rope_scaling=..., qk_layernorm=..., hidden_dropout=..., attention_dropout=..., partial_rotary_factor=..., pad_token_id=..., bos_token_id=..., eos_token_id=..., text_config=..., **kwargs) -> None:
        ...
    

