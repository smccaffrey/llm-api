"""
This type stub file was generated by pyright.
"""

from ...configuration_utils import PretrainedConfig

logger = ...
class LlavaOnevisionConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`LlavaOnevisionForConditionalGeneration`]. It is used to instantiate an
    Llava-NeXT model according to the specified arguments, defining the model architecture. Instantiating a configuration
    with the defaults will yield a similar configuration to that of the [llava-hf/llava-onevision-qwen2-7b-ov-hf](https://huggingface.co/llava-hf/llava-onevision-qwen2-7b-ov-hf)
    model.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        vision_config (`Union[AutoConfig, dict]`,  *optional*, defaults to `SiglipVisionConfig`):
            The config object or dictionary of the vision backbone.
        text_config (`Union[AutoConfig, dict]`, *optional*, defaults to `Qwen2Config`):
            The config object or dictionary of the text backbone.
        image_token_index (`int`, *optional*, defaults to 151646):
            The image token index to encode the image prompt.
        video_token_index (`int`, *optional*, defaults to 151647):
            The video token index to encode the video prompt.
        projector_hidden_act (`str`, *optional*, defaults to `"gelu"`):
            The activation function used by the multimodal projector.
        vision_feature_select_strategy (`str`, *optional*, defaults to `"full"`):
            The feature selection strategy used to select the vision feature from the vision backbone.
            Can be one of `"default"` or `"full"`. If `"default"`, the CLS token is removed from the vision features.
            If `"full"`, the full vision features are used.
        vision_feature_layer (`int`, *optional*, defaults to -1):
            The index of the layer to select the vision feature.
        vision_aspect_ratio (`str`, *optional*, defaults to `"anyres_max_9"`):
            Aspect ratio used when processong image features. The default value is "anyres_max_9".
        image_grid_pinpoints (`List`, *optional*):
            A list of possible resolutions to use for processing high resolution images. Each item in the list should be a tuple or list
            of the form `(height, width)`.
        tie_word_embeddings (`bool`, *optional*, defaults to `False`):
            Whether the model's input and output word embeddings should be tied.

    Example:

    ```python
    >>> from transformers import LlavaOnevisionForConditionalGeneration, LlavaOnevisionConfig, SiglipVisionConfig, Qwen2Config

    >>> # Initializing a CLIP-vision config
    >>> vision_config = SiglipVisionConfig()

    >>> # Initializing a Llama config
    >>> text_config = Qwen2Config()

    >>> # Initializing a Llava-Next llava-hf/llava-onevision-qwen2-7b-ov-hf style configuration
    >>> configuration = LlavaOnevisionConfig(vision_config, text_config)

    >>> # Initializing a model from the llava-hf/llava-onevision-qwen2-7b-ov-hf style configuration
    >>> model = LlavaOnevisionForConditionalGeneration(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""
    model_type = ...
    is_composition = ...
    def __init__(self, vision_config=..., text_config=..., image_token_index=..., video_token_index=..., projector_hidden_act=..., vision_feature_select_strategy=..., vision_feature_layer=..., vision_aspect_ratio=..., image_grid_pinpoints=..., tie_word_embeddings=..., **kwargs) -> None:
        ...
    

