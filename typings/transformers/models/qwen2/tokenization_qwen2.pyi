"""
This type stub file was generated by pyright.
"""

from functools import lru_cache
from typing import Optional, Tuple
from ...tokenization_utils import PreTrainedTokenizer

"""Tokenization classes for Qwen2."""
logger = ...
VOCAB_FILES_NAMES = ...
MAX_MODEL_INPUT_SIZES = ...
PRETOKENIZE_REGEX = ...
@lru_cache()
def bytes_to_unicode(): # -> dict[int, str]:
    """
    Returns list of utf-8 byte and a mapping to unicode strings. We specifically avoids mapping to whitespace/control
    characters the bpe code barfs on.

    The reversible bpe codes work on unicode strings. This means you need a large # of unicode characters in your vocab
    if you want to avoid UNKs. When you're at something like a 10B token dataset you end up needing around 5K for
    decent coverage. This is a significant percentage of your normal, say, 32K bpe vocab. To avoid that, we want lookup
    tables between utf-8 bytes and unicode strings.
    """
    ...

def get_pairs(word): # -> set[Any]:
    """
    Return set of symbol pairs in a word.

    Word is represented as tuple of symbols (symbols being variable-length strings).
    """
    ...

class Qwen2Tokenizer(PreTrainedTokenizer):
    """
    Construct a Qwen2 tokenizer. Based on byte-level Byte-Pair-Encoding.

    Same with GPT2Tokenizer, this tokenizer has been trained to treat spaces like parts of the tokens so a word will
    be encoded differently whether it is at the beginning of the sentence (without space) or not:

    ```python
    >>> from transformers import Qwen2Tokenizer

    >>> tokenizer = Qwen2Tokenizer.from_pretrained("Qwen/Qwen-tokenizer")
    >>> tokenizer("Hello world")["input_ids"]
    [9707, 1879]

    >>> tokenizer(" Hello world")["input_ids"]
    [21927, 1879]
    ```
    This is expected.

    You should not use GPT2Tokenizer instead, because of the different pretokenization rules.

    This tokenizer inherits from [`PreTrainedTokenizer`] which contains most of the main methods. Users should refer to
    this superclass for more information regarding those methods.

    Args:
        vocab_file (`str`):
            Path to the vocabulary file.
        merges_file (`str`):
            Path to the merges file.
        errors (`str`, *optional*, defaults to `"replace"`):
            Paradigm to follow when decoding bytes to UTF-8. See
            [bytes.decode](https://docs.python.org/3/library/stdtypes.html#bytes.decode) for more information.
        unk_token (`str`, *optional*, defaults to `"<|endoftext|>"`):
            The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
            token instead.
        bos_token (`str`, *optional*):
            The beginning of sequence token. Not applicable for this tokenizer.
        eos_token (`str`, *optional*, defaults to `"<|endoftext|>"`):
            The end of sequence token.
        pad_token (`str`, *optional*, defaults to `"<|endoftext|>"`):
            The token used for padding, for example when batching sequences of different lengths.
        clean_up_tokenization_spaces (`bool`, *optional*, defaults to `False`):
            Whether or not the model should cleanup the spaces that were added when splitting the input text during the
            tokenization process. Not applicable to this tokenizer, since tokenization does not add spaces.
        split_special_tokens (`bool`, *optional*, defaults to `False`):
            Whether or not the special tokens should be split during the tokenization process. The default behavior is
            to not split special tokens. This means that if `<|endoftext|>` is the `eos_token`, then `tokenizer.tokenize("<|endoftext|>") =
            ['<|endoftext|>`]. Otherwise, if `split_special_tokens=True`, then `tokenizer.tokenize("<|endoftext|>")` will be give `['<',
            '|', 'endo', 'ft', 'ext', '|', '>']`. This argument is only supported for `slow` tokenizers for the moment.
    """
    vocab_files_names = ...
    model_input_names = ...
    def __init__(self, vocab_file, merges_file, errors=..., unk_token=..., bos_token=..., eos_token=..., pad_token=..., clean_up_tokenization_spaces=..., split_special_tokens=..., **kwargs) -> None:
        ...
    
    @property
    def vocab_size(self) -> int:
        ...
    
    def get_vocab(self): # -> dict[Any, Any]:
        ...
    
    def bpe(self, token): # -> LiteralString:
        ...
    
    def convert_tokens_to_string(self, tokens): # -> str:
        """Converts a sequence of tokens (string) in a single string."""
        ...
    
    def decode(self, token_ids, skip_special_tokens: bool = ..., clean_up_tokenization_spaces: Optional[bool] = ..., spaces_between_special_tokens: bool = ..., **kwargs) -> str:
        ...
    
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = ...) -> Tuple[str]:
        ...
    
    def prepare_for_tokenization(self, text, **kwargs): # -> tuple[str, dict[str, Any]]:
        ...
    

