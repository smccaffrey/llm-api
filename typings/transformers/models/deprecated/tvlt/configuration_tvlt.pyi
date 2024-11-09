"""
This type stub file was generated by pyright.
"""

from ....configuration_utils import PretrainedConfig

"""TVLT model configuration"""
logger = ...
class TvltConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`TvltModel`]. It is used to instantiate a TVLT
    model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
    defaults will yield a similar configuration to that of the TVLT
    [ZinengTang/tvlt-base](https://huggingface.co/ZinengTang/tvlt-base) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        image_size (`int`, *optional*, defaults to 224):
            The size (resolution) of each image.
        spectrogram_length (`int`, *optional*, defaults to 2048):
            The time length of each audio spectrogram.
        frequency_length (`int`, *optional*, defaults to 128):
            The frequency length of audio spectrogram.
        image_patch_size (`List[int]`, *optional*, defaults to `[16, 16]`):
            The size (resolution) of each image patch.
        audio_patch_size (`List[int]`, *optional*, defaults to `[16, 16]`):
            The size (resolution) of each audio patch.
        num_image_channels (`int`, *optional*, defaults to 3):
            The number of input image channels.
        num_audio_channels (`int`, *optional*, defaults to 1):
            The number of input audio channels.
        num_frames (`int`, *optional*, defaults to 8):
            The maximum number of frames for an input video.
        hidden_size (`int`, *optional*, defaults to 768):
            Dimensionality of the encoder layers and the pooler layer.
        num_hidden_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        intermediate_size (`int`, *optional*, defaults to 3072):
            Dimensionality of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.0):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-06):
            The epsilon used by the layer normalization layers.
        qkv_bias (`bool`, *optional*, defaults to `True`):
            Whether to add a bias to the queries, keys and values.
        use_mean_pooling (`bool`, *optional*, defaults to `False`):
            Whether to mean pool the final hidden states instead of using the final hidden state of the [CLS] token.
        decoder_num_attention_heads (`int`, *optional*, defaults to 16):
            Number of attention heads for each attention layer in the decoder.
        decoder_hidden_size (`int`, *optional*, defaults to 512):
            Dimensionality of the decoder.
        decoder_num_hidden_layers (`int`, *optional*, defaults to 8):
            Number of hidden layers in the decoder.
        decoder_intermediate_size (`int`, *optional*, defaults to 2048):
            Dimensionality of the "intermediate" (i.e., feed-forward) layer in the decoder.
        pixel_mask_ratio (`float`, *optional*, defaults to 0.75):
            Image patch masking ratio.
        audio_mask_ratio (`float`, *optional*, defaults to 0.15):
            Audio patch masking ratio.
        audio_mask_type (`str`, *optional*, defaults to `"frame-level"`):
            Audio patch masking type, choose between "frame-level" and "patch-level".
        task_matching (`bool`, *optional*, defaults to `True`):
            Whether to use vision audio matching task in pretraining.
        task_mae (`bool`, *optional*, defaults to `True`):
            Whether to use the masked auto-encoder (MAE) in pretraining.
        loss_type (`str`, *optional*, defaults to `"classification"`):
            Loss types including regression and classification.

    Example:

    ```python
    >>> from transformers import TvltConfig, TvltModel

    >>> # # Initializing a TVLT ZinengTang/tvlt-base style configuration
    >>> configuration = TvltConfig()

    >>> # # Initializing a model (with random weights) from the ZinengTang/tvlt-base style configuration
    >>> model = TvltModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""
    model_type = ...
    def __init__(self, image_size=..., spectrogram_length=..., frequency_length=..., image_patch_size=..., audio_patch_size=..., num_image_channels=..., num_audio_channels=..., num_frames=..., hidden_size=..., num_hidden_layers=..., num_attention_heads=..., intermediate_size=..., hidden_act=..., hidden_dropout_prob=..., attention_probs_dropout_prob=..., initializer_range=..., layer_norm_eps=..., qkv_bias=..., use_mean_pooling=..., decoder_num_attention_heads=..., decoder_hidden_size=..., decoder_num_hidden_layers=..., decoder_intermediate_size=..., pixel_mask_ratio=..., audio_mask_ratio=..., audio_mask_type=..., task_matching=..., task_mae=..., loss_type=..., **kwargs) -> None:
        ...
    


