"""
This type stub file was generated by pyright.
"""

import numpy as np
from contextlib import contextmanager
from dataclasses import dataclass
from multiprocessing import Pool
from typing import Dict, Iterable, List, Optional, TYPE_CHECKING, Union
from ...processing_utils import ProcessorMixin
from ...utils import ModelOutput
from pyctcdecode import BeamSearchDecoderCTC
from ...feature_extraction_utils import FeatureExtractionMixin
from ...tokenization_utils import PreTrainedTokenizerBase

"""
Speech processor class for Wav2Vec2
"""
logger = ...
if TYPE_CHECKING:
    ...
ListOfDict = List[Dict[str, Union[int, str]]]
@dataclass
class Wav2Vec2DecoderWithLMOutput(ModelOutput):
    """
    Output type of [`Wav2Vec2DecoderWithLM`], with transcription.

    Args:
        text (list of `str` or `str`):
            Decoded logits in text from. Usually the speech transcription.
        logit_score (list of `float` or `float`):
            Total logit score of the beams associated with produced text.
        lm_score (list of `float`):
            Fused lm_score of the beams associated with produced text.
        word_offsets (list of `List[Dict[str, Union[int, str]]]` or `List[Dict[str, Union[int, str]]]`):
            Offsets of the decoded words. In combination with sampling rate and model downsampling rate word offsets
            can be used to compute time stamps for each word.
    """
    text: Union[List[List[str]], List[str], str]
    logit_score: Union[List[List[float]], List[float], float] = ...
    lm_score: Union[List[List[float]], List[float], float] = ...
    word_offsets: Union[List[List[ListOfDict]], List[ListOfDict], ListOfDict] = ...


class Wav2Vec2ProcessorWithLM(ProcessorMixin):
    r"""
    Constructs a Wav2Vec2 processor which wraps a Wav2Vec2 feature extractor, a Wav2Vec2 CTC tokenizer and a decoder
    with language model support into a single processor for language model boosted speech recognition decoding.

    Args:
        feature_extractor ([`Wav2Vec2FeatureExtractor`] or [`SeamlessM4TFeatureExtractor`]):
            An instance of [`Wav2Vec2FeatureExtractor`] or [`SeamlessM4TFeatureExtractor`]. The feature extractor is a required input.
        tokenizer ([`Wav2Vec2CTCTokenizer`]):
            An instance of [`Wav2Vec2CTCTokenizer`]. The tokenizer is a required input.
        decoder (`pyctcdecode.BeamSearchDecoderCTC`):
            An instance of [`pyctcdecode.BeamSearchDecoderCTC`]. The decoder is a required input.
    """
    feature_extractor_class = ...
    tokenizer_class = ...
    def __init__(self, feature_extractor: FeatureExtractionMixin, tokenizer: PreTrainedTokenizerBase, decoder: BeamSearchDecoderCTC) -> None:
        ...
    
    def save_pretrained(self, save_directory): # -> None:
        ...
    
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, **kwargs): # -> Self:
        r"""
        Instantiate a [`Wav2Vec2ProcessorWithLM`] from a pretrained Wav2Vec2 processor.

        <Tip>

        This class method is simply calling the feature extractor's
        [`~feature_extraction_utils.FeatureExtractionMixin.from_pretrained`], Wav2Vec2CTCTokenizer's
        [`~tokenization_utils_base.PreTrainedTokenizerBase.from_pretrained`], and
        [`pyctcdecode.BeamSearchDecoderCTC.load_from_hf_hub`].

        Please refer to the docstrings of the methods above for more information.

        </Tip>

        Args:
            pretrained_model_name_or_path (`str` or `os.PathLike`):
                This can be either:

                - a string, the *model id* of a pretrained feature_extractor hosted inside a model repo on
                  huggingface.co.
                - a path to a *directory* containing a feature extractor file saved using the
                  [`~SequenceFeatureExtractor.save_pretrained`] method, e.g., `./my_model_directory/`.
                - a path or url to a saved feature extractor JSON *file*, e.g.,
                  `./my_model_directory/preprocessor_config.json`.
            **kwargs
                Additional keyword arguments passed along to both [`SequenceFeatureExtractor`] and
                [`PreTrainedTokenizer`]
        """
        ...
    
    @property
    def language_model(self):
        ...
    
    @staticmethod
    def get_missing_alphabet_tokens(decoder, tokenizer): # -> set[Any]:
        ...
    
    def __call__(self, *args, **kwargs):
        """
        When used in normal mode, this method forwards all its arguments to the feature extractor's
        [`~FeatureExtractionMixin.__call__`] and returns its output. If used in the context
        [`~Wav2Vec2ProcessorWithLM.as_target_processor`] this method forwards all its arguments to
        Wav2Vec2CTCTokenizer's [`~Wav2Vec2CTCTokenizer.__call__`]. Please refer to the docstring of the above two
        methods for more information.
        """
        ...
    
    def pad(self, *args, **kwargs):
        """
        When used in normal mode, this method forwards all its arguments to the feature extractor's
        [`~FeatureExtractionMixin.pad`] and returns its output. If used in the context
        [`~Wav2Vec2ProcessorWithLM.as_target_processor`] this method forwards all its arguments to
        Wav2Vec2CTCTokenizer's [`~Wav2Vec2CTCTokenizer.pad`]. Please refer to the docstring of the above two methods
        for more information.
        """
        ...
    
    def batch_decode(self, logits: np.ndarray, pool: Optional[Pool] = ..., num_processes: Optional[int] = ..., beam_width: Optional[int] = ..., beam_prune_logp: Optional[float] = ..., token_min_logp: Optional[float] = ..., hotwords: Optional[Iterable[str]] = ..., hotword_weight: Optional[float] = ..., alpha: Optional[float] = ..., beta: Optional[float] = ..., unk_score_offset: Optional[float] = ..., lm_score_boundary: Optional[bool] = ..., output_word_offsets: bool = ..., n_best: int = ...): # -> Wav2Vec2DecoderWithLMOutput:
        """
        Batch decode output logits to audio transcription with language model support.

        <Tip>

        This function makes use of Python's multiprocessing. Currently, multiprocessing is available only on Unix
        systems (see this [issue](https://github.com/kensho-technologies/pyctcdecode/issues/65)).

        If you are decoding multiple batches, consider creating a `Pool` and passing it to `batch_decode`. Otherwise,
        `batch_decode` will be very slow since it will create a fresh `Pool` for each call. See usage example below.

        </Tip>

        Args:
            logits (`np.ndarray`):
                The logits output vector of the model representing the log probabilities for each token.
            pool (`multiprocessing.Pool`, *optional*):
                An optional user-managed pool. If not set, one will be automatically created and closed. The pool
                should be instantiated *after* `Wav2Vec2ProcessorWithLM`. Otherwise, the LM won't be available to the
                pool's sub-processes.

                <Tip>

                Currently, only pools created with a 'fork' context can be used. If a 'spawn' pool is passed, it will
                be ignored and sequential decoding will be used instead.

                </Tip>

            num_processes (`int`, *optional*):
                If `pool` is not set, number of processes on which the function should be parallelized over. Defaults
                to the number of available CPUs.
            beam_width (`int`, *optional*):
                Maximum number of beams at each step in decoding. Defaults to pyctcdecode's DEFAULT_BEAM_WIDTH.
            beam_prune_logp (`int`, *optional*):
                Beams that are much worse than best beam will be pruned Defaults to pyctcdecode's DEFAULT_PRUNE_LOGP.
            token_min_logp (`int`, *optional*):
                Tokens below this logp are skipped unless they are argmax of frame Defaults to pyctcdecode's
                DEFAULT_MIN_TOKEN_LOGP.
            hotwords (`List[str]`, *optional*):
                List of words with extra importance, can be OOV for LM
            hotword_weight (`int`, *optional*):
                Weight factor for hotword importance Defaults to pyctcdecode's DEFAULT_HOTWORD_WEIGHT.
            alpha (`float`, *optional*):
                Weight for language model during shallow fusion
            beta (`float`, *optional*):
                Weight for length score adjustment of during scoring
            unk_score_offset (`float`, *optional*):
                Amount of log score offset for unknown tokens
            lm_score_boundary (`bool`, *optional*):
                Whether to have kenlm respect boundaries when scoring
            output_word_offsets (`bool`, *optional*, defaults to `False`):
                Whether or not to output word offsets. Word offsets can be used in combination with the sampling rate
                and model downsampling rate to compute the time-stamps of transcribed words.
            n_best (`int`, *optional*, defaults to `1`):
                Number of best hypotheses to return. If `n_best` is greater than 1, the returned `text` will be a list
                of lists of strings, `logit_score` will be a list of lists of floats, and `lm_score` will be a list of
                lists of floats, where the length of the outer list will correspond to the batch size and the length of
                the inner list will correspond to the number of returned hypotheses . The value should be >= 1.

                <Tip>

                Please take a look at the Example of [`~Wav2Vec2ProcessorWithLM.decode`] to better understand how to
                make use of `output_word_offsets`. [`~Wav2Vec2ProcessorWithLM.batch_decode`] works the same way with
                batched output.

                </Tip>

        Returns:
            [`~models.wav2vec2.Wav2Vec2DecoderWithLMOutput`].

        Example:
            See [Decoding multiple audios](#decoding-multiple-audios).
        """
        ...
    
    def decode(self, logits: np.ndarray, beam_width: Optional[int] = ..., beam_prune_logp: Optional[float] = ..., token_min_logp: Optional[float] = ..., hotwords: Optional[Iterable[str]] = ..., hotword_weight: Optional[float] = ..., alpha: Optional[float] = ..., beta: Optional[float] = ..., unk_score_offset: Optional[float] = ..., lm_score_boundary: Optional[bool] = ..., output_word_offsets: bool = ..., n_best: int = ...): # -> Wav2Vec2DecoderWithLMOutput:
        """
        Decode output logits to audio transcription with language model support.

        Args:
            logits (`np.ndarray`):
                The logits output vector of the model representing the log probabilities for each token.
            beam_width (`int`, *optional*):
                Maximum number of beams at each step in decoding. Defaults to pyctcdecode's DEFAULT_BEAM_WIDTH.
            beam_prune_logp (`int`, *optional*):
                A threshold to prune beams with log-probs less than best_beam_logp + beam_prune_logp. The value should
                be <= 0. Defaults to pyctcdecode's DEFAULT_PRUNE_LOGP.
            token_min_logp (`int`, *optional*):
                Tokens with log-probs below token_min_logp are skipped unless they are have the maximum log-prob for an
                utterance. Defaults to pyctcdecode's DEFAULT_MIN_TOKEN_LOGP.
            hotwords (`List[str]`, *optional*):
                List of words with extra importance which can be missing from the LM's vocabulary, e.g. ["huggingface"]
            hotword_weight (`int`, *optional*):
                Weight multiplier that boosts hotword scores. Defaults to pyctcdecode's DEFAULT_HOTWORD_WEIGHT.
            alpha (`float`, *optional*):
                Weight for language model during shallow fusion
            beta (`float`, *optional*):
                Weight for length score adjustment of during scoring
            unk_score_offset (`float`, *optional*):
                Amount of log score offset for unknown tokens
            lm_score_boundary (`bool`, *optional*):
                Whether to have kenlm respect boundaries when scoring
            output_word_offsets (`bool`, *optional*, defaults to `False`):
                Whether or not to output word offsets. Word offsets can be used in combination with the sampling rate
                and model downsampling rate to compute the time-stamps of transcribed words.
            n_best (`int`, *optional*, defaults to `1`):
                Number of best hypotheses to return. If `n_best` is greater than 1, the returned `text` will be a list
                of strings, `logit_score` will be a list of floats, and `lm_score` will be a list of floats, where the
                length of these lists will correspond to the number of returned hypotheses. The value should be >= 1.

                <Tip>

                Please take a look at the example below to better understand how to make use of `output_word_offsets`.

                </Tip>

        Returns:
            [`~models.wav2vec2.Wav2Vec2DecoderWithLMOutput`].

        Example:

        ```python
        >>> # Let's see how to retrieve time steps for a model
        >>> from transformers import AutoTokenizer, AutoProcessor, AutoModelForCTC
        >>> from datasets import load_dataset
        >>> import datasets
        >>> import torch

        >>> # import model, feature extractor, tokenizer
        >>> model = AutoModelForCTC.from_pretrained("patrickvonplaten/wav2vec2-base-100h-with-lm")
        >>> processor = AutoProcessor.from_pretrained("patrickvonplaten/wav2vec2-base-100h-with-lm")

        >>> # load first sample of English common_voice
        >>> dataset = load_dataset("mozilla-foundation/common_voice_11_0", "en", split="train", streaming=True, trust_remote_code=True)
        >>> dataset = dataset.cast_column("audio", datasets.Audio(sampling_rate=16_000))
        >>> dataset_iter = iter(dataset)
        >>> sample = next(dataset_iter)

        >>> # forward sample through model to get greedily predicted transcription ids
        >>> input_values = processor(sample["audio"]["array"], return_tensors="pt").input_values
        >>> with torch.no_grad():
        ...     logits = model(input_values).logits[0].cpu().numpy()

        >>> # retrieve word stamps (analogous commands for `output_char_offsets`)
        >>> outputs = processor.decode(logits, output_word_offsets=True)
        >>> # compute `time_offset` in seconds as product of downsampling ratio and sampling_rate
        >>> time_offset = model.config.inputs_to_logits_ratio / processor.feature_extractor.sampling_rate

        >>> word_offsets = [
        ...     {
        ...         "word": d["word"],
        ...         "start_time": round(d["start_offset"] * time_offset, 2),
        ...         "end_time": round(d["end_offset"] * time_offset, 2),
        ...     }
        ...     for d in outputs.word_offsets
        ... ]
        >>> # compare word offsets with audio `en_train_0/common_voice_en_19121553.mp3` online on the dataset viewer:
        >>> # https://huggingface.co/datasets/mozilla-foundation/common_voice_11_0/viewer/en
        >>> word_offsets[:4]
        [{'word': 'THE', 'start_time': 0.68, 'end_time': 0.78}, {'word': 'TRACK', 'start_time': 0.88, 'end_time': 1.1}, {'word': 'APPEARS', 'start_time': 1.18, 'end_time': 1.66}, {'word': 'ON', 'start_time': 1.86, 'end_time': 1.92}]
        ```"""
        ...
    
    @contextmanager
    def as_target_processor(self): # -> Generator[None, Any, None]:
        """
        Temporarily sets the processor for processing the target. Useful for encoding the labels when fine-tuning
        Wav2Vec2.
        """
        ...
    

