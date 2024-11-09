"""
This type stub file was generated by pyright.
"""

import numpy as np
from typing import Dict, List, Optional, TYPE_CHECKING, Tuple, Union
from ..data import SquadExample
from ..modelcard import ModelCard
from ..tokenization_utils import PreTrainedTokenizer
from ..utils import add_end_docstrings, is_tf_available, is_torch_available
from .base import ArgumentHandler, ChunkPipeline, build_pipeline_init_args
from ..modeling_tf_utils import TFPreTrainedModel
from ..modeling_utils import PreTrainedModel
from torch.utils.data import Dataset

logger = ...
if TYPE_CHECKING:
    ...
if is_tf_available():
    Dataset = ...
if is_torch_available():
    ...
def decode_spans(start: np.ndarray, end: np.ndarray, topk: int, max_answer_len: int, undesired_tokens: np.ndarray) -> Tuple:
    """
    Take the output of any `ModelForQuestionAnswering` and will generate probabilities for each span to be the actual
    answer.

    In addition, it filters out some unwanted/impossible cases like answer len being greater than max_answer_len or
    answer end position being before the starting position. The method supports output the k-best answer through the
    topk argument.

    Args:
        start (`np.ndarray`): Individual start probabilities for each token.
        end (`np.ndarray`): Individual end probabilities for each token.
        topk (`int`): Indicates how many possible answer span(s) to extract from the model output.
        max_answer_len (`int`): Maximum size of the answer to extract from the model's output.
        undesired_tokens (`np.ndarray`): Mask determining tokens that can be part of the answer
    """
    ...

def select_starts_ends(start, end, p_mask, attention_mask, min_null_score=..., top_k=..., handle_impossible_answer=..., max_answer_len=...): # -> tuple[Any, Any, Any, int]:
    """
    Takes the raw output of any `ModelForQuestionAnswering` and first normalizes its outputs and then uses
    `decode_spans()` to generate probabilities for each span to be the actual answer.

    Args:
        start (`np.ndarray`): Individual start logits for each token.
        end (`np.ndarray`): Individual end logits for each token.
        p_mask (`np.ndarray`): A mask with 1 for values that cannot be in the answer
        attention_mask (`np.ndarray`): The attention mask generated by the tokenizer
        min_null_score(`float`): The minimum null (empty) answer score seen so far.
        topk (`int`): Indicates how many possible answer span(s) to extract from the model output.
        handle_impossible_answer(`bool`): Whether to allow null (empty) answers
        max_answer_len (`int`): Maximum size of the answer to extract from the model's output.
    """
    ...

class QuestionAnsweringArgumentHandler(ArgumentHandler):
    """
    QuestionAnsweringPipeline requires the user to provide multiple arguments (i.e. question & context) to be mapped to
    internal [`SquadExample`].

    QuestionAnsweringArgumentHandler manages all the possible to create a [`SquadExample`] from the command-line
    supplied arguments.
    """
    def normalize(self, item): # -> SquadExample | List[SquadExample]:
        ...
    
    def __call__(self, *args, **kwargs): # -> GeneratorType[Any, Any, Any] | Dataset[Any] | list[dict[Any, Any]] | list[dict[str, str]]:
        ...
    


@add_end_docstrings(build_pipeline_init_args(has_tokenizer=True))
class QuestionAnsweringPipeline(ChunkPipeline):
    """
    Question Answering pipeline using any `ModelForQuestionAnswering`. See the [question answering
    examples](../task_summary#question-answering) for more information.

    Example:

    ```python
    >>> from transformers import pipeline

    >>> oracle = pipeline(model="deepset/roberta-base-squad2")
    >>> oracle(question="Where do I live?", context="My name is Wolfgang and I live in Berlin")
    {'score': 0.9191, 'start': 34, 'end': 40, 'answer': 'Berlin'}
    ```

    Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

    This question answering pipeline can currently be loaded from [`pipeline`] using the following task identifier:
    `"question-answering"`.

    The models that this pipeline can use are models that have been fine-tuned on a question answering task. See the
    up-to-date list of available models on
    [huggingface.co/models](https://huggingface.co/models?filter=question-answering).
    """
    default_input_names = ...
    handle_impossible_answer = ...
    def __init__(self, model: Union[PreTrainedModel, TFPreTrainedModel], tokenizer: PreTrainedTokenizer, modelcard: Optional[ModelCard] = ..., framework: Optional[str] = ..., task: str = ..., **kwargs) -> None:
        ...
    
    @staticmethod
    def create_sample(question: Union[str, List[str]], context: Union[str, List[str]]) -> Union[SquadExample, List[SquadExample]]:
        """
        QuestionAnsweringPipeline leverages the [`SquadExample`] internally. This helper method encapsulate all the
        logic for converting question(s) and context(s) to [`SquadExample`].

        We currently support extractive question answering.

        Arguments:
            question (`str` or `List[str]`): The question(s) asked.
            context (`str` or `List[str]`): The context(s) in which we will look for the answer.

        Returns:
            One or a list of [`SquadExample`]: The corresponding [`SquadExample`] grouping question and context.
        """
        ...
    
    def __call__(self, *args, **kwargs): # -> list[Any] | PipelineIterator | Generator[Any, Any, None] | Tensor | Any | None:
        """
        Answer the question(s) given as inputs by using the context(s).

        Args:
            question (`str` or `List[str]`):
                One or several question(s) (must be used in conjunction with the `context` argument).
            context (`str` or `List[str]`):
                One or several context(s) associated with the question(s) (must be used in conjunction with the
                `question` argument).
            top_k (`int`, *optional*, defaults to 1):
                The number of answers to return (will be chosen by order of likelihood). Note that we return less than
                top_k answers if there are not enough options available within the context.
            doc_stride (`int`, *optional*, defaults to 128):
                If the context is too long to fit with the question for the model, it will be split in several chunks
                with some overlap. This argument controls the size of that overlap.
            max_answer_len (`int`, *optional*, defaults to 15):
                The maximum length of predicted answers (e.g., only answers with a shorter length are considered).
            max_seq_len (`int`, *optional*, defaults to 384):
                The maximum length of the total sentence (context + question) in tokens of each chunk passed to the
                model. The context will be split in several chunks (using `doc_stride` as overlap) if needed.
            max_question_len (`int`, *optional*, defaults to 64):
                The maximum length of the question after tokenization. It will be truncated if needed.
            handle_impossible_answer (`bool`, *optional*, defaults to `False`):
                Whether or not we accept impossible as an answer.
            align_to_words (`bool`, *optional*, defaults to `True`):
                Attempts to align the answer to real words. Improves quality on space separated languages. Might hurt on
                non-space-separated languages (like Japanese or Chinese)

        Return:
            A `dict` or a list of `dict`: Each result comes as a dictionary with the following keys:

            - **score** (`float`) -- The probability associated to the answer.
            - **start** (`int`) -- The character start index of the answer (in the tokenized version of the input).
            - **end** (`int`) -- The character end index of the answer (in the tokenized version of the input).
            - **answer** (`str`) -- The answer to the question.
        """
        ...
    
    def preprocess(self, example, padding=..., doc_stride=..., max_question_len=..., max_seq_len=...): # -> Generator[dict[str | Any, Any], Any, None]:
        ...
    
    def postprocess(self, model_outputs, top_k=..., handle_impossible_answer=..., max_answer_len=..., align_to_words=...): # -> list[Any]:
        ...
    
    def get_indices(self, enc: tokenizers.Encoding, s: int, e: int, sequence_index: int, align_to_words: bool) -> Tuple[int, int]:
        ...
    
    def span_to_answer(self, text: str, start: int, end: int) -> Dict[str, Union[str, int]]:
        """
        When decoding from token probabilities, this method maps token indexes to actual word in the initial context.

        Args:
            text (`str`): The actual context to extract the answer from.
            start (`int`): The answer starting token index.
            end (`int`): The answer end token index.

        Returns:
            Dictionary like `{'answer': str, 'start': int, 'end': int}`
        """
        ...
    


