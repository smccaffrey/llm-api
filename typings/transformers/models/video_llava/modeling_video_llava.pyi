"""
This type stub file was generated by pyright.
"""

import torch
from dataclasses import dataclass
from typing import List, Optional, Tuple, Union
from torch import nn
from ...generation import GenerationMixin
from ...modeling_outputs import ModelOutput
from ...modeling_utils import PreTrainedModel
from ...utils import add_start_docstrings, add_start_docstrings_to_model_forward, replace_return_docstrings
from .configuration_video_llava import VideoLlavaConfig

"""PyTorch VideoLlava model."""
logger = ...
_CONFIG_FOR_DOC = ...
@dataclass
class VideoLlavaCausalLMOutputWithPast(ModelOutput):
    """
    Base class for VideoLlava causal language model (or autoregressive) outputs.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Language modeling loss (for next-token prediction).
        logits (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
        past_key_values (`tuple(tuple(torch.FloatTensor))`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
            Tuple of `tuple(torch.FloatTensor)` of length `config.n_layers`, with each tuple having 2 tensors of shape
            `(batch_size, num_heads, sequence_length, embed_size_per_head)`)

            Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
            `past_key_values` input) to speed up sequential decoding.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
        image_hidden_states (`torch.FloatTensor`, *optional*):
            A `torch.FloatTensor` of size (batch_size, num_images, sequence_length, hidden_size)`.
            image_hidden_states of the model produced by the vision encoder and after projecting the last hidden state.
        video_hidden_states (`torch.FloatTensor`, *optional*):
            A `torch.FloatTensor`  of size `(batch_size * num_frames, num_videos, sequence_length, hidden_size)`.
            video_hidden_states of the model produced by the vision encoder and after projecting the last hidden state.
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    past_key_values: Optional[List[torch.FloatTensor]] = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    image_hidden_states: Optional[torch.FloatTensor] = ...
    video_hidden_states: Optional[torch.FloatTensor] = ...


class VideoLlavaMultiModalProjector(nn.Module):
    def __init__(self, config: VideoLlavaConfig) -> None:
        ...
    
    def forward(self, image_features): # -> Any:
        ...
    


VIDEO_LLAVA_START_DOCSTRING = ...
@add_start_docstrings(VIDEO_LLAVA_START_DOCSTRING)
class VideoLlavaPreTrainedModel(PreTrainedModel):
    config_class = VideoLlavaConfig
    base_model_prefix = ...
    supports_gradient_checkpointing = ...
    _no_split_modules = ...
    _skip_keys_device_placement = ...
    _supports_cache_class = ...
    _supports_flash_attn_2 = ...
    _supports_sdpa = ...


VIDEO_LLAVA_INPUTS_DOCSTRING = ...
@add_start_docstrings("""The VideoLlava model which consists of a vision backbone and a language model.""", VIDEO_LLAVA_START_DOCSTRING)
class VideoLlavaForConditionalGeneration(VideoLlavaPreTrainedModel, GenerationMixin):
    def __init__(self, config: VideoLlavaConfig) -> None:
        ...
    
    def get_input_embeddings(self):
        ...
    
    def set_input_embeddings(self, value): # -> None:
        ...
    
    def get_output_embeddings(self):
        ...
    
    def set_output_embeddings(self, new_embeddings): # -> None:
        ...
    
    def set_decoder(self, decoder): # -> None:
        ...
    
    def get_decoder(self):
        ...
    
    def tie_weights(self):
        ...
    
    def resize_token_embeddings(self, new_num_tokens: Optional[int] = ..., pad_to_multiple_of=...) -> nn.Embedding:
        ...
    
    def get_image_features(self, pixel_values_images: torch.FloatTensor, vision_feature_layer: int, vision_feature_select_strategy: str): # -> Any:
        """
        Obtains image last hidden states from the vision tower and apply multimodal projection.

        Args:
            pixel_values_images (`torch.FloatTensor]` of shape `(batch_size, channels, height, width)`)
               The tensors corresponding to the input images.
            vision_feature_layer (`int`):
                The index of the layer to select the vision feature.
            vision_feature_select_strategy (`str`):
                The feature selection strategy used to select the vision feature from the vision backbone.
                Can be one of `"default"` or `"full"`
        Returns:
            image_features (`torch.Tensor`): Image feature tensor of shape `(num_images, image_length, embed_dim)`).
        """
        ...
    
    def get_video_features(self, pixel_values_videos: torch.FloatTensor, vision_feature_layer: int): # -> tuple[Any, _int]:
        """
        Obtains video last hidden states from the vision tower and apply multimodal projection.

        Args:
            pixel_values_videos (`torch.FloatTensor]` of shape `(batch_size, num_frames, channels, height, width)`)
               The tensors corresponding to the input videos.
            vision_feature_layer (`int`):
                The index of the layer to select the vision feature.
        Returns:
            video_features (`torch.Tensor`): Video feature tensor of shape `(num_videos * num_frames, image_length, embed_dim)`).
            frames (`int`): Number of frames the videos have.
        """
        ...
    
    @add_start_docstrings_to_model_forward(VIDEO_LLAVA_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=VideoLlavaCausalLMOutputWithPast, config_class=_CONFIG_FOR_DOC)
    def forward(self, input_ids: torch.LongTensor = ..., pixel_values_images: torch.FloatTensor = ..., pixel_values_videos: torch.FloatTensor = ..., attention_mask: Optional[torch.Tensor] = ..., position_ids: Optional[torch.LongTensor] = ..., past_key_values: Optional[List[torch.FloatTensor]] = ..., inputs_embeds: Optional[torch.FloatTensor] = ..., vision_feature_layer: Optional[int] = ..., vision_feature_select_strategy: Optional[str] = ..., labels: Optional[torch.LongTensor] = ..., use_cache: Optional[bool] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., cache_position: Optional[torch.LongTensor] = ..., num_logits_to_keep: int = ...) -> Union[Tuple, VideoLlavaCausalLMOutputWithPast]:
        r"""
        Args:
            labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
                Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
                config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
                (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.

            num_logits_to_keep (`int`, *optional*):
                Calculate logits for the last `num_logits_to_keep` tokens. If `0`, calculate logits for all
                `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
                token can save memory, which becomes pretty significant for long sequences or large vocabulary size.

        Returns:

        Example:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> import numpy as np
        >>> import av
        >>> from huggingface_hub import hf_hub_download
        >>> from transformers import VideoLlavaProcessor, VideoLlavaForConditionalGeneration


        >>> def read_video_pyav(container, indices):
        ...     '''
        ...     Decode the video with PyAV decoder.
        ...     Args:
        ...         container (`av.container.input.InputContainer`): PyAV container.
        ...         indices (`List[int]`): List of frame indices to decode.
        ...     Returns:
        ...         result (np.ndarray): np array of decoded frames of shape (num_frames, height, width, 3).
        ...     '''
        ...     frames = []
        ...     container.seek(0)
        ...     start_index = indices[0]
        ...     end_index = indices[-1]
        ...     for i, frame in enumerate(container.decode(video=0)):
        ...         if i > end_index:
        ...             break
        ...         if i >= start_index and i in indices:
        ...             frames.append(frame)
        ...     return np.stack([x.to_ndarray(format="rgb24") for x in frames])

        >>> model = VideoLlavaForConditionalGeneration.from_pretrained("LanguageBind/Video-LLaVA-7B-hf")
        >>> processor = VideoLlavaProcessor.from_pretrained("LanguageBind/Video-LLaVA-7B-hf")

        >>> prompt = "USER: <video>\nWhy is this video funny? ASSISTANT:"
        >>> video_path = hf_hub_download(repo_id="raushan-testing-hf/videos-test", filename="sample_demo_1.mp4", repo_type="dataset")
        >>> container = av.open(video_path)

        >>> # sample uniformly 8 frames from the video
        >>> total_frames = container.streams.video[0].frames
        >>> indices = np.arange(0, total_frames, total_frames / 8).astype(int)
        >>> clip = read_video_pyav(container, indices)

        >>> inputs = processor(text=prompt, videos=clip, return_tensors="pt")

        >>> # Generate
        >>> generate_ids = model.generate(**inputs, max_length=80)
        >>> processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        "USER:  Why is this video funny? ASSISTANT: The video is funny because the baby is playing with a Wii remote while sitting on the floor, and the baby is wearing glasses.Ъ. The baby's actions are amusing because it is a young child trying to interact with a video game, which is not a typical activity for a"

        >>> # to generate from image and video mix
        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)
        >>> prompt = [
        ...     "USER: <image>\nHow many cats do you see? ASSISTANT:",
        ...     "USER: <video>\nWhy is this video funny? ASSISTANT:"
        ... ]
        >>> inputs = processor(text=prompt, images=image, videos=clip, padding=True, return_tensors="pt")

        >>> # Generate
        >>> generate_ids = model.generate(**inputs, max_length=50)
        >>> processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=True)
        ['USER:   How many cats do you see? ASSISTANT: There are two cats visible in the image. (or three, if you count the one in the background).', 'USER:  Why is this video funny? ASSISTANT: The video is funny because it shows a baby sitting on a bed and playing with a Wii remote.Ъ. The baby is holding the remote']
        ```
        """
        ...
    
    def prepare_inputs_for_generation(self, input_ids, past_key_values=..., inputs_embeds=..., pixel_values_images=..., pixel_values_videos=..., attention_mask=..., cache_position=..., num_logits_to_keep=..., **kwargs):
        ...
    


