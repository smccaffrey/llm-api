"""
This type stub file was generated by pyright.
"""

from typing import Mapping
from ...configuration_utils import PretrainedConfig
from ...onnx import OnnxConfig

"""PoolFormer model configuration"""
logger = ...
class PoolFormerConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of [`PoolFormerModel`]. It is used to instantiate a
    PoolFormer model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the PoolFormer
    [sail/poolformer_s12](https://huggingface.co/sail/poolformer_s12) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        num_channels (`int`, *optional*, defaults to 3):
            The number of channels in the input image.
        patch_size (`int`, *optional*, defaults to 16):
            The size of the input patch.
        stride (`int`, *optional*, defaults to 16):
            The stride of the input patch.
        pool_size (`int`, *optional*, defaults to 3):
            The size of the pooling window.
        mlp_ratio (`float`, *optional*, defaults to 4.0):
            The ratio of the number of channels in the output of the MLP to the number of channels in the input.
        depths (`list`, *optional*, defaults to `[2, 2, 6, 2]`):
            The depth of each encoder block.
        hidden_sizes (`list`, *optional*, defaults to `[64, 128, 320, 512]`):
            The hidden sizes of each encoder block.
        patch_sizes (`list`, *optional*, defaults to `[7, 3, 3, 3]`):
            The size of the input patch for each encoder block.
        strides (`list`, *optional*, defaults to `[4, 2, 2, 2]`):
            The stride of the input patch for each encoder block.
        padding (`list`, *optional*, defaults to `[2, 1, 1, 1]`):
            The padding of the input patch for each encoder block.
        num_encoder_blocks (`int`, *optional*, defaults to 4):
            The number of encoder blocks.
        drop_path_rate (`float`, *optional*, defaults to 0.0):
            The dropout rate for the dropout layers.
        hidden_act (`str`, *optional*, defaults to `"gelu"`):
            The activation function for the hidden layers.
        use_layer_scale (`bool`, *optional*, defaults to `True`):
            Whether to use layer scale.
        layer_scale_init_value (`float`, *optional*, defaults to 1e-05):
            The initial value for the layer scale.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The initializer range for the weights.

    Example:

    ```python
    >>> from transformers import PoolFormerConfig, PoolFormerModel

    >>> # Initializing a PoolFormer sail/poolformer_s12 style configuration
    >>> configuration = PoolFormerConfig()

    >>> # Initializing a model (with random weights) from the sail/poolformer_s12 style configuration
    >>> model = PoolFormerModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```
    """
    model_type = ...
    def __init__(self, num_channels=..., patch_size=..., stride=..., pool_size=..., mlp_ratio=..., depths=..., hidden_sizes=..., patch_sizes=..., strides=..., padding=..., num_encoder_blocks=..., drop_path_rate=..., hidden_act=..., use_layer_scale=..., layer_scale_init_value=..., initializer_range=..., **kwargs) -> None:
        ...
    


class PoolFormerOnnxConfig(OnnxConfig):
    torch_onnx_minimum_version = ...
    @property
    def inputs(self) -> Mapping[str, Mapping[int, str]]:
        ...
    
    @property
    def atol_for_validation(self) -> float:
        ...
    

