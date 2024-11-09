"""
This type stub file was generated by pyright.
"""

from typing import Mapping
from ...configuration_utils import PretrainedConfig
from ...onnx import OnnxConfig

"""BigBird model configuration"""
logger = ...
class BigBirdConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`BigBirdModel`]. It is used to instantiate an
    BigBird model according to the specified arguments, defining the model architecture. Instantiating a configuration
    with the defaults will yield a similar configuration to that of the BigBird
    [google/bigbird-roberta-base](https://huggingface.co/google/bigbird-roberta-base) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 50358):
            Vocabulary size of the BigBird model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`BigBirdModel`].
        hidden_size (`int`, *optional*, defaults to 768):
            Dimension of the encoder layers and the pooler layer.
        num_hidden_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        intermediate_size (`int`, *optional*, defaults to 3072):
            Dimension of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu_new"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        max_position_embeddings (`int`, *optional*, defaults to 4096):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 1024 or 2048 or 4096).
        type_vocab_size (`int`, *optional*, defaults to 2):
            The vocabulary size of the `token_type_ids` passed when calling [`BigBirdModel`].
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        is_decoder (`bool`, *optional*, defaults to `False`):
            Whether the model is used as a decoder or not. If `False`, the model is used as an encoder.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models). Only
            relevant if `config.is_decoder=True`.
        attention_type (`str`, *optional*, defaults to `"block_sparse"`)
            Whether to use block sparse attention (with n complexity) as introduced in paper or original attention
            layer (with n^2 complexity). Possible values are `"original_full"` and `"block_sparse"`.
        use_bias (`bool`, *optional*, defaults to `True`)
            Whether to use bias in query, key, value.
        rescale_embeddings (`bool`, *optional*, defaults to `False`)
            Whether to rescale embeddings with (hidden_size ** 0.5).
        block_size (`int`, *optional*, defaults to 64)
            Size of each block. Useful only when `attention_type == "block_sparse"`.
        num_random_blocks (`int`, *optional*, defaults to 3)
            Each query is going to attend these many number of random blocks. Useful only when `attention_type ==
            "block_sparse"`.
        classifier_dropout (`float`, *optional*):
            The dropout ratio for the classification head.

    Example:

    ```python
    >>> from transformers import BigBirdConfig, BigBirdModel

    >>> # Initializing a BigBird google/bigbird-roberta-base style configuration
    >>> configuration = BigBirdConfig()

    >>> # Initializing a model (with random weights) from the google/bigbird-roberta-base style configuration
    >>> model = BigBirdModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""
    model_type = ...
    def __init__(self, vocab_size=..., hidden_size=..., num_hidden_layers=..., num_attention_heads=..., intermediate_size=..., hidden_act=..., hidden_dropout_prob=..., attention_probs_dropout_prob=..., max_position_embeddings=..., type_vocab_size=..., initializer_range=..., layer_norm_eps=..., use_cache=..., pad_token_id=..., bos_token_id=..., eos_token_id=..., sep_token_id=..., attention_type=..., use_bias=..., rescale_embeddings=..., block_size=..., num_random_blocks=..., classifier_dropout=..., **kwargs) -> None:
        ...
    


class BigBirdOnnxConfig(OnnxConfig):
    @property
    def inputs(self) -> Mapping[str, Mapping[int, str]]:
        ...
    

