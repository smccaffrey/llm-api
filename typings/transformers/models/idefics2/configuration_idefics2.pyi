"""
This type stub file was generated by pyright.
"""

import os
from typing import Union
from ...configuration_utils import PretrainedConfig

"""Idefics2 model configuration"""
logger = ...
class Idefics2VisionConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`Idefics2VisionModel`]. It is used to instantiate a
    Idefics2 vision encoder according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the SigLIP checkpoint
    [google/siglip-base-patch16-224](https://huggingface.co/google/siglip-base-patch16-224) used in the Idefics2 model
    [HuggingFaceM4/idefics2-8b](https://huggingface.co/HuggingFaceM4/idefics2-8b).

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        hidden_size (`int`, *optional*, defaults to 768):
            Dimensionality of the encoder layers and the pooler layer.
        intermediate_size (`int`, *optional*, defaults to 3072):
            Dimensionality of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.
        num_hidden_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        num_channels (`int`, *optional*, defaults to 3):
            Number of channels in the input images.
        image_size (`int`, *optional*, defaults to 224):
            The size (resolution) of each image.
        patch_size (`int`, *optional*, defaults to 32):
            The size (resolution) of each patch.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu_pytorch_tanh"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` `"quick_gelu"` are supported.
        layer_norm_eps (`float`, *optional*, defaults to 1e-06):
            The epsilon used by the layer normalization layers.
        attention_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation for initializing all weight matrices in the model.

    Example:

    ```python
    >>> from transformers.models.idefics2.modeling_idefics2 import Idefics2VisionTransformer
    >>> from transformers.models.idefics2.configuration_idefics2 import Idefics2VisionConfig

    >>> # Initializing a Idefics2VisionConfig with google/siglip-base-patch16-224 style configuration
    >>> configuration = Idefics2VisionConfig()

    >>> # Initializing a Idefics2VisionTransformer (with random weights) from the google/siglip-base-patch16-224 style configuration
    >>> model = Idefics2VisionTransformer(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""
    model_type = ...
    def __init__(self, hidden_size=..., intermediate_size=..., num_hidden_layers=..., num_attention_heads=..., num_channels=..., image_size=..., patch_size=..., hidden_act=..., layer_norm_eps=..., attention_dropout=..., initializer_range=..., **kwargs) -> None:
        ...
    
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path: Union[str, os.PathLike], **kwargs) -> PretrainedConfig:
        ...
    


class Idefics2PerceiverConfig(PretrainedConfig):
    r"""
    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        hidden_act (`str` or `function`, *optional*, defaults to `"silu"`):
            The non-linear activation function (function or string) in the perceiver block.
        hidden_size (`int`, *optional*, defaults to 4096):
            Dimension of the hidden representations.
        rms_norm_eps (`float`, *optional*, defaults to 1e-06):
            The epsilon used by the rms normalization layers.
        resampler_n_latents (`int`, *optional*, defaults to 64):
            Number of latent embeddings to resample ("compress") the input sequence to (usually < 128).
        resampler_depth (`int`, *optional*, defaults to 3):
            Depth of the Perceiver Resampler (Transformer w/ cross attention). Should be shallow (<= 3).
        resampler_n_heads (`int`, *optional*, defaults to 16):
            Number of heads in each Transformer block (for multi-headed self-attention).
        resampler_head_dim (`int`, *optional*, defaults to 96):
            Dimensionality of each head projection in the Transformer block.
        num_key_value_heads (`int`, *optional*, defaults to 4):
            Number of key-value heads in the perceiver attention block.
        attention_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
    """
    model_type = ...
    def __init__(self, hidden_act=..., hidden_size=..., rms_norm_eps=..., resampler_n_latents=..., resampler_depth=..., resampler_n_heads=..., resampler_head_dim=..., num_key_value_heads=..., attention_dropout=..., **kwargs) -> None:
        ...
    


class Idefics2Config(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`Idefics2Model`]. It is used to instantiate a
    Idefics2 model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the model of the Idefics2
    [HuggingFaceM4/idefics2-8b](https://huggingface.co/HuggingFaceM4/idefics2-8b) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should cache the key/value pairs of the attention mechanism.
        image_token_id (`int`, *optional*, defaults to 32001):
            The id of the "image" token.
        tie_word_embeddings (`bool`, *optional*, defaults to `False`):
            Whether or not to tie the word embeddings with the token embeddings.
        vision_config (`IdeficsVisionConfig` or `dict`, *optional*):
            Custom vision config or dict
        perceiver_config (`IdeficsPerceiverConfig` or `dict`, *optional*):
            Custom perceiver config or dict
        text_config (`MistralConfig` or `dict`, *optional*):
            Custom text config or dict for the text model

    Example:
    ```python
    >>> from transformers import Idefics2Model, Idefics2Config
    >>> # Initializing configuration
    >>> configuration = Idefics2Config()
    >>> # Initializing a model from the configuration
    >>> model = Idefics2Model(configuration)
    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""
    model_type = ...
    is_composition = ...
    def __init__(self, use_cache=..., image_token_id=..., tie_word_embeddings=..., vision_config=..., perceiver_config=..., text_config=..., **kwargs) -> None:
        ...
    

