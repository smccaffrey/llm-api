"""
This type stub file was generated by pyright.
"""

import numpy as np
import tensorflow as tf
from dataclasses import dataclass
from typing import Any, Optional, Tuple, Union
from ...modeling_tf_outputs import TFBaseModelOutput, TFBaseModelOutputWithPooling
from ...modeling_tf_utils import TFModelInputType, TFPreTrainedModel, keras, keras_serializable, unpack_inputs
from ...utils import ModelOutput, add_start_docstrings, add_start_docstrings_to_model_forward, replace_return_docstrings
from .configuration_clip import CLIPConfig, CLIPTextConfig, CLIPVisionConfig

"""TF 2.0 CLIP model."""
logger = ...
_CHECKPOINT_FOR_DOC = ...
LARGE_NEGATIVE = ...
def contrastive_loss(logits: tf.Tensor) -> tf.Tensor:
    ...

def clip_loss(similarity: tf.Tensor) -> tf.Tensor:
    ...

@dataclass
class TFCLIPOutput(ModelOutput):
    """
    Args:
        loss (`tf.Tensor` of shape `(1,)`, *optional*, returned when `return_loss` is `True`):
            Contrastive loss for image-text similarity.
        logits_per_image:(`tf.Tensor` of shape `(image_batch_size, text_batch_size)`):
            The scaled dot product scores between `image_embeds` and `text_embeds`. This represents the image-text
            similarity scores.
        logits_per_text:(`tf.Tensor` of shape `(text_batch_size, image_batch_size)`):
            The scaled dot product scores between `text_embeds` and `image_embeds`. This represents the text-image
            similarity scores.
        text_embeds(`tf.Tensor` of shape `(batch_size, output_dim`):
            The text embeddings obtained by applying the projection layer to the pooled output of [`TFCLIPTextModel`].
        image_embeds(`tf.Tensor` of shape `(batch_size, output_dim`):
            The image embeddings obtained by applying the projection layer to the pooled output of
            [`TFCLIPVisionModel`].
        text_model_output([`~modeling_tf_utils.TFBaseModelOutputWithPooling`]):
            The output of the [`TFCLIPTextModel`].
        vision_model_output([`~modeling_tf_utils.TFBaseModelOutputWithPooling`]):
            The output of the [`TFCLIPVisionModel`].
    """
    loss: tf.Tensor | None = ...
    logits_per_image: tf.Tensor = ...
    logits_per_text: tf.Tensor = ...
    text_embeds: tf.Tensor = ...
    image_embeds: tf.Tensor = ...
    text_model_output: TFBaseModelOutputWithPooling = ...
    vision_model_output: TFBaseModelOutputWithPooling = ...
    def to_tuple(self) -> Tuple[Any]:
        ...
    


class TFCLIPVisionEmbeddings(keras.layers.Layer):
    def __init__(self, config: CLIPVisionConfig, **kwargs) -> None:
        ...
    
    def build(self, input_shape: tf.TensorShape = ...): # -> None:
        ...
    
    def call(self, pixel_values: tf.Tensor) -> tf.Tensor:
        """`pixel_values` is expected to be of NCHW format."""
        ...
    


class TFCLIPTextEmbeddings(keras.layers.Layer):
    def __init__(self, config: CLIPTextConfig, **kwargs) -> None:
        ...
    
    def build(self, input_shape: tf.TensorShape = ...): # -> None:
        ...
    
    def call(self, input_ids: tf.Tensor = ..., position_ids: tf.Tensor = ..., inputs_embeds: tf.Tensor = ...) -> tf.Tensor:
        """
        Applies embedding based on inputs tensor.

        Returns:
            final_embeddings (`tf.Tensor`): output embedding tensor.
        """
        ...
    


class TFCLIPAttention(keras.layers.Layer):
    """Multi-headed attention from 'Attention Is All You Need' paper"""
    def __init__(self, config: CLIPConfig, **kwargs) -> None:
        ...
    
    def transpose_for_scores(self, tensor: tf.Tensor, batch_size: int) -> tf.Tensor:
        ...
    
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, causal_attention_mask: tf.Tensor, output_attentions: bool, training: bool = ...) -> Tuple[tf.Tensor]:
        """Input shape: Batch x Time x Channel"""
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFCLIPMLP(keras.layers.Layer):
    def __init__(self, config: CLIPConfig, **kwargs) -> None:
        ...
    
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFCLIPEncoderLayer(keras.layers.Layer):
    def __init__(self, config: CLIPConfig, **kwargs) -> None:
        ...
    
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, causal_attention_mask: tf.Tensor, output_attentions: bool, training: bool = ...) -> Tuple[tf.Tensor]:
        """
        Args:
            hidden_states (`tf.Tensor`): input to the layer of shape `(batch, seq_len, embed_dim)`
            attention_mask (`tf.Tensor`): attention mask of size
                `(batch, 1, tgt_len, src_len)` where padding elements are indicated by very large negative values.
            causal_attention_mask (`tf.Tensor`): causal attention mask of size
                `(batch, 1, tgt_len, src_len)` where padding elements are indicated by very large negative values.
            output_attentions (`bool`):
                Whether or not to return the attentions tensors of all attention layers. See `outputs` under returned
                tensors for more detail.
        """
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFCLIPEncoder(keras.layers.Layer):
    """
    Transformer encoder consisting of `config.num_hidden_layers` self attention layers. Each layer is a
    [`TFCLIPEncoderLayer`].

    Args:
        config: CLIPConfig
    """
    def __init__(self, config: CLIPConfig, **kwargs) -> None:
        ...
    
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, causal_attention_mask: tf.Tensor, output_attentions: bool, output_hidden_states: bool, return_dict: bool, training: bool = ...) -> Union[TFBaseModelOutput, Tuple[tf.Tensor]]:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFCLIPTextTransformer(keras.layers.Layer):
    def __init__(self, config: CLIPTextConfig, **kwargs) -> None:
        ...
    
    def call(self, input_ids: TFModelInputType, attention_mask: tf.Tensor, position_ids: tf.Tensor, output_attentions: bool, output_hidden_states: bool, return_dict: bool, training: bool = ...) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


@keras_serializable
class TFCLIPTextMainLayer(keras.layers.Layer):
    config_class = CLIPTextConfig
    def __init__(self, config: CLIPTextConfig, **kwargs) -> None:
        ...
    
    def get_input_embeddings(self) -> keras.layers.Layer:
        ...
    
    def set_input_embeddings(self, value: tf.Variable): # -> None:
        ...
    
    @unpack_inputs
    def call(self, input_ids: TFModelInputType | None = ..., attention_mask: np.ndarray | tf.Tensor | None = ..., position_ids: np.ndarray | tf.Tensor | None = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., training: bool = ...) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFCLIPVisionTransformer(keras.layers.Layer):
    def __init__(self, config: CLIPVisionConfig, **kwargs) -> None:
        ...
    
    def call(self, pixel_values: TFModelInputType, output_attentions: bool, output_hidden_states: bool, return_dict: bool, training: bool = ...) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


@keras_serializable
class TFCLIPVisionMainLayer(keras.layers.Layer):
    config_class = CLIPVisionConfig
    def __init__(self, config: CLIPVisionConfig, **kwargs) -> None:
        ...
    
    def get_input_embeddings(self) -> keras.layers.Layer:
        ...
    
    @unpack_inputs
    def call(self, pixel_values: TFModelInputType | None = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., training: bool = ...) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


@keras_serializable
class TFCLIPMainLayer(keras.layers.Layer):
    config_class = CLIPConfig
    def __init__(self, config: CLIPConfig, **kwargs) -> None:
        ...
    
    def build(self, input_shape: tf.TensorShape = ...): # -> None:
        ...
    
    @unpack_inputs
    def get_text_features(self, input_ids: TFModelInputType | None = ..., attention_mask: np.ndarray | tf.Tensor | None = ..., position_ids: np.ndarray | tf.Tensor | None = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., training: bool = ...) -> tf.Tensor:
        ...
    
    @unpack_inputs
    def get_image_features(self, pixel_values: TFModelInputType | None = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., training: bool = ...) -> tf.Tensor:
        ...
    
    @unpack_inputs
    def call(self, input_ids: TFModelInputType | None = ..., pixel_values: TFModelInputType | None = ..., attention_mask: np.ndarray | tf.Tensor | None = ..., position_ids: np.ndarray | tf.Tensor | None = ..., return_loss: Optional[bool] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., training: bool = ...) -> Union[TFCLIPOutput, Tuple[tf.Tensor]]:
        ...
    


class TFCLIPPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = CLIPConfig
    base_model_prefix = ...
    _keys_to_ignore_on_load_missing = ...
    _keys_to_ignore_on_load_unexpected = ...


CLIP_START_DOCSTRING = ...
CLIP_TEXT_INPUTS_DOCSTRING = ...
CLIP_VISION_INPUTS_DOCSTRING = ...
CLIP_INPUTS_DOCSTRING = ...
class TFCLIPTextModel(TFCLIPPreTrainedModel):
    config_class = CLIPTextConfig
    def __init__(self, config: CLIPTextConfig, *inputs, **kwargs) -> None:
        ...
    
    @unpack_inputs
    @add_start_docstrings_to_model_forward(CLIP_TEXT_INPUTS_DOCSTRING.format("batch_size, sequence_length"))
    @replace_return_docstrings(output_type=TFBaseModelOutputWithPooling, config_class=CLIPTextConfig)
    def call(self, input_ids: TFModelInputType | None = ..., attention_mask: np.ndarray | tf.Tensor | None = ..., position_ids: np.ndarray | tf.Tensor | None = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., training: Optional[bool] = ...) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]:
        r"""
        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, TFCLIPTextModel

        >>> model = TFCLIPTextModel.from_pretrained("openai/clip-vit-base-patch32")
        >>> tokenizer = AutoTokenizer.from_pretrained("openai/clip-vit-base-patch32")

        >>> inputs = tokenizer(["a photo of a cat", "a photo of a dog"], padding=True, return_tensors="tf")

        >>> outputs = model(**inputs)
        >>> last_hidden_state = outputs.last_hidden_state
        >>> pooled_output = outputs.pooler_output  # pooled (EOS token) states
        ```"""
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFCLIPVisionModel(TFCLIPPreTrainedModel):
    config_class = CLIPVisionConfig
    main_input_name = ...
    def __init__(self, config: CLIPVisionConfig, *inputs, **kwargs) -> None:
        ...
    
    @unpack_inputs
    @add_start_docstrings_to_model_forward(CLIP_VISION_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=TFBaseModelOutputWithPooling, config_class=CLIPVisionConfig)
    def call(self, pixel_values: TFModelInputType | None = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., training: Optional[bool] = ...) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]:
        r"""
        Returns:

        Examples:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, TFCLIPVisionModel

        >>> model = TFCLIPVisionModel.from_pretrained("openai/clip-vit-base-patch32")
        >>> processor = AutoProcessor.from_pretrained("openai/clip-vit-base-patch32")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(images=image, return_tensors="tf")

        >>> outputs = model(**inputs)
        >>> last_hidden_state = outputs.last_hidden_state
        >>> pooled_output = outputs.pooler_output  # pooled CLS states
        ```"""
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


@add_start_docstrings(CLIP_START_DOCSTRING)
class TFCLIPModel(TFCLIPPreTrainedModel):
    config_class = CLIPConfig
    def __init__(self, config: CLIPConfig, *inputs, **kwargs) -> None:
        ...
    
    @unpack_inputs
    @add_start_docstrings_to_model_forward(CLIP_TEXT_INPUTS_DOCSTRING.format("batch_size, sequence_length"))
    def get_text_features(self, input_ids: TFModelInputType | None = ..., attention_mask: np.ndarray | tf.Tensor | None = ..., position_ids: np.ndarray | tf.Tensor | None = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., training: bool = ...) -> tf.Tensor:
        r"""
        Returns:
            text_features (`tf.Tensor` of shape `(batch_size, output_dim`): The text embeddings obtained by applying
            the projection layer to the pooled output of [`TFCLIPTextModel`].

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, TFCLIPModel

        >>> model = TFCLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        >>> tokenizer = AutoTokenizer.from_pretrained("openai/clip-vit-base-patch32")

        >>> inputs = tokenizer(["a photo of a cat", "a photo of a dog"], padding=True, return_tensors="tf")
        >>> text_features = model.get_text_features(**inputs)
        ```"""
        ...
    
    @unpack_inputs
    @add_start_docstrings_to_model_forward(CLIP_VISION_INPUTS_DOCSTRING)
    def get_image_features(self, pixel_values: TFModelInputType | None = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., training: bool = ...) -> tf.Tensor:
        r"""
        Returns:
            image_features (`tf.Tensor` of shape `(batch_size, output_dim`): The image embeddings obtained by applying
            the projection layer to the pooled output of [`TFCLIPVisionModel`].

        Examples:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, TFCLIPModel

        >>> model = TFCLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        >>> processor = AutoProcessor.from_pretrained("openai/clip-vit-base-patch32")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(images=image, return_tensors="tf")

        >>> image_features = model.get_image_features(**inputs)
        ```"""
        ...
    
    @unpack_inputs
    @add_start_docstrings_to_model_forward(CLIP_INPUTS_DOCSTRING.format("batch_size, sequence_length"))
    @replace_return_docstrings(output_type=TFCLIPOutput, config_class=CLIPConfig)
    def call(self, input_ids: TFModelInputType | None = ..., pixel_values: TFModelInputType | None = ..., attention_mask: np.ndarray | tf.Tensor | None = ..., position_ids: np.ndarray | tf.Tensor | None = ..., return_loss: Optional[bool] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., training: bool = ...) -> Union[TFCLIPOutput, Tuple[tf.Tensor]]:
        r"""
        Returns:

        Examples:

        ```python
        >>> import tensorflow as tf
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, TFCLIPModel

        >>> model = TFCLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        >>> processor = AutoProcessor.from_pretrained("openai/clip-vit-base-patch32")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(
        ...     text=["a photo of a cat", "a photo of a dog"], images=image, return_tensors="tf", padding=True
        ... )

        >>> outputs = model(**inputs)
        >>> logits_per_image = outputs.logits_per_image  # this is the image-text similarity score
        >>> probs = tf.nn.softmax(logits_per_image, axis=1)  # we can take the softmax to get the label probabilities
        ```"""
        ...
    
    def serving_output(self, output: TFCLIPOutput) -> TFCLIPOutput:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


