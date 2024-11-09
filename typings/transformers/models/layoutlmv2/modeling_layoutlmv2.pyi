"""
This type stub file was generated by pyright.
"""

import torch
from typing import Optional, Tuple, Union
from torch import nn
from ...modeling_outputs import BaseModelOutput, BaseModelOutputWithPooling, QuestionAnsweringModelOutput, SequenceClassifierOutput, TokenClassifierOutput
from ...modeling_utils import PreTrainedModel
from ...utils import add_start_docstrings, add_start_docstrings_to_model_forward, is_detectron2_available, replace_return_docstrings
from .configuration_layoutlmv2 import LayoutLMv2Config

"""PyTorch LayoutLMv2 model."""
if is_detectron2_available():
    ...
logger = ...
_CHECKPOINT_FOR_DOC = ...
_CONFIG_FOR_DOC = ...
class LayoutLMv2Embeddings(nn.Module):
    """Construct the embeddings from word, position and token_type embeddings."""
    def __init__(self, config) -> None:
        ...
    


class LayoutLMv2SelfAttention(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def transpose_for_scores(self, x):
        ...
    
    def compute_qkv(self, hidden_states): # -> tuple[Tensor | Any, Tensor | Any, Tensor | Any]:
        ...
    
    def forward(self, hidden_states, attention_mask=..., head_mask=..., output_attentions=..., rel_pos=..., rel_2d_pos=...): # -> tuple[Tensor, Any] | tuple[Tensor]:
        ...
    


class LayoutLMv2Attention(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def forward(self, hidden_states, attention_mask=..., head_mask=..., output_attentions=..., rel_pos=..., rel_2d_pos=...): # -> Any:
        ...
    


class LayoutLMv2SelfOutput(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def forward(self, hidden_states, input_tensor): # -> Any:
        ...
    


class LayoutLMv2Intermediate(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
        ...
    


class LayoutLMv2Output(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor:
        ...
    


class LayoutLMv2Layer(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def forward(self, hidden_states, attention_mask=..., head_mask=..., output_attentions=..., rel_pos=..., rel_2d_pos=...): # -> Any:
        ...
    
    def feed_forward_chunk(self, attention_output): # -> Any:
        ...
    


def relative_position_bucket(relative_position, bidirectional=..., num_buckets=..., max_distance=...): # -> Tensor:
    """
    Adapted from Mesh Tensorflow:
    https://github.com/tensorflow/mesh/blob/0cb87fe07da627bf0b7e60475d59f95ed6b5be3d/mesh_tensorflow/transformer/transformer_layers.py#L593
    Translate relative position to a bucket number for relative attention. The relative position is defined as
    memory_position - query_position, i.e. the distance in tokens from the attending position to the attended-to
    position. If bidirectional=False, then positive relative positions are invalid. We use smaller buckets for small
    absolute relative_position and larger buckets for larger absolute relative_positions. All relative positions
    >=max_distance map to the same bucket. All relative positions <=-max_distance map to the same bucket. This should
    allow for more graceful generalization to longer sequences than the model has been trained on.

    Args:
        relative_position: an int32 Tensor
        bidirectional: a boolean - whether the attention is bidirectional
        num_buckets: an integer
        max_distance: an integer

    Returns:
        a Tensor with the same shape as relative_position, containing int32 values in the range [0, num_buckets)
    """
    ...

class LayoutLMv2Encoder(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def forward(self, hidden_states, attention_mask=..., head_mask=..., output_attentions=..., output_hidden_states=..., return_dict=..., bbox=..., position_ids=...): # -> tuple[Any, ...] | BaseModelOutput:
        ...
    


class LayoutLMv2PreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = LayoutLMv2Config
    base_model_prefix = ...


def my_convert_sync_batchnorm(module, process_group=...): # -> SyncBatchNorm:
    ...

class LayoutLMv2VisualBackbone(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def forward(self, images): # -> Any:
        ...
    
    def synchronize_batch_norm(self): # -> None:
        ...
    


LAYOUTLMV2_START_DOCSTRING = ...
LAYOUTLMV2_INPUTS_DOCSTRING = ...
class LayoutLMv2Pooler(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def forward(self, hidden_states): # -> Any:
        ...
    


@add_start_docstrings("The bare LayoutLMv2 Model transformer outputting raw hidden-states without any specific head on top.", LAYOUTLMV2_START_DOCSTRING)
class LayoutLMv2Model(LayoutLMv2PreTrainedModel):
    def __init__(self, config) -> None:
        ...
    
    def get_input_embeddings(self): # -> Embedding:
        ...
    
    def set_input_embeddings(self, value): # -> None:
        ...
    
    @add_start_docstrings_to_model_forward(LAYOUTLMV2_INPUTS_DOCSTRING.format("(batch_size, sequence_length)"))
    @replace_return_docstrings(output_type=BaseModelOutput, config_class=_CONFIG_FOR_DOC)
    def forward(self, input_ids: Optional[torch.LongTensor] = ..., bbox: Optional[torch.LongTensor] = ..., image: Optional[torch.FloatTensor] = ..., attention_mask: Optional[torch.FloatTensor] = ..., token_type_ids: Optional[torch.LongTensor] = ..., position_ids: Optional[torch.LongTensor] = ..., head_mask: Optional[torch.FloatTensor] = ..., inputs_embeds: Optional[torch.FloatTensor] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple, BaseModelOutputWithPooling]:
        r"""
        Return:

        Examples:

        ```python
        >>> from transformers import AutoProcessor, LayoutLMv2Model, set_seed
        >>> from PIL import Image
        >>> import torch
        >>> from datasets import load_dataset

        >>> set_seed(0)

        >>> processor = AutoProcessor.from_pretrained("microsoft/layoutlmv2-base-uncased")
        >>> model = LayoutLMv2Model.from_pretrained("microsoft/layoutlmv2-base-uncased")


        >>> dataset = load_dataset("hf-internal-testing/fixtures_docvqa", trust_remote_code=True)
        >>> image_path = dataset["test"][0]["file"]
        >>> image = Image.open(image_path).convert("RGB")

        >>> encoding = processor(image, return_tensors="pt")

        >>> outputs = model(**encoding)
        >>> last_hidden_states = outputs.last_hidden_state

        >>> last_hidden_states.shape
        torch.Size([1, 342, 768])
        ```
        """
        ...
    


@add_start_docstrings("""
    LayoutLMv2 Model with a sequence classification head on top (a linear layer on top of the concatenation of the
    final hidden state of the [CLS] token, average-pooled initial visual embeddings and average-pooled final visual
    embeddings, e.g. for document image classification tasks such as the
    [RVL-CDIP](https://www.cs.cmu.edu/~aharley/rvl-cdip/) dataset.
    """, LAYOUTLMV2_START_DOCSTRING)
class LayoutLMv2ForSequenceClassification(LayoutLMv2PreTrainedModel):
    def __init__(self, config) -> None:
        ...
    
    def get_input_embeddings(self): # -> Embedding:
        ...
    
    @add_start_docstrings_to_model_forward(LAYOUTLMV2_INPUTS_DOCSTRING.format("batch_size, sequence_length"))
    @replace_return_docstrings(output_type=SequenceClassifierOutput, config_class=_CONFIG_FOR_DOC)
    def forward(self, input_ids: Optional[torch.LongTensor] = ..., bbox: Optional[torch.LongTensor] = ..., image: Optional[torch.FloatTensor] = ..., attention_mask: Optional[torch.FloatTensor] = ..., token_type_ids: Optional[torch.LongTensor] = ..., position_ids: Optional[torch.LongTensor] = ..., head_mask: Optional[torch.FloatTensor] = ..., inputs_embeds: Optional[torch.FloatTensor] = ..., labels: Optional[torch.LongTensor] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple, SequenceClassifierOutput]:
        r"""
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).

        Returns:

        Example:

        ```python
        >>> from transformers import AutoProcessor, LayoutLMv2ForSequenceClassification, set_seed
        >>> from PIL import Image
        >>> import torch
        >>> from datasets import load_dataset

        >>> set_seed(0)

        >>> dataset = load_dataset("aharley/rvl_cdip", split="train", streaming=True, trust_remote_code=True)
        >>> data = next(iter(dataset))
        >>> image = data["image"].convert("RGB")

        >>> processor = AutoProcessor.from_pretrained("microsoft/layoutlmv2-base-uncased")
        >>> model = LayoutLMv2ForSequenceClassification.from_pretrained(
        ...     "microsoft/layoutlmv2-base-uncased", num_labels=dataset.info.features["label"].num_classes
        ... )

        >>> encoding = processor(image, return_tensors="pt")
        >>> sequence_label = torch.tensor([data["label"]])

        >>> outputs = model(**encoding, labels=sequence_label)

        >>> loss, logits = outputs.loss, outputs.logits
        >>> predicted_idx = logits.argmax(dim=-1).item()
        >>> predicted_answer = dataset.info.features["label"].names[4]
        >>> predicted_idx, predicted_answer  # results are not good without further fine-tuning
        (7, 'advertisement')
        ```
        """
        ...
    


@add_start_docstrings("""
    LayoutLMv2 Model with a token classification head on top (a linear layer on top of the text part of the hidden
    states) e.g. for sequence labeling (information extraction) tasks such as
    [FUNSD](https://guillaumejaume.github.io/FUNSD/), [SROIE](https://rrc.cvc.uab.es/?ch=13),
    [CORD](https://github.com/clovaai/cord) and [Kleister-NDA](https://github.com/applicaai/kleister-nda).
    """, LAYOUTLMV2_START_DOCSTRING)
class LayoutLMv2ForTokenClassification(LayoutLMv2PreTrainedModel):
    def __init__(self, config) -> None:
        ...
    
    def get_input_embeddings(self): # -> Embedding:
        ...
    
    @add_start_docstrings_to_model_forward(LAYOUTLMV2_INPUTS_DOCSTRING.format("batch_size, sequence_length"))
    @replace_return_docstrings(output_type=TokenClassifierOutput, config_class=_CONFIG_FOR_DOC)
    def forward(self, input_ids: Optional[torch.LongTensor] = ..., bbox: Optional[torch.LongTensor] = ..., image: Optional[torch.FloatTensor] = ..., attention_mask: Optional[torch.FloatTensor] = ..., token_type_ids: Optional[torch.LongTensor] = ..., position_ids: Optional[torch.LongTensor] = ..., head_mask: Optional[torch.FloatTensor] = ..., inputs_embeds: Optional[torch.FloatTensor] = ..., labels: Optional[torch.LongTensor] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple, TokenClassifierOutput]:
        r"""
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.

        Returns:

        Example:

        ```python
        >>> from transformers import AutoProcessor, LayoutLMv2ForTokenClassification, set_seed
        >>> from PIL import Image
        >>> from datasets import load_dataset

        >>> set_seed(0)

        >>> datasets = load_dataset("nielsr/funsd", split="test", trust_remote_code=True)
        >>> labels = datasets.features["ner_tags"].feature.names
        >>> id2label = {v: k for v, k in enumerate(labels)}

        >>> processor = AutoProcessor.from_pretrained("microsoft/layoutlmv2-base-uncased", revision="no_ocr")
        >>> model = LayoutLMv2ForTokenClassification.from_pretrained(
        ...     "microsoft/layoutlmv2-base-uncased", num_labels=len(labels)
        ... )

        >>> data = datasets[0]
        >>> image = Image.open(data["image_path"]).convert("RGB")
        >>> words = data["words"]
        >>> boxes = data["bboxes"]  # make sure to normalize your bounding boxes
        >>> word_labels = data["ner_tags"]
        >>> encoding = processor(
        ...     image,
        ...     words,
        ...     boxes=boxes,
        ...     word_labels=word_labels,
        ...     padding="max_length",
        ...     truncation=True,
        ...     return_tensors="pt",
        ... )

        >>> outputs = model(**encoding)
        >>> logits, loss = outputs.logits, outputs.loss

        >>> predicted_token_class_ids = logits.argmax(-1)
        >>> predicted_tokens_classes = [id2label[t.item()] for t in predicted_token_class_ids[0]]
        >>> predicted_tokens_classes[:5]  # results are not good without further fine-tuning
        ['I-HEADER', 'I-HEADER', 'I-QUESTION', 'I-HEADER', 'I-QUESTION']
        ```
        """
        ...
    


@add_start_docstrings("""
    LayoutLMv2 Model with a span classification head on top for extractive question-answering tasks such as
    [DocVQA](https://rrc.cvc.uab.es/?ch=17) (a linear layer on top of the text part of the hidden-states output to
    compute `span start logits` and `span end logits`).
    """, LAYOUTLMV2_START_DOCSTRING)
class LayoutLMv2ForQuestionAnswering(LayoutLMv2PreTrainedModel):
    def __init__(self, config, has_visual_segment_embedding=...) -> None:
        ...
    
    def get_input_embeddings(self): # -> Embedding:
        ...
    
    @add_start_docstrings_to_model_forward(LAYOUTLMV2_INPUTS_DOCSTRING.format("batch_size, sequence_length"))
    @replace_return_docstrings(output_type=QuestionAnsweringModelOutput, config_class=_CONFIG_FOR_DOC)
    def forward(self, input_ids: Optional[torch.LongTensor] = ..., bbox: Optional[torch.LongTensor] = ..., image: Optional[torch.FloatTensor] = ..., attention_mask: Optional[torch.FloatTensor] = ..., token_type_ids: Optional[torch.LongTensor] = ..., position_ids: Optional[torch.LongTensor] = ..., head_mask: Optional[torch.FloatTensor] = ..., inputs_embeds: Optional[torch.FloatTensor] = ..., start_positions: Optional[torch.LongTensor] = ..., end_positions: Optional[torch.LongTensor] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple, QuestionAnsweringModelOutput]:
        r"""
        start_positions (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the start of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        end_positions (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the end of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.

        Returns:

        Example:

        In this example below, we give the LayoutLMv2 model an image (of texts) and ask it a question. It will give us
        a prediction of what it thinks the answer is (the span of the answer within the texts parsed from the image).

        ```python
        >>> from transformers import AutoProcessor, LayoutLMv2ForQuestionAnswering, set_seed
        >>> import torch
        >>> from PIL import Image
        >>> from datasets import load_dataset

        >>> set_seed(0)
        >>> processor = AutoProcessor.from_pretrained("microsoft/layoutlmv2-base-uncased")
        >>> model = LayoutLMv2ForQuestionAnswering.from_pretrained("microsoft/layoutlmv2-base-uncased")

        >>> dataset = load_dataset("hf-internal-testing/fixtures_docvqa", trust_remote_code=True)
        >>> image_path = dataset["test"][0]["file"]
        >>> image = Image.open(image_path).convert("RGB")
        >>> question = "When is coffee break?"
        >>> encoding = processor(image, question, return_tensors="pt")

        >>> outputs = model(**encoding)
        >>> predicted_start_idx = outputs.start_logits.argmax(-1).item()
        >>> predicted_end_idx = outputs.end_logits.argmax(-1).item()
        >>> predicted_start_idx, predicted_end_idx
        (30, 191)

        >>> predicted_answer_tokens = encoding.input_ids.squeeze()[predicted_start_idx : predicted_end_idx + 1]
        >>> predicted_answer = processor.tokenizer.decode(predicted_answer_tokens)
        >>> predicted_answer  # results are not good without further fine-tuning
        '44 a. m. to 12 : 25 p. m. 12 : 25 to 12 : 58 p. m. 12 : 58 to 4 : 00 p. m. 2 : 00 to 5 : 00 p. m. coffee break coffee will be served for men and women in the lobby adjacent to exhibit area. please move into exhibit area. ( exhibits open ) trrf general session ( part | ) presiding : lee a. waller trrf vice president “ introductory remarks ” lee a. waller, trrf vice presi - dent individual interviews with trrf public board members and sci - entific advisory council mem - bers conducted by trrf treasurer philip g. kuehn to get answers which the public refrigerated warehousing industry is looking for. plus questions from'
        ```

        ```python
        >>> target_start_index = torch.tensor([7])
        >>> target_end_index = torch.tensor([14])
        >>> outputs = model(**encoding, start_positions=target_start_index, end_positions=target_end_index)
        >>> predicted_answer_span_start = outputs.start_logits.argmax(-1).item()
        >>> predicted_answer_span_end = outputs.end_logits.argmax(-1).item()
        >>> predicted_answer_span_start, predicted_answer_span_end
        (30, 191)
        ```
        """
        ...
    


