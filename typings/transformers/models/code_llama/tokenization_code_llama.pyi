"""
This type stub file was generated by pyright.
"""

from typing import Any, Dict, List, Optional, Tuple
from ...tokenization_utils import PreTrainedTokenizer

"""Tokenization classes for Code LLaMA."""
logger = ...
VOCAB_FILES_NAMES = ...
SPIECE_UNDERLINE = ...
DEFAULT_SYSTEM_PROMPT = ...
class CodeLlamaTokenizer(PreTrainedTokenizer):
    """
    Construct a CodeLlama tokenizer. Based on byte-level Byte-Pair-Encoding. The default padding token is unset as
    there is no padding token in the original model.

    The default configuration match that of
    [codellama/CodeLlama-7b-Instruct-hf](https://huggingface.co/meta-llama/CodeLlama-7b-Instruct-hf/blob/main/tokenizer_config.json)
    which supports prompt infilling.

    Args:
        vocab_file (`str`):
            Path to the vocabulary file.
        unk_token (`str`, *optional*, defaults to `"<unk>"`):
            The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
            token instead.
        bos_token (`str`, *optional*, defaults to `"<s>"`):
            The beginning of sequence token that was used during pretraining. Can be used a sequence classifier token.
        eos_token (`str`, *optional*, defaults to `"</s>"`):
            The end of sequence token.

            <Tip>

            When building a sequence using special tokens, this is not the token that is used for the end of sequence.
            The token used is the `sep_token`.

            </Tip>

        prefix_token (`str`, *optional*, defaults to `"▁<PRE>"`):
            Prefix token used for infilling.
        middle_token (`str`, *optional*, defaults to `"▁<MID>"`):
            Middle token used for infilling.
        suffix_token (`str`, *optional*, defaults to `"▁<SUF>"`):
            Suffix token used for infilling.
        eot_token (`str`, *optional*, defaults to `"▁<EOT>"`):
            End of text token used for infilling.
        fill_token (`str`, *optional*, defaults to `"<FILL_ME>"`):
            The token used to split the input between the prefix and suffix.
        suffix_first (`bool`, *optional*, defaults to `False`):
            Whether the input prompt and suffix should be formatted with the suffix first.
        sp_model_kwargs (`dict`, *optional*):
            Will be passed to the `SentencePieceProcessor.__init__()` method. The [Python wrapper for
            SentencePiece](https://github.com/google/sentencepiece/tree/master/python) can be used, among other things,
            to set:

            - `enable_sampling`: Enable subword regularization.
            - `nbest_size`: Sampling parameters for unigram. Invalid for BPE-Dropout.

              - `nbest_size = {0,1}`: No sampling is performed.
              - `nbest_size > 1`: samples from the nbest_size results.
              - `nbest_size < 0`: assuming that nbest_size is infinite and samples from the all hypothesis (lattice)
                using forward-filtering-and-backward-sampling algorithm.

            - `alpha`: Smoothing parameter for unigram sampling, and dropout probability of merge operations for
              BPE-dropout.
        add_bos_token (`bool`, *optional*, defaults to `True`):
            Whether to add a beginning of sequence token at the start of sequences.
        add_eos_token (`bool`, *optional*, defaults to `False`):
            Whether to add an end of sequence token at the end of sequences.
        clean_up_tokenization_spaces (`bool`, *optional*, defaults to `False`):
            Whether or not to clean up the tokenization spaces.
        additional_special_tokens (`List[str]`, *optional*):
            Additional special tokens used by the tokenizer.
        use_default_system_prompt (`bool`, *optional*, defaults to `False`):
            Whether or not the default system prompt for Llama should be used.
    """
    vocab_files_names = ...
    model_input_names = ...
    def __init__(self, vocab_file, unk_token=..., bos_token=..., eos_token=..., prefix_token=..., middle_token=..., suffix_token=..., eot_token=..., fill_token=..., suffix_first=..., sp_model_kwargs: Optional[Dict[str, Any]] = ..., add_bos_token=..., add_eos_token=..., clean_up_tokenization_spaces=..., additional_special_tokens=..., use_default_system_prompt=..., **kwargs) -> None:
        ...
    
    @property
    def unk_token_length(self): # -> int:
        ...
    
    def get_spm_processor(self): # -> SentencePieceProcessor:
        ...
    
    @property
    def prefix_token(self): # -> str:
        ...
    
    @property
    def prefix_id(self): # -> int | List[int] | None:
        ...
    
    @property
    def middle_token(self): # -> str:
        ...
    
    @property
    def middle_id(self): # -> int | List[int] | None:
        ...
    
    @property
    def suffix_token(self): # -> str:
        ...
    
    @property
    def suffix_id(self): # -> int | List[int] | None:
        ...
    
    @property
    def eot_token(self): # -> str:
        ...
    
    @property
    def eot_id(self): # -> int | List[int] | None:
        ...
    
    @property
    def vocab_size(self):
        """Returns vocab size"""
        ...
    
    def get_vocab(self): # -> dict[str, int]:
        """Returns vocab as a dict"""
        ...
    
    def tokenize(self, prefix, suffix=..., suffix_first=..., **kwargs) -> List[int]:
        ...
    
    def convert_tokens_to_string(self, tokens):
        """Converts a sequence of tokens (string) in a single string."""
        ...
    
    def save_vocabulary(self, save_directory, filename_prefix: Optional[str] = ...) -> Tuple[str]:
        """
        Save the vocabulary and special tokens file to a directory.

        Args:
            save_directory (`str`):
                The directory in which to save the vocabulary.

        Returns:
            `Tuple(str)`: Paths to the files saved.
        """
        ...
    
    def build_inputs_with_special_tokens(self, token_ids_0, token_ids_1=...): # -> list[int | None]:
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
        Creates a mask from the two sequences passed to be used in a sequence-pair classification task. An ALBERT
        sequence pair mask has the following format:

        ```
        0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1
        | first sequence    | second sequence |
        ```

        if token_ids_1 is None, only returns the first portion of the mask (0s).

        Args:
            token_ids_0 (`List[int]`):
                List of ids.
            token_ids_1 (`List[int]`, *optional*):
                Optional second list of IDs for sequence pairs.

        Returns:
            `List[int]`: List of [token type IDs](../glossary#token-type-ids) according to the given sequence(s).
        """
        ...
    
    def __getstate__(self): # -> dict[str, Any]:
        ...
    
    def __setstate__(self, d): # -> None:
        ...
    

