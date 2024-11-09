"""
This type stub file was generated by pyright.
"""

from typing import List, Optional, Tuple
from ...tokenization_utils_fast import PreTrainedTokenizerFast
from ...utils import is_sentencepiece_available
from .tokenization_pegasus import PegasusTokenizer

"""Tokenization class for model PEGASUS."""
if is_sentencepiece_available():
    ...
else:
    PegasusTokenizer = ...
logger = ...
SPIECE_UNDERLINE = ...
VOCAB_FILES_NAMES = ...
class PegasusTokenizerFast(PreTrainedTokenizerFast):
    r"""
    Construct a "fast" PEGASUS tokenizer (backed by HuggingFace's *tokenizers* library). Based on
    [Unigram](https://huggingface.co/docs/tokenizers/python/latest/components.html?highlight=unigram#models).

    This tokenizer inherits from [`PreTrainedTokenizerFast`] which contains most of the main methods. Users should
    refer to this superclass for more information regarding those methods.

    Args:
        vocab_file (`str`):
            [SentencePiece](https://github.com/google/sentencepiece) file (generally has a *.spm* extension) that
            contains the vocabulary necessary to instantiate a tokenizer.
        pad_token (`str`, *optional*, defaults to `"<pad>"`):
            The token used for padding, for example when batching sequences of different lengths.
        eos_token (`str`, *optional*, defaults to `"</s>"`):
            The end of sequence token.

            <Tip>

            When building a sequence using special tokens, this is not the token that is used for the end of sequence.
            The token used is the `sep_token`.

            </Tip>

        unk_token (`str`, *optional*, defaults to `"<unk>"`):
            The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
            token instead.
        mask_token (`str`, *optional*, defaults to `"<mask_2>"`):
            The token used for masking single token values. This is the token used when training this model with masked
            language modeling (MLM). This is the token that the PEGASUS encoder will try to predict during pretraining.
            It corresponds to *[MASK2]* in [PEGASUS: Pre-training with Extracted Gap-sentences for Abstractive
            Summarization](https://arxiv.org/pdf/1912.08777.pdf).
        mask_token_sent (`str`, *optional*, defaults to `"<mask_1>"`):
            The token used for masking whole target sentences. This is the token used when training this model with gap
            sentences generation (GSG). This is the sentence that the PEGASUS decoder will try to predict during
            pretraining. It corresponds to *[MASK1]* in [PEGASUS: Pre-training with Extracted Gap-sentences for
            Abstractive Summarization](https://arxiv.org/pdf/1912.08777.pdf).
        additional_special_tokens (`List[str]`, *optional*):
            Additional special tokens used by the tokenizer. If no additional_special_tokens are provided <mask_2> and
            <unk_2, ..., unk_102> are used as additional special tokens corresponding to the [original PEGASUS
            tokenizer](https://github.com/google-research/pegasus/blob/939830367bcf411193d2b5eca2f2f90f3f9260ca/pegasus/ops/pretrain_parsing_ops.cc#L66)
            that uses the tokens 2 - 104 only for pretraining
    """
    vocab_files_names = ...
    slow_tokenizer_class = ...
    model_input_names = ...
    def __init__(self, vocab_file=..., tokenizer_file=..., pad_token=..., eos_token=..., unk_token=..., mask_token=..., mask_token_sent=..., additional_special_tokens=..., offset=..., **kwargs) -> None:
        ...
    
    @property
    def can_save_slow_tokenizer(self) -> bool:
        ...
    
    def get_special_tokens_mask(self, token_ids_0: List, token_ids_1: Optional[List] = ..., already_has_special_tokens: bool = ...) -> List[int]:
        """Get list where entries are [1] if a token is [eos] or [pad] else 0."""
        ...
    
    def build_inputs_with_special_tokens(self, token_ids_0, token_ids_1=...) -> List[int]:
        """
        Build model inputs from a sequence by adding eos to the end. no bos token is added to the front.

        - single sequence: `X </s>`
        - pair of sequences: `A B </s>` (not intended use)

        Args:
            token_ids_0 (`List[int]`):
                List of IDs to which the special tokens will be added
            token_ids_1 (`List[int]`, *optional*):
                Optional second list of IDs for sequence pairs.

        Returns:
            `List[int]`: list of [input IDs](../glossary#input-ids) with the appropriate special tokens.
        """
        ...
    
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = ...) -> Tuple[str]:
        ...
    


