"""
This type stub file was generated by pyright.
"""

import tensorflow as tf
from typing import Optional, Tuple, Union
from ...modeling_tf_outputs import TFBaseModelOutputWithNoAttention, TFBaseModelOutputWithPoolingAndNoAttention, TFImageClassifierOutputWithNoAttention
from ...modeling_tf_utils import TFPreTrainedModel, TFSequenceClassificationLoss, keras, keras_serializable, unpack_inputs
from ...utils import add_code_sample_docstrings, add_start_docstrings, add_start_docstrings_to_model_forward
from .configuration_resnet import ResNetConfig

"""TensorFlow ResNet model."""
logger = ...
_CONFIG_FOR_DOC = ...
_CHECKPOINT_FOR_DOC = ...
_EXPECTED_OUTPUT_SHAPE = ...
_IMAGE_CLASS_CHECKPOINT = ...
_IMAGE_CLASS_EXPECTED_OUTPUT = ...
class TFResNetConvLayer(keras.layers.Layer):
    def __init__(self, in_channels: int, out_channels: int, kernel_size: int = ..., stride: int = ..., activation: str = ..., **kwargs) -> None:
        ...
    
    def convolution(self, hidden_state: tf.Tensor) -> tf.Tensor:
        ...
    
    def call(self, hidden_state: tf.Tensor, training: bool = ...) -> tf.Tensor:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFResNetEmbeddings(keras.layers.Layer):
    """
    ResNet Embeddings (stem) composed of a single aggressive convolution.
    """
    def __init__(self, config: ResNetConfig, **kwargs) -> None:
        ...
    
    def call(self, pixel_values: tf.Tensor, training: bool = ...) -> tf.Tensor:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFResNetShortCut(keras.layers.Layer):
    """
    ResNet shortcut, used to project the residual features to the correct size. If needed, it is also used to
    downsample the input using `stride=2`.
    """
    def __init__(self, in_channels: int, out_channels: int, stride: int = ..., **kwargs) -> None:
        ...
    
    def call(self, x: tf.Tensor, training: bool = ...) -> tf.Tensor:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFResNetBasicLayer(keras.layers.Layer):
    """
    A classic ResNet's residual layer composed by two `3x3` convolutions.
    """
    def __init__(self, in_channels: int, out_channels: int, stride: int = ..., activation: str = ..., **kwargs) -> None:
        ...
    
    def call(self, hidden_state: tf.Tensor, training: bool = ...) -> tf.Tensor:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFResNetBottleNeckLayer(keras.layers.Layer):
    """
    A classic ResNet's bottleneck layer composed by three `3x3` convolutions.

    The first `1x1` convolution reduces the input by a factor of `reduction` in order to make the second `3x3`
    convolution faster. The last `1x1` convolution remaps the reduced features to `out_channels`.
    """
    def __init__(self, in_channels: int, out_channels: int, stride: int = ..., activation: str = ..., reduction: int = ..., **kwargs) -> None:
        ...
    
    def call(self, hidden_state: tf.Tensor, training: bool = ...) -> tf.Tensor:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFResNetStage(keras.layers.Layer):
    """
    A ResNet stage composed of stacked layers.
    """
    def __init__(self, config: ResNetConfig, in_channels: int, out_channels: int, stride: int = ..., depth: int = ..., **kwargs) -> None:
        ...
    
    def call(self, hidden_state: tf.Tensor, training: bool = ...) -> tf.Tensor:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFResNetEncoder(keras.layers.Layer):
    def __init__(self, config: ResNetConfig, **kwargs) -> None:
        ...
    
    def call(self, hidden_state: tf.Tensor, output_hidden_states: bool = ..., return_dict: bool = ..., training: bool = ...) -> TFBaseModelOutputWithNoAttention:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFResNetPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = ResNetConfig
    base_model_prefix = ...
    main_input_name = ...
    @property
    def input_signature(self): # -> dict[str, Any]:
        ...
    


RESNET_START_DOCSTRING = ...
RESNET_INPUTS_DOCSTRING = ...
@keras_serializable
class TFResNetMainLayer(keras.layers.Layer):
    config_class = ResNetConfig
    def __init__(self, config: ResNetConfig, **kwargs) -> None:
        ...
    
    @unpack_inputs
    def call(self, pixel_values: tf.Tensor, output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., training: bool = ...) -> Union[Tuple[tf.Tensor], TFBaseModelOutputWithPoolingAndNoAttention]:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


@add_start_docstrings("The bare ResNet model outputting raw features without any specific head on top.", RESNET_START_DOCSTRING)
class TFResNetModel(TFResNetPreTrainedModel):
    def __init__(self, config: ResNetConfig, **kwargs) -> None:
        ...
    
    @add_start_docstrings_to_model_forward(RESNET_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(checkpoint=_CHECKPOINT_FOR_DOC, output_type=TFBaseModelOutputWithPoolingAndNoAttention, config_class=_CONFIG_FOR_DOC, modality="vision", expected_output=_EXPECTED_OUTPUT_SHAPE)
    @unpack_inputs
    def call(self, pixel_values: tf.Tensor, output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., training: bool = ...) -> Union[Tuple[tf.Tensor], TFBaseModelOutputWithPoolingAndNoAttention]:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


@add_start_docstrings("""
    ResNet Model with an image classification head on top (a linear layer on top of the pooled features), e.g. for
    ImageNet.
    """, RESNET_START_DOCSTRING)
class TFResNetForImageClassification(TFResNetPreTrainedModel, TFSequenceClassificationLoss):
    def __init__(self, config: ResNetConfig, **kwargs) -> None:
        ...
    
    def classifier(self, x: tf.Tensor) -> tf.Tensor:
        ...
    
    @add_start_docstrings_to_model_forward(RESNET_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(checkpoint=_IMAGE_CLASS_CHECKPOINT, output_type=TFImageClassifierOutputWithNoAttention, config_class=_CONFIG_FOR_DOC, expected_output=_IMAGE_CLASS_EXPECTED_OUTPUT)
    @unpack_inputs
    def call(self, pixel_values: tf.Tensor = ..., labels: tf.Tensor = ..., output_hidden_states: bool = ..., return_dict: bool = ..., training: bool = ...) -> Union[Tuple[tf.Tensor], TFImageClassifierOutputWithNoAttention]:
        r"""
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    

