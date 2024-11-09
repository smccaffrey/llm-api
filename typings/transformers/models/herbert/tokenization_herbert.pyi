"""
This type stub file was generated by pyright.
"""

from typing import List, Optional, Tuple
from ...tokenization_utils import PreTrainedTokenizer

logger = ...
VOCAB_FILES_NAMES = ...
def get_pairs(word): # -> set[Any]:
    """
    Return set of symbol pairs in a word. word is represented as tuple of symbols (symbols being variable-length
    strings)
    """
    ...

def replace_unicode_punct(text): # -> str:
    """
    Port of https://github.com/moses-smt/mosesdecoder/blob/master/scripts/tokenizer/replace-unicode-punctuation.perl
    """
    ...

def remove_non_printing_char(text): # -> LiteralString:
    """
    Port of https://github.com/moses-smt/mosesdecoder/blob/master/scripts/tokenizer/remove-non-printing-char.perl
    """
    ...

def whitespace_tokenize(text): # -> list[Any]:
    """Runs basic whitespace cleaning and splitting on a piece of text."""
    ...

class BasicTokenizer:
    """
    Constructs a BasicTokenizer that will run basic tokenization (punctuation splitting, lower casing, etc.).

    Args:
        do_lower_case (`bool`, *optional*, defaults to `True`):
            Whether or not to lowercase the input when tokenizing.
        never_split (`Iterable`, *optional*):
            Collection of tokens which will never be split during tokenization. Only has an effect when
            `do_basic_tokenize=True`
        tokenize_chinese_chars (`bool`, *optional*, defaults to `True`):
            Whether or not to tokenize Chinese characters.

            This should likely be deactivated for Japanese (see this
            [issue](https://github.com/huggingface/transformers/issues/328)).
        strip_accents (`bool`, *optional*):
            Whether or not to strip all accents. If this option is not specified, then it will be determined by the
            value for `lowercase` (as in the original BERT).
        do_split_on_punc (`bool`, *optional*, defaults to `True`):
            In some instances we want to skip the basic punctuation splitting so that later tokenization can capture
            the full context of the words, such as contractions.
    """
    def __init__(self, do_lower_case=..., never_split=..., tokenize_chinese_chars=..., strip_accents=..., do_split_on_punc=...) -> None:
        ...
    
    def tokenize(self, text, never_split=...): # -> list[Any] | list[LiteralString]:
        """
        Basic Tokenization of a piece of text. For sub-word tokenization, see WordPieceTokenizer.

        Args:
            never_split (`List[str]`, *optional*)
                Kept for backward compatibility purposes. Now implemented directly at the base class level (see
                [`PreTrainedTokenizer.tokenize`]) List of token not to split.
        """
        ...
    


class HerbertTokenizer(PreTrainedTokenizer):
    """
    Construct a BPE tokenizer for HerBERT.

    Peculiarities:

    - uses BERT's pre-tokenizer: BaseTokenizer splits tokens on spaces, and also on punctuation. Each occurrence of a
      punctuation character will be treated separately.

    - Such pretokenized input is BPE subtokenized

    This tokenizer inherits from [`XLMTokenizer`] which contains most of the methods. Users should refer to the
    superclass for more information regarding methods.
    """
    vocab_files_names = ...
    def __init__(self, vocab_file, merges_file, tokenizer_file=..., cls_token=..., unk_token=..., pad_token=..., mask_token=..., sep_token=..., bos_token=..., do_lowercase_and_remove_accent=..., additional_special_tokens=..., lang2id=..., id2lang=..., **kwargs) -> None:
        ...
    
    @property
    def do_lower_case(self): # -> bool:
        ...
    
    def moses_punct_norm(self, text, lang):
        ...
    
    def moses_tokenize(self, text, lang):
        ...
    
    def moses_pipeline(self, text, lang): # -> LiteralString:
        ...
    
    def ja_tokenize(self, text): # -> list[Any]:
        ...
    
    @property
    def vocab_size(self): # -> int:
        ...
    
    def get_vocab(self): # -> dict[Any, Any]:
        ...
    
    def bpe(self, token): # -> LiteralString | Literal['\n</w>']:
        ...
    
    def convert_tokens_to_string(self, tokens): # -> str:
        """Converts a sequence of tokens (string) in a single string."""
        ...
    
    def build_inputs_with_special_tokens(self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = ...) -> List[int]:
        """
        Build model inputs from a sequence or a pair of sequence for sequence classification tasks by concatenating and
        adding special tokens. An XLM sequence has the following format:

        - single sequence: `<s> X </s>`
        - pair of sequences: `<s> A </s> B </s>`

        Args:
            token_ids_0 (`List[int]`):
                List of IDs to which the special tokens will be added.
            token_ids_1 (`List[int]`, *optional*):
                Optional second list of IDs for sequence pairs.

        Returns:
            `List[int]`: List of [input IDs](../glossary#input-ids) with the appropriate special tokens.

        """
        ...
    
    def get_special_tokens_mask(self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = ..., already_has_special_tokens: bool = ...) -> List[int]:
        """
        Retrieve sequence ids from a token list that has no special tokens added. This method is called when adding
        special tokens using the tokenizer `prepare_for_model` method.

        Args:
            token_ids_0 (`List[int]`):
                List of IDs.
            token_ids_1 (`List[int]`, *optional*):
                Optional second list of IDs for sequence pairs.
            already_has_special_tokens (`bool`, *optional*, defaults to `False`):
                Whether or not the token list is already formatted with special tokens for the model.

        Returns:
            `List[int]`: A list of integers in the range [0, 1]: 1 for a special token, 0 for a sequence token.
        """
        ...
    
    def create_token_type_ids_from_sequences(self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = ...) -> List[int]:
        """
        Create a mask from the two sequences passed to be used in a sequence-pair classification task. An XLM sequence
        pair mask has the following format:

        ```
        0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1
        | first sequence    | second sequence |
        ```

        If `token_ids_1` is `None`, this method only returns the first portion of the mask (0s).

        Args:
            token_ids_0 (`List[int]`):
                List of IDs.
            token_ids_1 (`List[int]`, *optional*):
                Optional second list of IDs for sequence pairs.

        Returns:
            `List[int]`: List of [token type IDs](../glossary#token-type-ids) according to the given sequence(s).
        """
        ...
    
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = ...) -> Tuple[str]:
        ...
    
    def __getstate__(self): # -> dict[str, Any]:
        ...
    
    def __setstate__(self, d): # -> None:
        ...
    

