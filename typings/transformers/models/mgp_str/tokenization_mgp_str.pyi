"""
This type stub file was generated by pyright.
"""

from typing import Optional, Tuple
from ...tokenization_utils import PreTrainedTokenizer

"""Tokenization classes for MGT-STR CHAR."""
logger = ...
VOCAB_FILES_NAMES = ...
class MgpstrTokenizer(PreTrainedTokenizer):
    """
    Construct a MGP-STR char tokenizer.

    This tokenizer inherits from [`PreTrainedTokenizer`] which contains most of the main methods. Users should refer to
    this superclass for more information regarding those methods.

    Args:
        vocab_file (`str`):
            Path to the vocabulary file.
        unk_token (`str`, *optional*, defaults to `"[GO]"`):
            The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
            token instead.
        bos_token (`str`, *optional*, defaults to `"[GO]"`):
            The beginning of sequence token.
        eos_token (`str`, *optional*, defaults to `"[s]"`):
            The end of sequence token.
        pad_token (`str` or `tokenizers.AddedToken`, *optional*, defaults to `"[GO]"`):
            A special token used to make arrays of tokens the same size for batching purpose. Will then be ignored by
            attention mechanisms or loss computation.
    """
    vocab_files_names = ...
    def __init__(self, vocab_file, unk_token=..., bos_token=..., eos_token=..., pad_token=..., **kwargs) -> None:
        ...
    
    @property
    def vocab_size(self): # -> int:
        ...
    
    def get_vocab(self): # -> dict[Any, Any]:
        ...
    
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = ...) -> Tuple[str]:
        ...
    

