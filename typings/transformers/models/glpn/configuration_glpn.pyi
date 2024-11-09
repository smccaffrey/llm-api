"""
This type stub file was generated by pyright.
"""

from ...configuration_utils import PretrainedConfig

"""GLPN model configuration"""
logger = ...
class GLPNConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`GLPNModel`]. It is used to instantiate an GLPN
    model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
    defaults will yield a similar configuration to that of the GLPN
    [vinvino02/glpn-kitti](https://huggingface.co/vinvino02/glpn-kitti) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        num_channels (`int`, *optional*, defaults to 3):
            The number of input channels.
        num_encoder_blocks (`int`, *optional*, defaults to 4):
            The number of encoder blocks (i.e. stages in the Mix Transformer encoder).
        depths (`List[int]`, *optional*, defaults to `[2, 2, 2, 2]`):
            The number of layers in each encoder block.
        sr_ratios (`List[int]`, *optional*, defaults to `[8, 4, 2, 1]`):
            Sequence reduction ratios in each encoder block.
        hidden_sizes (`List[int]`, *optional*, defaults to `[32, 64, 160, 256]`):
            Dimension of each of the encoder blocks.
        patch_sizes (`List[int]`, *optional*, defaults to `[7, 3, 3, 3]`):
            Patch size before each encoder block.
        strides (`List[int]`, *optional*, defaults to `[4, 2, 2, 2]`):
            Stride before each encoder block.
        num_attention_heads (`List[int]`, *optional*, defaults to `[1, 2, 5, 8]`):
            Number of attention heads for each attention layer in each block of the Transformer encoder.
        mlp_ratios (`List[int]`, *optional*, defaults to `[4, 4, 4, 4]`):
            Ratio of the size of the hidden layer compared to the size of the input layer of the Mix FFNs in the
            encoder blocks.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.0):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        drop_path_rate (`float`, *optional*, defaults to 0.1):
            The dropout probability for stochastic depth, used in the blocks of the Transformer encoder.
        layer_norm_eps (`float`, *optional*, defaults to 1e-06):
            The epsilon used by the layer normalization layers.
        decoder_hidden_size (`int`, *optional*, defaults to 64):
            The dimension of the decoder.
        max_depth (`int`, *optional*, defaults to 10):
            The maximum depth of the decoder.
        head_in_index (`int`, *optional*, defaults to -1):
            The index of the features to use in the head.

    Example:

    ```python
    >>> from transformers import GLPNModel, GLPNConfig

    >>> # Initializing a GLPN vinvino02/glpn-kitti style configuration
    >>> configuration = GLPNConfig()

    >>> # Initializing a model from the vinvino02/glpn-kitti style configuration
    >>> model = GLPNModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""
    model_type = ...
    def __init__(self, num_channels=..., num_encoder_blocks=..., depths=..., sr_ratios=..., hidden_sizes=..., patch_sizes=..., strides=..., num_attention_heads=..., mlp_ratios=..., hidden_act=..., hidden_dropout_prob=..., attention_probs_dropout_prob=..., initializer_range=..., drop_path_rate=..., layer_norm_eps=..., decoder_hidden_size=..., max_depth=..., head_in_index=..., **kwargs) -> None:
        ...
    

