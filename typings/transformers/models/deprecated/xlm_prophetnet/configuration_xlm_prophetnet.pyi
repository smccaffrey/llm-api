"""
This type stub file was generated by pyright.
"""

from typing import Callable, Optional, Union
from ....configuration_utils import PretrainedConfig

"""XLM-ProphetNet model configuration"""
logger = ...
class XLMProphetNetConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`XLMProphetNetModel`]. It is used to instantiate a
    XLMProphetNet model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the XLMProphetNet
    [microsoft/xprophetnet-large-wiki100-cased](https://huggingface.co/microsoft/xprophetnet-large-wiki100-cased)
    architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        activation_dropout (`float`, *optional*, defaults to 0.1):
            The dropout ratio for activations inside the fully connected layer.
        activation_function (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"silu"` and `"gelu_new"` are supported.
        vocab_size (`int`, *optional*, defaults to 30522):
            Vocabulary size of the ProphetNET model. Defines the number of different tokens that can be represented by
            the `inputs_ids` passed when calling [`XLMProphetNetModel`].
        hidden_size (`int`, *optional*, defaults to 1024):
            Dimensionality of the layers and the pooler layer.
        encoder_ffn_dim (`int`, *optional*, defaults to 4096):
            Dimensionality of the "intermediate" (often named feed-forward) layer in decoder.
        num_encoder_layers (`int`, *optional*, defaults to 12):
            Number of encoder layers.
        num_encoder_attention_heads (`int`, *optional*, defaults to 16):
            Number of attention heads for each attention layer in the Transformer encoder.
        decoder_ffn_dim (`int`, *optional*, defaults to 4096):
            Dimensionality of the `intermediate` (often named feed-forward) layer in decoder.
        num_decoder_layers (`int`, *optional*, defaults to 12):
            Number of decoder layers.
        num_decoder_attention_heads (`int`, *optional*, defaults to 16):
            Number of attention heads for each attention layer in the Transformer decoder.
        attention_dropout (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        dropout (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        max_position_embeddings (`int`, *optional*, defaults to 512):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        init_std (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        add_cross_attention (`bool`, *optional*, defaults to `True`):
            Whether cross-attention layers should be added to the model.
        is_encoder_decoder (`bool`, *optional*, defaults to `True`):
            Whether this is an encoder/decoder model.
        pad_token_id (`int`, *optional*, defaults to 1)
            Padding token id.
        bos_token_id (`int`, *optional*, defaults to 0)
            Beginning of stream token id.
        eos_token_id (`int`, *optional*, defaults to 2)
            End of stream token id.
        ngram (`int`, *optional*, defaults to 2)
            Number of future tokens to predict. Set to 1 to be same as traditional Language model to predict next first
            token.
        num_buckets (`int`, *optional*, defaults to 32)
            The number of buckets to use for each attention layer. This is for relative position calculation. See the
            [T5 paper](see https://arxiv.org/abs/1910.10683) for more details.
        relative_max_distance (`int`, *optional*, defaults to 128)
            Relative distances greater than this number will be put into the last same bucket. This is for relative
            position calculation. See the [T5 paper](see https://arxiv.org/abs/1910.10683) for more details.
        disable_ngram_loss (`bool`, *optional*, defaults to `False`):
            Whether be trained predicting only the next first token.
        eps (`float`, *optional*, defaults to 0.0):
            Controls the `epsilon` parameter value for label smoothing in the loss calculation. If set to 0, no label
            smoothing is performed.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models).
    """
    model_type = ...
    keys_to_ignore_at_inference = ...
    attribute_map = ...
    def __init__(self, activation_dropout: Optional[float] = ..., activation_function: Optional[Union[str, Callable]] = ..., vocab_size: Optional[int] = ..., hidden_size: Optional[int] = ..., encoder_ffn_dim: Optional[int] = ..., num_encoder_layers: Optional[int] = ..., num_encoder_attention_heads: Optional[int] = ..., decoder_ffn_dim: Optional[int] = ..., num_decoder_layers: Optional[int] = ..., num_decoder_attention_heads: Optional[int] = ..., attention_dropout: Optional[float] = ..., dropout: Optional[float] = ..., max_position_embeddings: Optional[int] = ..., init_std: Optional[float] = ..., is_encoder_decoder: Optional[bool] = ..., add_cross_attention: Optional[bool] = ..., decoder_start_token_id: Optional[int] = ..., ngram: Optional[int] = ..., num_buckets: Optional[int] = ..., relative_max_distance: Optional[int] = ..., disable_ngram_loss: Optional[bool] = ..., eps: Optional[float] = ..., use_cache: Optional[bool] = ..., pad_token_id: Optional[int] = ..., bos_token_id: Optional[int] = ..., eos_token_id: Optional[int] = ..., **kwargs) -> None:
        ...
    
    @property
    def num_hidden_layers(self) -> int:
        ...
    
    @num_hidden_layers.setter
    def num_hidden_layers(self, value):
        ...
    


