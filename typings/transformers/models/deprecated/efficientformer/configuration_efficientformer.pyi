"""
This type stub file was generated by pyright.
"""

from typing import List
from ....configuration_utils import PretrainedConfig

"""EfficientFormer model configuration"""
logger = ...
class EfficientFormerConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of an [`EfficientFormerModel`]. It is used to
    instantiate an EfficientFormer model according to the specified arguments, defining the model architecture.
    Instantiating a configuration with the defaults will yield a similar configuration to that of the EfficientFormer
    [snap-research/efficientformer-l1](https://huggingface.co/snap-research/efficientformer-l1) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        depths (`List(int)`, *optional*, defaults to `[3, 2, 6, 4]`)
            Depth of each stage.
        hidden_sizes (`List(int)`, *optional*, defaults to `[48, 96, 224, 448]`)
            Dimensionality of each stage.
        downsamples (`List(bool)`, *optional*, defaults to `[True, True, True, True]`)
            Whether or not to downsample inputs between two stages.
        dim (`int`, *optional*, defaults to 448):
            Number of channels in Meta3D layers
        key_dim (`int`, *optional*, defaults to 32):
            The size of the key in meta3D block.
        attention_ratio (`int`, *optional*, defaults to 4):
            Ratio of the dimension of the query and value to the dimension of the key in MSHA block
        resolution (`int`, *optional*, defaults to 7)
            Size of each patch
        num_hidden_layers (`int`, *optional*, defaults to 5):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 8):
            Number of attention heads for each attention layer in the 3D MetaBlock.
        mlp_expansion_ratio (`int`, *optional*, defaults to 4):
            Ratio of size of the hidden dimensionality of an MLP to the dimensionality of its input.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings and encoder.
        patch_size (`int`, *optional*, defaults to 16):
            The size (resolution) of each patch.
        num_channels (`int`, *optional*, defaults to 3):
            The number of input channels.
        pool_size (`int`, *optional*, defaults to 3):
            Kernel size of pooling layers.
        downsample_patch_size (`int`, *optional*, defaults to 3):
            The size of patches in downsampling layers.
        downsample_stride (`int`, *optional*, defaults to 2):
            The stride of convolution kernels in downsampling layers.
        downsample_pad (`int`, *optional*, defaults to 1):
            Padding in downsampling layers.
        drop_path_rate (`int`, *optional*, defaults to 0):
            Rate at which to increase dropout probability in DropPath.
        num_meta3d_blocks (`int`, *optional*, defaults to 1):
            The number of 3D MetaBlocks in the last stage.
        distillation (`bool`, *optional*, defaults to `True`):
            Whether to add a distillation head.
        use_layer_scale (`bool`, *optional*, defaults to `True`):
            Whether to scale outputs from token mixers.
        layer_scale_init_value (`float`, *optional*, defaults to 1e-5):
            Factor by which outputs from token mixers are scaled.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` are supported.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        image_size (`int`, *optional*, defaults to `224`):
            The size (resolution) of each image.

    Example:

    ```python
    >>> from transformers import EfficientFormerConfig, EfficientFormerModel

    >>> # Initializing a EfficientFormer efficientformer-l1 style configuration
    >>> configuration = EfficientFormerConfig()

    >>> # Initializing a EfficientFormerModel (with random weights) from the efficientformer-l3 style configuration
    >>> model = EfficientFormerModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""
    model_type = ...
    def __init__(self, depths: List[int] = ..., hidden_sizes: List[int] = ..., downsamples: List[bool] = ..., dim: int = ..., key_dim: int = ..., attention_ratio: int = ..., resolution: int = ..., num_hidden_layers: int = ..., num_attention_heads: int = ..., mlp_expansion_ratio: int = ..., hidden_dropout_prob: float = ..., patch_size: int = ..., num_channels: int = ..., pool_size: int = ..., downsample_patch_size: int = ..., downsample_stride: int = ..., downsample_pad: int = ..., drop_path_rate: float = ..., num_meta3d_blocks: int = ..., distillation: bool = ..., use_layer_scale: bool = ..., layer_scale_init_value: float = ..., hidden_act: str = ..., initializer_range: float = ..., layer_norm_eps: float = ..., image_size: int = ..., batch_norm_eps: float = ..., **kwargs) -> None:
        ...
    


