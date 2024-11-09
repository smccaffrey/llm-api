"""
This type stub file was generated by pyright.
"""

import tensorflow as tf
from typing import List, Optional, Tuple, Union
from ...modeling_tf_outputs import TFBaseModelOutput, TFQuestionAnsweringModelOutput, TFSequenceClassifierOutput, TFTokenClassifierOutput
from ...modeling_tf_utils import TFPreTrainedModel, TFQuestionAnsweringLoss, TFSequenceClassificationLoss, TFTokenClassificationLoss, keras, keras_serializable, unpack_inputs
from ...utils import add_start_docstrings, add_start_docstrings_to_model_forward, replace_return_docstrings
from .configuration_layoutlmv3 import LayoutLMv3Config

"""TF 2.0 LayoutLMv3 model."""
_CONFIG_FOR_DOC = ...
_DUMMY_INPUT_IDS = ...
_DUMMY_BBOX = ...
LARGE_NEGATIVE = ...
class TFLayoutLMv3PatchEmbeddings(keras.layers.Layer):
    """LayoutLMv3 image (patch) embeddings."""
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None:
        ...
    
    def call(self, pixel_values: tf.Tensor) -> tf.Tensor:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFLayoutLMv3TextEmbeddings(keras.layers.Layer):
    """
    LayoutLMv3 text embeddings. Same as `RobertaEmbeddings` but with added spatial (layout) embeddings.
    """
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None:
        ...
    
    def calculate_spatial_position_embeddings(self, bbox: tf.Tensor) -> tf.Tensor:
        ...
    
    def create_position_ids_from_inputs_embeds(self, inputs_embds: tf.Tensor) -> tf.Tensor:
        """
        We are provided embeddings directly. We cannot infer which are padded, so just generate sequential position
        ids.
        """
        ...
    
    def create_position_ids_from_input_ids(self, input_ids: tf.Tensor) -> tf.Tensor:
        """
        Replace non-padding symbols with their position numbers. Position numbers begin at padding_token_index + 1.
        """
        ...
    
    def create_position_ids(self, input_ids: tf.Tensor, inputs_embeds: tf.Tensor) -> tf.Tensor:
        ...
    
    def call(self, input_ids: tf.Tensor | None = ..., bbox: tf.Tensor = ..., token_type_ids: tf.Tensor | None = ..., position_ids: tf.Tensor | None = ..., inputs_embeds: tf.Tensor | None = ..., training: bool = ...) -> tf.Tensor:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFLayoutLMv3SelfAttention(keras.layers.Layer):
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None:
        ...
    
    def transpose_for_scores(self, x: tf.Tensor):
        ...
    
    def cogview_attention(self, attention_scores: tf.Tensor, alpha: Union[float, int] = ...):
        """
        https://arxiv.org/abs/2105.13290 Section 2.4 Stabilization of training: Precision Bottleneck Relaxation
        (PB-Relax). A replacement of the original keras.layers.Softmax(axis=-1)(attention_scores). Seems the new
        attention_probs will result in a slower speed and a little bias. Can use
        tf.debugging.assert_near(standard_attention_probs, cogview_attention_probs, atol=1e-08) for comparison. The
        smaller atol (e.g., 1e-08), the better.
        """
        ...
    
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor | None, head_mask: tf.Tensor | None, output_attentions: bool, rel_pos: tf.Tensor | None = ..., rel_2d_pos: tf.Tensor | None = ..., training: bool = ...) -> Union[Tuple[tf.Tensor], Tuple[tf.Tensor, tf.Tensor]]:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFLayoutLMv3SelfOutput(keras.layers.Layer):
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None:
        ...
    
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = ...) -> tf.Tensor:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFLayoutLMv3Attention(keras.layers.Layer):
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None:
        ...
    
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor | None, head_mask: tf.Tensor | None, output_attentions: bool, rel_pos: tf.Tensor | None = ..., rel_2d_pos: tf.Tensor | None = ..., training: bool = ...) -> Union[Tuple[tf.Tensor], Tuple[tf.Tensor, tf.Tensor]]:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFLayoutLMv3Intermediate(keras.layers.Layer):
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None:
        ...
    
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFLayoutLMv3Output(keras.layers.Layer):
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None:
        ...
    
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = ...) -> tf.Tensor:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFLayoutLMv3Layer(keras.layers.Layer):
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None:
        ...
    
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor | None, head_mask: tf.Tensor | None, output_attentions: bool, rel_pos: tf.Tensor | None = ..., rel_2d_pos: tf.Tensor | None = ..., training: bool = ...) -> Union[Tuple[tf.Tensor], Tuple[tf.Tensor, tf.Tensor]]:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFLayoutLMv3Encoder(keras.layers.Layer):
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None:
        ...
    
    def relative_position_bucket(self, relative_positions: tf.Tensor, num_buckets: int, max_distance: int):
        ...
    
    def call(self, hidden_states: tf.Tensor, bbox: tf.Tensor | None = ..., attention_mask: tf.Tensor | None = ..., head_mask: tf.Tensor | None = ..., output_attentions: bool = ..., output_hidden_states: bool = ..., return_dict: bool = ..., position_ids: tf.Tensor | None = ..., training: bool = ...) -> Union[TFBaseModelOutput, Tuple[tf.Tensor], Tuple[tf.Tensor, tf.Tensor], Tuple[tf.Tensor, tf.Tensor, tf.Tensor],]:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


@keras_serializable
class TFLayoutLMv3MainLayer(keras.layers.Layer):
    config_class = LayoutLMv3Config
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    
    def get_input_embeddings(self) -> keras.layers.Layer:
        ...
    
    def set_input_embeddings(self, value: tf.Variable): # -> None:
        ...
    
    def init_visual_bbox(self, image_size: Tuple[int, int], max_len: int = ...): # -> None:
        ...
    
    def calculate_visual_bbox(self, batch_size: int, dtype: tf.DType):
        ...
    
    def embed_image(self, pixel_values: tf.Tensor) -> tf.Tensor:
        ...
    
    def get_extended_attention_mask(self, attention_mask: tf.Tensor) -> tf.Tensor:
        ...
    
    def get_head_mask(self, head_mask: tf.Tensor | None) -> Union[tf.Tensor, List[tf.Tensor | None]]:
        ...
    
    @unpack_inputs
    def call(self, input_ids: tf.Tensor | None = ..., bbox: tf.Tensor | None = ..., attention_mask: tf.Tensor | None = ..., token_type_ids: tf.Tensor | None = ..., position_ids: tf.Tensor | None = ..., head_mask: tf.Tensor | None = ..., inputs_embeds: tf.Tensor | None = ..., pixel_values: tf.Tensor | None = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., training: bool = ...) -> Union[TFBaseModelOutput, Tuple[tf.Tensor], Tuple[tf.Tensor, tf.Tensor], Tuple[tf.Tensor, tf.Tensor, tf.Tensor],]:
        ...
    


class TFLayoutLMv3PreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = LayoutLMv3Config
    base_model_prefix = ...
    @property
    def input_signature(self): # -> Dict[str, Any]:
        ...
    


LAYOUTLMV3_START_DOCSTRING = ...
LAYOUTLMV3_INPUTS_DOCSTRING = ...
@add_start_docstrings("The bare LayoutLMv3 Model transformer outputting raw hidden-states without any specific head on top.", LAYOUTLMV3_START_DOCSTRING)
class TFLayoutLMv3Model(TFLayoutLMv3PreTrainedModel):
    _keys_to_ignore_on_load_unexpected = ...
    def __init__(self, config, *inputs, **kwargs) -> None:
        ...
    
    @unpack_inputs
    @add_start_docstrings_to_model_forward(LAYOUTLMV3_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=TFBaseModelOutput, config_class=_CONFIG_FOR_DOC)
    def call(self, input_ids: tf.Tensor | None = ..., bbox: tf.Tensor | None = ..., attention_mask: tf.Tensor | None = ..., token_type_ids: tf.Tensor | None = ..., position_ids: tf.Tensor | None = ..., head_mask: tf.Tensor | None = ..., inputs_embeds: tf.Tensor | None = ..., pixel_values: tf.Tensor | None = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., training: bool = ...) -> Union[TFBaseModelOutput, Tuple[tf.Tensor], Tuple[tf.Tensor, tf.Tensor], Tuple[tf.Tensor, tf.Tensor, tf.Tensor],]:
        r"""
        Returns:

        Examples:

        ```python
        >>> from transformers import AutoProcessor, TFAutoModel
        >>> from datasets import load_dataset

        >>> processor = AutoProcessor.from_pretrained("microsoft/layoutlmv3-base", apply_ocr=False)
        >>> model = TFAutoModel.from_pretrained("microsoft/layoutlmv3-base")

        >>> dataset = load_dataset("nielsr/funsd-layoutlmv3", split="train", trust_remote_code=True)
        >>> example = dataset[0]
        >>> image = example["image"]
        >>> words = example["tokens"]
        >>> boxes = example["bboxes"]

        >>> encoding = processor(image, words, boxes=boxes, return_tensors="tf")

        >>> outputs = model(**encoding)
        >>> last_hidden_states = outputs.last_hidden_state
        ```"""
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


class TFLayoutLMv3ClassificationHead(keras.layers.Layer):
    """
    Head for sentence-level classification tasks. Reference: RobertaClassificationHead
    """
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None:
        ...
    
    def call(self, inputs: tf.Tensor, training: bool = ...) -> tf.Tensor:
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


@add_start_docstrings("""
    LayoutLMv3 Model with a sequence classification head on top (a linear layer on top of the final hidden state of the
    [CLS] token) e.g. for document image classification tasks such as the
    [RVL-CDIP](https://www.cs.cmu.edu/~aharley/rvl-cdip/) dataset.
    """, LAYOUTLMV3_START_DOCSTRING)
class TFLayoutLMv3ForSequenceClassification(TFLayoutLMv3PreTrainedModel, TFSequenceClassificationLoss):
    _keys_to_ignore_on_load_unexpected = ...
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None:
        ...
    
    @unpack_inputs
    @add_start_docstrings_to_model_forward(LAYOUTLMV3_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=TFSequenceClassifierOutput, config_class=_CONFIG_FOR_DOC)
    def call(self, input_ids: tf.Tensor | None = ..., attention_mask: tf.Tensor | None = ..., token_type_ids: tf.Tensor | None = ..., position_ids: tf.Tensor | None = ..., head_mask: tf.Tensor | None = ..., inputs_embeds: tf.Tensor | None = ..., labels: tf.Tensor | None = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., bbox: tf.Tensor | None = ..., pixel_values: tf.Tensor | None = ..., training: Optional[bool] = ...) -> Union[TFSequenceClassifierOutput, Tuple[tf.Tensor], Tuple[tf.Tensor, tf.Tensor], Tuple[tf.Tensor, tf.Tensor, tf.Tensor], Tuple[tf.Tensor, tf.Tensor, tf.Tensor, tf.Tensor],]:
        """
        Returns:

        Examples:

        ```python
        >>> from transformers import AutoProcessor, TFAutoModelForSequenceClassification
        >>> from datasets import load_dataset
        >>> import tensorflow as tf

        >>> processor = AutoProcessor.from_pretrained("microsoft/layoutlmv3-base", apply_ocr=False)
        >>> model = TFAutoModelForSequenceClassification.from_pretrained("microsoft/layoutlmv3-base")

        >>> dataset = load_dataset("nielsr/funsd-layoutlmv3", split="train", trust_remote_code=True)
        >>> example = dataset[0]
        >>> image = example["image"]
        >>> words = example["tokens"]
        >>> boxes = example["bboxes"]

        >>> encoding = processor(image, words, boxes=boxes, return_tensors="tf")
        >>> sequence_label = tf.convert_to_tensor([1])

        >>> outputs = model(**encoding, labels=sequence_label)
        >>> loss = outputs.loss
        >>> logits = outputs.logits
        ```"""
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


@add_start_docstrings("""
    LayoutLMv3 Model with a token classification head on top (a linear layer on top of the final hidden states) e.g.
    for sequence labeling (information extraction) tasks such as [FUNSD](https://guillaumejaume.github.io/FUNSD/),
    [SROIE](https://rrc.cvc.uab.es/?ch=13), [CORD](https://github.com/clovaai/cord) and
    [Kleister-NDA](https://github.com/applicaai/kleister-nda).
    """, LAYOUTLMV3_START_DOCSTRING)
class TFLayoutLMv3ForTokenClassification(TFLayoutLMv3PreTrainedModel, TFTokenClassificationLoss):
    _keys_to_ignore_on_load_unexpected = ...
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None:
        ...
    
    @unpack_inputs
    @add_start_docstrings_to_model_forward(LAYOUTLMV3_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=TFTokenClassifierOutput, config_class=_CONFIG_FOR_DOC)
    def call(self, input_ids: tf.Tensor | None = ..., bbox: tf.Tensor | None = ..., attention_mask: tf.Tensor | None = ..., token_type_ids: tf.Tensor | None = ..., position_ids: tf.Tensor | None = ..., head_mask: tf.Tensor | None = ..., inputs_embeds: tf.Tensor | None = ..., labels: tf.Tensor | None = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ..., pixel_values: tf.Tensor | None = ..., training: Optional[bool] = ...) -> Union[TFTokenClassifierOutput, Tuple[tf.Tensor], Tuple[tf.Tensor, tf.Tensor], Tuple[tf.Tensor, tf.Tensor, tf.Tensor], Tuple[tf.Tensor, tf.Tensor, tf.Tensor, tf.Tensor],]:
        r"""
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoProcessor, TFAutoModelForTokenClassification
        >>> from datasets import load_dataset

        >>> processor = AutoProcessor.from_pretrained("microsoft/layoutlmv3-base", apply_ocr=False)
        >>> model = TFAutoModelForTokenClassification.from_pretrained("microsoft/layoutlmv3-base", num_labels=7)

        >>> dataset = load_dataset("nielsr/funsd-layoutlmv3", split="train", trust_remote_code=True)
        >>> example = dataset[0]
        >>> image = example["image"]
        >>> words = example["tokens"]
        >>> boxes = example["bboxes"]
        >>> word_labels = example["ner_tags"]

        >>> encoding = processor(image, words, boxes=boxes, word_labels=word_labels, return_tensors="tf")

        >>> outputs = model(**encoding)
        >>> loss = outputs.loss
        >>> logits = outputs.logits
        ```"""
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    


@add_start_docstrings("""
    LayoutLMv3 Model with a span classification head on top for extractive question-answering tasks such as
    [DocVQA](https://rrc.cvc.uab.es/?ch=17) (a linear layer on top of the text part of the hidden-states output to
    compute `span start logits` and `span end logits`).
    """, LAYOUTLMV3_START_DOCSTRING)
class TFLayoutLMv3ForQuestionAnswering(TFLayoutLMv3PreTrainedModel, TFQuestionAnsweringLoss):
    _keys_to_ignore_on_load_unexpected = ...
    def __init__(self, config: LayoutLMv3Config, **kwargs) -> None:
        ...
    
    @unpack_inputs
    @add_start_docstrings_to_model_forward(LAYOUTLMV3_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=TFQuestionAnsweringModelOutput, config_class=_CONFIG_FOR_DOC)
    def call(self, input_ids: tf.Tensor | None = ..., attention_mask: tf.Tensor | None = ..., token_type_ids: tf.Tensor | None = ..., position_ids: tf.Tensor | None = ..., head_mask: tf.Tensor | None = ..., inputs_embeds: tf.Tensor | None = ..., start_positions: tf.Tensor | None = ..., end_positions: tf.Tensor | None = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., bbox: tf.Tensor | None = ..., pixel_values: tf.Tensor | None = ..., return_dict: Optional[bool] = ..., training: bool = ...) -> Union[TFQuestionAnsweringModelOutput, Tuple[tf.Tensor], Tuple[tf.Tensor, tf.Tensor], Tuple[tf.Tensor, tf.Tensor, tf.Tensor], Tuple[tf.Tensor, tf.Tensor, tf.Tensor, tf.Tensor],]:
        r"""
        start_positions (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the start of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        end_positions (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the end of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoProcessor, TFAutoModelForQuestionAnswering
        >>> from datasets import load_dataset
        >>> import tensorflow as tf

        >>> processor = AutoProcessor.from_pretrained("microsoft/layoutlmv3-base", apply_ocr=False)
        >>> model = TFAutoModelForQuestionAnswering.from_pretrained("microsoft/layoutlmv3-base")

        >>> dataset = load_dataset("nielsr/funsd-layoutlmv3", split="train", trust_remote_code=True)
        >>> example = dataset[0]
        >>> image = example["image"]
        >>> question = "what's his name?"
        >>> words = example["tokens"]
        >>> boxes = example["bboxes"]

        >>> encoding = processor(image, question, words, boxes=boxes, return_tensors="tf")
        >>> start_positions = tf.convert_to_tensor([1])
        >>> end_positions = tf.convert_to_tensor([3])

        >>> outputs = model(**encoding, start_positions=start_positions, end_positions=end_positions)
        >>> loss = outputs.loss
        >>> start_scores = outputs.start_logits
        >>> end_scores = outputs.end_logits
        ```"""
        ...
    
    def build(self, input_shape=...): # -> None:
        ...
    

