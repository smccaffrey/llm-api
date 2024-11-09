"""
This type stub file was generated by pyright.
"""

from ...configuration_utils import PretrainedConfig

"""FALCONMAMBA configuration"""
logger = ...
class FalconMambaConfig(PretrainedConfig):
    """
    This is the configuration class to store the configuration of a [`FalconMambaModel`]. It is used to instantiate a FALCON_MAMBA
    model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
    defaults will yield a similar configuration to that of the FALCON_MAMBA
    [tiiuae/falcon-mamba-7b](https://huggingface.co/tiiuae/falcon-mamba-7b) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 50280):
            Vocabulary size of the FALCON_MAMBA model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`FalconMambaModel`].
        hidden_size (`int`, *optional*, defaults to 768):
            Dimensionality of the embeddings and hidden states.
        state_size (`int`, *optional*, defaults to 16): shape of the state space latents.
        num_hidden_layers (`int`, *optional*, defaults to 32):
            Number of hidden layers in the model.
        layer_norm_epsilon (`float`, *optional*, defaults to 1e-05):
            The epsilon to use in the layer normalization layers.
        pad_token_id (`int`, *optional*, defaults to 0):
            Padding token id.
        bos_token_id (`int`, *optional*, defaults to 0):
            The id of the beginning of sentence token in the vocabulary.
        eos_token_id (`int`, *optional*, defaults to 0):
            The id of the end of sentence token in the vocabulary.
        expand (`int`, *optional*, defaults to 2): Expanding factor used to determine the intermediate size.
        conv_kernel (`int`, *optional*, defaults to 4): Size of the convolution kernel.
        use_bias (`bool`, *optional*, defaults to `False`):
            Whether or not to use bias in ["in_proj", "out_proj"] of the mixer block
        use_conv_bias (`bool`, *optional*, defaults to `True`):
            Whether or not to use bias in the convolution layer of the mixer block.
        hidden_act (`str`, *optional*, defaults to `"silu"`):
            The non-linear activation function (function or string) in the decoder.
        initializer_range (`float`, *optional*, defaults to 0.1):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        residual_in_fp32 (`bool`, *optional*, defaults to `True`):
            Whether or not residuals should be in `float32`. If set to `False` residuals will keep the same `dtype` as the rest of the model
        time_step_rank (`Union[int,str]`, *optional*, defaults to `"auto"`):
            Rank of the discretization projection matrix. `"auto"` means that it will default to `math.ceil(self.hidden_size / 16)`
        time_step_scale (`float`, *optional*, defaults to 1.0):
            Scale used used to scale `dt_proj.bias`.
        time_step_min (`float`, *optional*, defaults to 0.001):
            Minimum `time_step` used to bound `dt_proj.bias`.
        time_step_max (`float`, *optional*, defaults to 0.1):
            Maximum `time_step` used to bound `dt_proj.bias`.
        time_step_init_scheme (`float`, *optional*, defaults to `"random"`):
            Init scheme used for `dt_proj.weight`. Should be one of `["random","uniform"]`
        time_step_floor (`float`, *optional*, defaults to 0.0001):
            Minimum clamping value of the `dt_proj.bias` layer initialization.
        rescale_prenorm_residual (`bool`, *optional*, defaults to `False`):
            Whether or not to rescale `out_proj` weights when initializing.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the cache should be used.
        use_mambapy (`bool`, *optional*, defaults to `False`):
            Determines the fallback strategy during training if the CUDA-based official implementation of FalconMamba is not avaiable. If `True`, the falcon_mamba.py implementation is used. If `False`, the naive and slower implementation is used. Consider switching to the naive version if memory is limited.
        mixer_rms_eps (`float`, *optional*, defaults to 1e-06):
            The RMS norm epsilon value that is used in the Mixer RMS norm for B, C and dt states.
    Example:

    ```python
    >>> from transformers import FalconMambaConfig, FalconMambaModel

    >>> # Initializing a FalconMamba configuration
    >>> configuration = FalconMambaConfig()

    >>> # Initializing a model (with random weights) from the configuration
    >>> model = FalconMambaModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""
    model_type = ...
    def __init__(self, vocab_size=..., hidden_size=..., state_size=..., num_hidden_layers=..., layer_norm_epsilon=..., pad_token_id=..., bos_token_id=..., eos_token_id=..., expand=..., conv_kernel=..., use_bias=..., use_conv_bias=..., hidden_act=..., initializer_range=..., residual_in_fp32=..., time_step_rank=..., time_step_scale=..., time_step_min=..., time_step_max=..., time_step_init_scheme=..., time_step_floor=..., rescale_prenorm_residual=..., use_cache=..., use_mambapy=..., mixer_rms_eps=..., **kwargs) -> None:
        ...
    

