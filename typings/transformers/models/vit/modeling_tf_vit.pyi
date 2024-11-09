"""
This type stub file was generated by pyright.
"""

import numpy as np
import tensorflow as tf
from typing import Optional, Tuple, Union
from ...modeling_tf_outputs import TFBaseModelOutput, TFBaseModelOutputWithPooling, TFSequenceClassifierOutput
from ...modeling_tf_utils import TFModelInputType, TFPreTrainedModel, TFSequenceClassificationLoss, keras, keras_serializable, unpack_inputs
from ...utils import add_code_sample_docstrings, add_start_docstrings, add_start_docstrings_to_model_forward
from .configuration_vit import ViTConfig

"""TF 2.0 ViT model."""
logger = ...
_CONFIG_FOR_DOC = ...
_CHECKPOINT_FOR_DOC = ...
_EXPECTED_OUTPUT_SHAPE = ...
_IMAGE_CLASS_CHECKPOINT = ...
_IMAGE_CLASS_EXPECTED_OUTPUT = ...
class TFViTEmbeddings(keras.layers.Layer):
    """
    Construct the CLS token, position and patch embeddings.

    """
    def __init__(self, config: ViTConfig, **kwargs) -> None:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    
    def interpolate_pos_encoding(self, embeddings, height, width) -> tf.Tensor:
        """
        This method allows to interpolate the pre-trained position encodings, to be able to use the model on higher
        resolution images.

        Source:
        https://github.com/facebookresearch/dino/blob/de9ee3df6cf39fac952ab558447af1fa1365362a/vision_transformer.py#L174
        """
        ...
    
    def call(self, pixel_values: tf.Tensor, interpolate_pos_encoding: bool = ..., training: bool = ...) -> tf.Tensor:
        ...
    


class TFViTPatchEmbeddings(keras.layers.Layer):
    """
    This class turns `pixel_values` of shape `(batch_size, num_channels, height, width)` into the initial
    `hidden_states` (patch embeddings) of shape `(batch_size, seq_length, hidden_size)` to be consumed by a
    Transformer.
    """
    def __init__(self, config: ViTConfig, **kwargs) -> None:
        ...
    
    def call(self, pixel_values: tf.Tensor, interpolate_pos_encoding: bool = ..., training: bool = ...) -> tf.Tensor:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFViTSelfAttention(keras.layers.Layer):
    def __init__(self, config: ViTConfig, **kwargs) -> None:
        ...
    
    def transpose_for_scores(self, tensor: tf.Tensor, batch_size: int) -> tf.Tensor:
        ...
    
    def call(self, hidden_states: tf.Tensor, head_mask: tf.Tensor, output_attentions: bool, training: bool = ...) -> Tuple[tf.Tensor]:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFViTSelfOutput(keras.layers.Layer):
    """
    The residual connection is defined in TFViTLayer instead of here (as is the case with other models), due to the
    layernorm applied before each block.
    """
    def __init__(self, config: ViTConfig, **kwargs) -> None:
        ...
    
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = ...) -> tf.Tensor:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFViTAttention(keras.layers.Layer):
    def __init__(self, config: ViTConfig, **kwargs) -> None:
        ...
    
    def prune_heads(self, heads):
        ...
    
    def call(self, input_tensor: tf.Tensor, head_mask: tf.Tensor, output_attentions: bool, training: bool = ...) -> Tuple[tf.Tensor]:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFViTIntermediate(keras.layers.Layer):
    def __init__(self, config: ViTConfig, **kwargs) -> None:
        ...
    
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFViTOutput(keras.layers.Layer):
    def __init__(self, config: ViTConfig, **kwargs) -> None:
        ...
    
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = ...) -> tf.Tensor:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFViTLayer(keras.layers.Layer):
    """This corresponds to the Block class in the timm implementation."""
    def __init__(self, config: ViTConfig, **kwargs) -> None:
        ...
    
    def call(self, hidden_states: tf.Tensor, head_mask: tf.Tensor, output_attentions: bool, training: bool = ...) -> Tuple[tf.Tensor]:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFViTEncoder(keras.layers.Layer):
    def __init__(self, config: ViTConfig, **kwargs) -> None:
        ...
    
    def call(self, hidden_states: tf.Tensor, head_mask: tf.Tensor, output_attentions: bool, output_hidden_states: bool, return_dict: bool, training: bool = ...) -> Union[TFBaseModelOutput, Tuple[tf.Tensor]]:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


@keras_serializable
class TFViTMainLayer(keras.layers.Layer):
    config_class = ViTConfig
    def __init__(self, config: ViTConfig, add_pooling_layer: bool = ..., **kwargs) -> None:
        ...
    
    def get_input_embeddings(self) -> keras.layers.Layer:
        ...
    
    @unpack_inputs
    def call(self, pixel_values: TFModelInputType | None = ..., head_mask: np.ndarray | tf.Tensor | None = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., interpolate_pos_encoding: Optional[bool] = ..., return_dict: Optional[bool] = ..., training: bool = ...) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFViTPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = ViTConfig
    base_model_prefix = ...
    main_input_name = ...


VIT_START_DOCSTRING = ...
VIT_INPUTS_DOCSTRING = ...
@add_start_docstrings("The bare ViT Model transformer outputting raw hidden-states without any specific head on top.", VIT_START_DOCSTRING)
class TFViTModel(TFViTPreTrainedModel):
    def __init__(self, config: ViTConfig, *inputs, add_pooling_layer=..., **kwargs) -> None:
        ...
    
    @unpack_inputs
    @add_start_docstrings_to_model_forward(VIT_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(checkpoint=_CHECKPOINT_FOR_DOC, output_type=TFBaseModelOutputWithPooling, config_class=_CONFIG_FOR_DOC, modality="vision", expected_output=_EXPECTED_OUTPUT_SHAPE)
    def call(self, pixel_values: TFModelInputType | None = ..., head_mask: np.ndarray | tf.Tensor | None = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., interpolate_pos_encoding: Optional[bool] = ..., return_dict: Optional[bool] = ..., training: bool = ...) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFViTPooler(keras.layers.Layer):
    def __init__(self, config: ViTConfig, **kwargs) -> None:
        ...
    
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


@add_start_docstrings("""
    ViT Model transformer with an image classification head on top (a linear layer on top of the final hidden state of
    the [CLS] token) e.g. for ImageNet.

    <Tip>

        Note that it's possible to fine-tune ViT on higher resolution images than the ones it has been trained on, by
        setting `interpolate_pos_encoding` to `True` in the forward of the model. This will interpolate the pre-trained
        position embeddings to the higher resolution.

    </Tip>
    """, VIT_START_DOCSTRING)
class TFViTForImageClassification(TFViTPreTrainedModel, TFSequenceClassificationLoss):
    def __init__(self, config: ViTConfig, *inputs, **kwargs) -> None:
        ...
    
    @unpack_inputs
    @add_start_docstrings_to_model_forward(VIT_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(checkpoint=_IMAGE_CLASS_CHECKPOINT, output_type=TFSequenceClassifierOutput, config_class=_CONFIG_FOR_DOC, expected_output=_IMAGE_CLASS_EXPECTED_OUTPUT)
    def call(self, pixel_values: TFModelInputType | None = ..., head_mask: np.ndarray | tf.Tensor | None = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., interpolate_pos_encoding: Optional[bool] = ..., return_dict: Optional[bool] = ..., labels: np.ndarray | tf.Tensor | None = ..., training: Optional[bool] = ...) -> Union[TFSequenceClassifierOutput, Tuple[tf.Tensor]]:
        r"""
        labels (`tf.Tensor` or `np.ndarray` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    

