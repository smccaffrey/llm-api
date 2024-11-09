"""
This type stub file was generated by pyright.
"""

from typing import List, Optional, Union
from ...processing_utils import ProcessorMixin
from ...tokenization_utils_base import BatchEncoding, PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy
from ...utils import TensorType

"""
Processor class for LayoutLMv2.
"""
class LayoutLMv2Processor(ProcessorMixin):
    r"""
    Constructs a LayoutLMv2 processor which combines a LayoutLMv2 image processor and a LayoutLMv2 tokenizer into a
    single processor.

    [`LayoutLMv2Processor`] offers all the functionalities you need to prepare data for the model.

    It first uses [`LayoutLMv2ImageProcessor`] to resize document images to a fixed size, and optionally applies OCR to
    get words and normalized bounding boxes. These are then provided to [`LayoutLMv2Tokenizer`] or
    [`LayoutLMv2TokenizerFast`], which turns the words and bounding boxes into token-level `input_ids`,
    `attention_mask`, `token_type_ids`, `bbox`. Optionally, one can provide integer `word_labels`, which are turned
    into token-level `labels` for token classification tasks (such as FUNSD, CORD).

    Args:
        image_processor (`LayoutLMv2ImageProcessor`, *optional*):
            An instance of [`LayoutLMv2ImageProcessor`]. The image processor is a required input.
        tokenizer (`LayoutLMv2Tokenizer` or `LayoutLMv2TokenizerFast`, *optional*):
            An instance of [`LayoutLMv2Tokenizer`] or [`LayoutLMv2TokenizerFast`]. The tokenizer is a required input.
    """
    attributes = ...
    image_processor_class = ...
    tokenizer_class = ...
    def __init__(self, image_processor=..., tokenizer=..., **kwargs) -> None:
        ...
    
    def __call__(self, images, text: Union[TextInput, PreTokenizedInput, List[TextInput], List[PreTokenizedInput]] = ..., text_pair: Optional[Union[PreTokenizedInput, List[PreTokenizedInput]]] = ..., boxes: Union[List[List[int]], List[List[List[int]]]] = ..., word_labels: Optional[Union[List[int], List[List[int]]]] = ..., add_special_tokens: bool = ..., padding: Union[bool, str, PaddingStrategy] = ..., truncation: Union[bool, str, TruncationStrategy] = ..., max_length: Optional[int] = ..., stride: int = ..., pad_to_multiple_of: Optional[int] = ..., return_token_type_ids: Optional[bool] = ..., return_attention_mask: Optional[bool] = ..., return_overflowing_tokens: bool = ..., return_special_tokens_mask: bool = ..., return_offsets_mapping: bool = ..., return_length: bool = ..., verbose: bool = ..., return_tensors: Optional[Union[str, TensorType]] = ..., **kwargs) -> BatchEncoding:
        """
        This method first forwards the `images` argument to [`~LayoutLMv2ImageProcessor.__call__`]. In case
        [`LayoutLMv2ImageProcessor`] was initialized with `apply_ocr` set to `True`, it passes the obtained words and
        bounding boxes along with the additional arguments to [`~LayoutLMv2Tokenizer.__call__`] and returns the output,
        together with resized `images`. In case [`LayoutLMv2ImageProcessor`] was initialized with `apply_ocr` set to
        `False`, it passes the words (`text`/``text_pair`) and `boxes` specified by the user along with the additional
        arguments to [`~LayoutLMv2Tokenizer.__call__`] and returns the output, together with resized `images``.

        Please refer to the docstring of the above two methods for more information.
        """
        ...
    
    def get_overflowing_images(self, images, overflow_to_sample_mapping): # -> list[Any]:
        ...
    
    def batch_decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to PreTrainedTokenizer's [`~PreTrainedTokenizer.batch_decode`]. Please
        refer to the docstring of this method for more information.
        """
        ...
    
    def decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to PreTrainedTokenizer's [`~PreTrainedTokenizer.decode`]. Please refer
        to the docstring of this method for more information.
        """
        ...
    
    @property
    def model_input_names(self): # -> list[str]:
        ...
    
    @property
    def feature_extractor_class(self): # -> str:
        ...
    
    @property
    def feature_extractor(self):
        ...
    

