"""
This type stub file was generated by pyright.
"""

from typing import Mapping
from ...configuration_utils import PretrainedConfig
from ...onnx import OnnxConfig

"""MobileBERT model configuration"""
logger = ...
class MobileBertConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`MobileBertModel`] or a [`TFMobileBertModel`]. It
    is used to instantiate a MobileBERT model according to the specified arguments, defining the model architecture.
    Instantiating a configuration with the defaults will yield a similar configuration to that of the MobileBERT
    [google/mobilebert-uncased](https://huggingface.co/google/mobilebert-uncased) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 30522):
            Vocabulary size of the MobileBERT model. Defines the number of different tokens that can be represented by
            the `inputs_ids` passed when calling [`MobileBertModel`] or [`TFMobileBertModel`].
        hidden_size (`int`, *optional*, defaults to 512):
            Dimensionality of the encoder layers and the pooler layer.
        num_hidden_layers (`int`, *optional*, defaults to 24):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 4):
            Number of attention heads for each attention layer in the Transformer encoder.
        intermediate_size (`int`, *optional*, defaults to 512):
            Dimensionality of the "intermediate" (often named feed-forward) layer in the Transformer encoder.
        hidden_act (`str` or `function`, *optional*, defaults to `"relu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"silu"` and `"gelu_new"` are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.0):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        max_position_embeddings (`int`, *optional*, defaults to 512):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        type_vocab_size (`int`, *optional*, defaults to 2):
            The vocabulary size of the `token_type_ids` passed when calling [`MobileBertModel`] or
            [`TFMobileBertModel`].
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.

        pad_token_id (`int`, *optional*, defaults to 0):
            The ID of the token in the word embedding to use as padding.
        embedding_size (`int`, *optional*, defaults to 128):
            The dimension of the word embedding vectors.
        trigram_input (`bool`, *optional*, defaults to `True`):
            Use a convolution of trigram as input.
        use_bottleneck (`bool`, *optional*, defaults to `True`):
            Whether to use bottleneck in BERT.
        intra_bottleneck_size (`int`, *optional*, defaults to 128):
            Size of bottleneck layer output.
        use_bottleneck_attention (`bool`, *optional*, defaults to `False`):
            Whether to use attention inputs from the bottleneck transformation.
        key_query_shared_bottleneck (`bool`, *optional*, defaults to `True`):
            Whether to use the same linear transformation for query&key in the bottleneck.
        num_feedforward_networks (`int`, *optional*, defaults to 4):
            Number of FFNs in a block.
        normalization_type (`str`, *optional*, defaults to `"no_norm"`):
            The normalization type in MobileBERT.
        classifier_dropout (`float`, *optional*):
            The dropout ratio for the classification head.

    Examples:

    ```python
    >>> from transformers import MobileBertConfig, MobileBertModel

    >>> # Initializing a MobileBERT configuration
    >>> configuration = MobileBertConfig()

    >>> # Initializing a model (with random weights) from the configuration above
    >>> model = MobileBertModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```
    """
    model_type = ...
    def __init__(self, vocab_size=..., hidden_size=..., num_hidden_layers=..., num_attention_heads=..., intermediate_size=..., hidden_act=..., hidden_dropout_prob=..., attention_probs_dropout_prob=..., max_position_embeddings=..., type_vocab_size=..., initializer_range=..., layer_norm_eps=..., pad_token_id=..., embedding_size=..., trigram_input=..., use_bottleneck=..., intra_bottleneck_size=..., use_bottleneck_attention=..., key_query_shared_bottleneck=..., num_feedforward_networks=..., normalization_type=..., classifier_activation=..., classifier_dropout=..., **kwargs) -> None:
        ...
    


class MobileBertOnnxConfig(OnnxConfig):
    @property
    def inputs(self) -> Mapping[str, Mapping[int, str]]:
        ...
    

