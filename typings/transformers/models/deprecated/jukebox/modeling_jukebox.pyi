"""
This type stub file was generated by pyright.
"""

import torch
from typing import List, Optional, Tuple
from torch import nn
from torch.nn import LayerNorm as FusedLayerNorm
from ....modeling_utils import PreTrainedModel
from ....utils import add_start_docstrings
from .configuration_jukebox import JukeboxConfig, JukeboxPriorConfig, JukeboxVQVAEConfig

"""PyTorch Jukebox model."""
logger = ...
def filter_logits(logits, top_k=..., top_p=..., filter_value=...):
    """
    Filter a distribution of logits using top-k and/or nucleus (top-p) filtering

    Args:
        logits (`torch.Tensor`):
            logits distribution shape (vocabulary size)
        top_k (`int`, *optional*, defaults to 0):
            When `top_k >0` keep only top key tokens with highest probability (top-k filtering).
        top_p (`int`, *optional*, defaults to 0):
            When `top_p>0.0` keep the top tokens with cumulative probability >= `top_p` (nucleus filtering).
    """
    ...

def get_relevant_lyric_tokens(full_tokens, max_n_lyric_tokens, total_length, offset, duration): # -> tuple[Tensor | Any, Any | list[int]]:
    """
    Extract only the relevant tokens based on the character position. A total of `max_n_lyric_tokens` tokens will be
    returned. If the provided token sequence is smaller, it will be padded, otherwise, only characters ranging from the
    midpoint - `max_n_lyric_tokens//2` to the midpoint + `max_n_lyric_tokens//2` will be returned. This *focuses* on
    the most relevant tokens (in time) for the sequence.

    Args:
        full_tokens (`List[int]`):
            List containing the token ids of the entire lyrics.
        total_length (`int`):
            Total expected length of the music (not all of it is generated, see duration), in samples.
        offset (`int`):
            Starting sample in the music. If the offset is greater than 0, the lyrics will be shifted take that into
            account
        duration (`int`):
            Expected duration of the generated music, in samples. The duration has to be smaller than the total length,
            which represent the overall length of the signal,
    """
    ...

def get_starts(total_length, n_ctx, hop_length): # -> list[Any]:
    ...

def get_alignment(music_tokens, labels, prior, config): # -> list[Any]:
    ...

def save_temp_audio(fname, lvl, metas, aud): # -> None:
    ...

def get_mask(mask, query_length, key_value_length, blocks, spread, device, sample, sample_t): # -> Tensor | None:
    ...

class JukeboxConv1D(nn.Module):
    def __init__(self, input_width, output_width) -> None:
        ...
    
    def forward(self, hidden_states): # -> Tensor:
        ...
    


class JukeboxResConv1DBlock(nn.Module):
    def __init__(self, config, conv_width, depth=..., res_scale=...) -> None:
        ...
    
    def forward(self, hidden_states):
        ...
    


class JukeboxResnet1D(nn.Module):
    def __init__(self, config, conv_width, n_depth, reverse_dilation=...) -> None:
        ...
    
    def forward(self, hidden_states): # -> Any:
        ...
    


class JukeboxEncoderConvBlock(nn.Module):
    def __init__(self, config, embed_dim, hidden_dim, depth, down_t, stride_t) -> None:
        ...
    
    def forward(self, hidden_states): # -> Any:
        ...
    


class JukeboxEncoder(nn.Module):
    def __init__(self, config, width, depth, levels, downs_t, strides_t) -> None:
        ...
    
    def forward(self, hidden_states): # -> list[Any]:
        ...
    


class JukeboxDecoderConvBock(nn.Module):
    def __init__(self, config, embed_dim, hidden_dim, depth, down_t, stride_t, reverse_dilation=...) -> None:
        ...
    
    def forward(self, hidden_states): # -> Any:
        ...
    


class JukeboxDecoder(nn.Module):
    def __init__(self, config, hidden_dim, depth, levels, downs_t, strides_t) -> None:
        ...
    
    def forward(self, hidden_states, all_levels=...): # -> Any:
        ...
    


class JukeboxBottleneckBlock(nn.Module):
    def __init__(self, config: JukeboxVQVAEConfig) -> None:
        ...
    
    def init_codebook(self, hidden_states): # -> None:
        ...
    
    def update_codebook(self, hidden_states, latent_states): # -> dict[str, Any]:
        ...
    
    def preprocess(self, hidden_states): # -> tuple[Any, Any]:
        ...
    
    def postprocess(self, latent_states, dequantised_states, x_shape): # -> tuple[Any, Any]:
        ...
    
    def quantise(self, latent_states): # -> tuple[Tensor, Tensor]:
        ...
    
    def dequantise(self, music_tokens): # -> Tensor:
        ...
    
    def encode(self, latent_states): # -> Tensor:
        ...
    
    def decode(self, music_tokens): # -> Tensor:
        ...
    
    def forward(self, hidden_states, update_codebook=...): # -> tuple[Any, Any, Any, dict[str, Tensor]]:
        ...
    


class JukeboxBottleneck(nn.Module):
    def __init__(self, config, levels) -> None:
        ...
    
    def encode(self, raw_audio): # -> list[Any]:
        ...
    
    def decode(self, music_tokens, start_level=..., end_level=...): # -> list[Any]:
        ...
    
    def forward(self, input_audio): # -> tuple[list[Any], list[Any], list[Any], list[Any]]:
        ...
    


JUKEBOX_START_DOCSTRING = ...
@add_start_docstrings("""The Hierarchical VQ-VAE model used in Jukebox. This model follows the Hierarchical VQVAE paper from [Will Williams, Sam
Ringer, Tom Ash, John Hughes, David MacLeod, Jamie Dougherty](https://arxiv.org/abs/2002.08111).

    """, JUKEBOX_START_DOCSTRING)
class JukeboxVQVAE(PreTrainedModel):
    config_class = JukeboxVQVAEConfig
    base_model_prefix = ...
    def __init__(self, config: JukeboxVQVAEConfig) -> None:
        ...
    
    def decode(self, music_tokens, start_level=..., end_level=..., bs_chunks=...) -> torch.Tensor:
        """
        Transforms the input `music_tokens` to their `raw_audio` representation.

        Args:
            music_tokens (`torch.LongTensor`):
                Tensor of music tokens which will be decoded to raw audio by using the codebook. Each music token
                should be an index to a corresponding `code` vector in the codebook.
            start_level (`int`, *optional*):
                Level at which the decoding process will start. Default to 0.
            end_level (`int`, *optional*):
                Level at which the decoding process will start. Default to None.
            bs_chunks (int, *optional*):
                Number of chunks to process at the same time.
        """
        ...
    
    def encode(self, input_audio, start_level=..., end_level=..., bs_chunks=...): # -> list[Tensor]:
        """
        Transforms the `input_audio` to a discrete representation made out of `music_tokens`.

        Args:
            input_audio (`torch.Tensor`):
                Raw audio which will be encoded to its discrete representation using the codebook. The closest `code`
                form the codebook will be computed for each sequence of samples.
            start_level (`int`, *optional*, defaults to 0):
                Level at which the encoding process will start. Default to 0.
            end_level (`int`, *optional*):
                Level at which the encoding process will start. Default to None.
            bs_chunks (int, *optional*, defaults to 1):
                Number of chunks of raw audio to process at the same time.
        """
        ...
    
    def sample(self, n_samples): # -> Tensor:
        ...
    
    def forward(self, raw_audio: torch.FloatTensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Forward pass of the VQ-VAE, encodes the `raw_audio` to latent states, which are then decoded for each level.
        The commit loss, which ensure that the encoder's computed embeddings are close to the codebook vectors, is
        computed.

        Args:
            raw_audio (`torch.FloatTensor`):
                Audio input which will be encoded and decoded.

        Returns:
            `Tuple[torch.Tensor, torch.Tensor]`


        Example:
        ```python
        >>> from transformers import JukeboxVQVAE, set_seed
        >>> import torch

        >>> model = JukeboxVQVAE.from_pretrained("openai/jukebox-1b-lyrics").eval()
        >>> set_seed(0)
        >>> zs = [torch.randint(100, (4, 1))]
        >>> model.decode(zs).shape
        torch.Size([4, 8, 1])
        ```
        """
        ...
    


class JukeboxMLP(nn.Module):
    def __init__(self, config) -> None:
        ...
    
    def forward(self, hidden_states): # -> Any:
        ...
    


class JukeboxLayerNorm(FusedLayerNorm):
    def __init__(self, normalized_shape, eps=..., elementwise_affine=...) -> None:
        ...
    
    def forward(self, input): # -> Tensor:
        ...
    


class JukeboxAttention(nn.Module):
    def __init__(self, config, n_ctx, attn_func=...) -> None:
        ...
    
    def merge_heads(self, hidden_states):
        ...
    
    def split_heads(self, hidden_states, is_key=...):
        ...
    
    def dense_attn(self, query, key, value, sample): # -> Tensor:
        ...
    
    def block_attn(self, query, key, value, sample):
        ...
    
    def transpose_block_attn(self, query, key, value, sample):
        ...
    
    def prev_block_attn(self, query, key, value, sample):
        ...
    
    def summary_attn(self, query, key, value, sample):
        ...
    
    def summary_spread_attn(self, query, key, value, sample):
        ...
    
    def prime_attn(self, query, key, value, sample):
        ...
    
    def factored_qkv(self, hidden_states, last_encoder_hidden_states=..., sample=...): # -> tuple[Any | Tensor, Any | Tensor, Any | Tensor, bool]:
        ...
    
    def prime_qkv(self, hidden_states, last_encoder_hidden_states=..., sample=...): # -> tuple[Any, Any, Any, bool]:
        ...
    
    def decode_qkv(self, hidden_states, last_encoder_hidden_states=..., sample=...): # -> tuple[Any, Any, Any, bool]:
        ...
    
    def forward(self, hidden_states, last_encoder_hidden_states=..., sample=...): # -> Any:
        ...
    
    def del_cache(self): # -> None:
        ...
    


class JukeboxBlock(nn.Module):
    def __init__(self, config, n_ctx, attn_func=...) -> None:
        ...
    
    def forward(self, hidden_states, last_encoder_hidden_states, sample=...):
        ...
    


class JukeboxLayerStack(nn.Module):
    def __init__(self, config, n_ctx) -> None:
        ...
    
    def set_record_attn(self, record_attn): # -> None:
        """
        Makes forward prop dump self-attention softmaxes to self.saved_attn_weights.

        Args:
            record_attn (`Union[bool,set]`):
                Either a set of layer indices indicating which layers to store, or a boolean value indicating Whether
                to dump all.
        """
        ...
    
    def forward(self, hidden_states, last_encoder_hidden_states=..., sample=...): # -> Any:
        ...
    
    def del_cache(self): # -> None:
        ...
    


class JukeboxPositionalEmbedding(nn.Module):
    def __init__(self, embed_dim, width) -> None:
        ...
    
    def forward(self): # -> Parameter:
        ...
    


class JukeboxConditionalAutoregressive(nn.Module):
    def __init__(self, config, n_ctx=..., embed_dim=..., audio_conditioning=..., metadata_conditioning=..., is_encoder=...) -> None:
        """
        Autoregressive model on either lyric tokens or music tokens, or both. The attention pattern should be properly
        set fro each configuration.

        Args:
            config (`JukeboxPriorConfig`):
                Model configuration class with all the parameters of the model. Initializing with a config file does
                not load the weights associated with the model, only the configuration. Check out the
                [`~PreTrainedModel.from_pretrained`] method to load the model weights.
            n_ctx (`int`, *optional*):
                Number of tokens or lyrics tokens provided in a single pass.
            embed_dim (`int`, *optional*):
                Either equals to the dimension of the codebook, or the sum of n_vocab (lyrics) and codeboook dimension,
                if the model combines lyrics and music tokens, or simply n_vocab if the model is a seperate encoder
            audio_conditioning (`bool`, *optional*, defaults to `False`):
                Whether or not the prior supports conditionning on audio.
            metadata_conditioning (`bool`, *optional*, defaults to `False`):
                Whether or not the prior supports conditionning on artitst, genres, lyrics and timing.
            is_encoder (`bool`, *optional*, defaults to `False`):
                Whether the model is an encoder only model.
        """
        ...
    
    def forward(self, tokens, audio_conditioning=..., metadata_conditioning=..., last_encoder_hidden_states=..., get_preds=..., get_acts=..., get_sep_loss=...): # -> Any | tuple[tuple[Any, Any] | Any, Any] | tuple[tuple[Any, Any] | Any, None]:
        """
        Args:
            tokens (`torch.tensor`):
                Can represent music tokens, lyrics tokens or both, depending on the configuration.
        """
        ...
    
    def get_emb(self, sample_t, n_samples, tokens, audio_conditioning, metadata_conditioning): # -> tuple[Any, Any]:
        ...
    
    def sample(self, n_samples, audio_conditioning=..., metadata_conditioning=..., last_encoder_hidden_states=..., temp=..., top_k=..., top_p=..., get_preds=..., sample_tokens=...): # -> tuple[Tensor, Tensor | Any | list[Any]] | Tensor:
        ...
    
    def split_chunks(self, length, chunk_size): # -> list[Any]:
        ...
    
    def primed_sample(self, n_samples, lyric_and_music_tokens, audio_conditioning=..., metadata_conditioning=..., last_encoder_hidden_states=..., temp=..., top_k=..., top_p=..., get_preds=..., chunk_size=..., sample_tokens=...): # -> tuple[Tensor, Tensor | Any | list[Any]] | Tensor:
        ...
    


class JukeboxMusicTokenConditioner(nn.Module):
    """
    The `JukeboxMusicTokenConditioner` takes music tokens as an input (coresponding to the codes of the VQVAE's
    codebook) and upsamples it using a single layer of decoder convolution block (the same is used in the VQVAE).
    """
    def __init__(self, config, level) -> None:
        ...
    
    def forward(self, music_tokens, raw_audio_conditionning=...): # -> Any:
        """
        Args:
            music_tokens (`torch.LongTensor`):
                Music tokens form the uper level in range(nb_discrete_codes)
            raw_audio_conditionning (`torch.LongTensor`, *optional*):
                Audio used when primed sampling, raw audio information that conditions the generation
        """
        ...
    


class JukeboxRangeEmbedding(nn.Module):
    """
    The `JukeboxRangeEmbedding` interpolate the given [pos_start, pos_end] to obtain an equivalent of time positional
    embedding of length `n_ctx`.

    Binning process : For each pos in position tensor, find its bin [start,end) mapped to [0,1,...,bins-1] [start,end)
    -> [0,1) -> [0, bins) -> floor -> [0,...,bins-1] NOTE: Open ended interval on right, so start <= pos < end, not <=
    end
    """
    def __init__(self, n_time, embed_dim, range, out_width, clamp=...) -> None:
        ...
    
    def forward(self, pos_start, pos_end=...): # -> Any:
        ...
    


class JukeboxLabelConditioner(nn.Module):
    def __init__(self, config, include_time_signal) -> None:
        ...
    
    def forward(self, metadata): # -> tuple[Any, Any | None]:
        ...
    


class JukeboxPrior(PreTrainedModel):
    """
    The JukeboxPrior class, which is a wrapper around the various conditioning and the transformer. JukeboxPrior can be
    seen as language models trained on music. They model the next `music token` prediction task. If a (lyric) `encoderù
    is defined, it also models the `next character` prediction on the lyrics. Can be conditionned on timing, artist,
    genre, lyrics and codes from lower-levels Priors.

    Args:
        config (`JukeboxPriorConfig`):
            Model configuration class with all the parameters of the model. Initializing with a config file does not
            load the weights associated with the model, only the configuration. Check out the
            [`~PreTrainedModel.from_pretrained`] method to load the model weights.
        level (`int`, *optional*):
            Current level of the Prior. Should be in range `[0,nb_priors]`.
        nb_priors (`int`, *optional*, defaults to 3):
            Total number of priors.
        vqvae_encoder (`Callable`, *optional*):
            Encoding method of the VQVAE encoder used in the forward pass of the model. Passing functions instead of
            the vqvae module to avoid getting the parameters.
        vqvae_decoder (`Callable`, *optional*):
            Decoding method of the VQVAE decoder used in the forward pass of the model. Passing functions instead of
            the vqvae module to avoid getting the parameters.
    """
    config_class = JukeboxPriorConfig
    def __init__(self, config: JukeboxPriorConfig, level=..., nb_priors=..., vqvae_encoder=..., vqvae_decoder=...) -> None:
        ...
    
    def get_metadata(self, labels, start, total_length, offset, get_indices=...): # -> tuple[Tensor | Any, list[Any] | None] | Tensor:
        ...
    
    def set_metadata_lyric_tokens(self, labels): # -> tuple[Tensor, list[Any]] | tuple[Any, None]:
        """
        Processes the full labels to only retreive the relevant lyric tokens and keep the metadata conditioning tokens.
        """
        ...
    
    def get_music_tokens_conds(self, music_tokens, start, end): # -> list[Tensor | Any] | None:
        """
        Extracts current level's conditioning music tokens.
        """
        ...
    
    def prior_preprocess(self, tokens, conds): # -> tuple[Tensor, Tensor]:
        """
        Shifts the input tokens to account for the dictionary merge. The embed_dim_shift give by how much the music
        tokens should be shifted by. It is equal to `lyric_vocab_size`.
        """
        ...
    
    def prior_postprocess(self, tokens): # -> Tensor:
        """
        Shifts back the input tokens if the model uses an encoder decoder architecture. As the embedding layer is
        shared, `prior_embed_dim_shift` shifts the music token ids by `lyric_vocab_size`. Only returns the music
        tokens.
        """
        ...
    
    def embed_tokens(self, music_tokens_conds): # -> Any | None:
        """
        Embeds the upper level music tokens and upsamples them to provide as audio conditioning.
        """
        ...
    
    def encode(self, hidden_states, start_level=..., end_level=..., bs_chunks=...):
        """
        Encodes the hidden states (raw audio) using the VQVAE's encoder. Returns latent_states.
        """
        ...
    
    def decode(self, music_tokens, start_level=..., end_level=..., bs_chunks=...):
        """
        Usamples the sequence of codebook vectors to a raw audio.
        """
        ...
    
    def get_cond(self, music_tokens_conds, metadata): # -> tuple[Any | None, Any | None, Any | None]:
        """
        Converts the input tokens to input_embeddings. Splits the lyrics form the rest of the metadata. Lyric tokens
        can be None.
        """
        ...
    
    def sample(self, n_samples, music_tokens=..., music_tokens_conds=..., metadata=..., temp=..., top_k=..., top_p=..., chunk_size=..., sample_tokens=...): # -> Tensor | tuple[Tensor, Tensor | Any | list[Any]]:
        """
        Ancestral/Prime sampling a window of tokens using the provided conditioning and metadatas.

        Args:
            n_samples (`int`):
                Number of samples to generate.
            music_tokens (`List[torch.LongTensor]`, *optional*):
                Previously gemerated tokens at the current level. Used as context for the generation.
            music_tokens_conds (`List[torch.FloatTensor]`, *optional*):
                Upper-level music tokens generated by the previous prior model. Is `None` if the generation is not
                conditionned on the upper-level tokens.
            metadata (`List[torch.LongTensor]`, *optional*):
                List containing the metatdata tensor with the artist, genre and the lyric tokens.
            temp (`float`, *optional*, defaults to 1.0):
                Sampling temperature.
            top_k (`int`, *optional*, defaults to 0):
                Top k probabilities used for filtering.
            top_p (`float`, *optional*, defaults to 0.0):
                Top p probabilities used for filtering.
            chunk_size (`int`, *optional*):
                Size of the chunks used to prepare the cache of the transformer.
            sample_tokens (`int`, *optional*):
                Number of tokens to sample.

        """
        ...
    
    def get_encoder_states(self, lyric_tokens, sample=...): # -> Any | None:
        """
        Retreive the last hidden_states of the lyric encoder that will be attended to by the decoder. Forwards through
        the lyric encoder.
        """
        ...
    
    def get_encoder_loss(self, last_encoder_hidden_states, target_lyrics): # -> Any | Tensor:
        """
        Computes the loss for the lyric encoder: next lyric token prediction.
        """
        ...
    
    def forward_tokens(self, music_tokens, music_tokens_conds=..., metadata=..., get_preds=..., get_attn_weights=...): # -> list[Any] | tuple[Any, dict[str, Any]]:
        """
        Applies a forward pass using the conditioning tokens. Different from the classic forward as it does not use the
        vqvae's encoding layers.
        """
        ...
    
    def forward(self, hidden_states: torch.Tensor, metadata: Optional[List[torch.LongTensor]], decode: Optional[bool] = ..., get_preds: Optional[bool] = ...) -> List[torch.Tensor]:
        """
        Encode the hidden states using the `vqvae` encoder, and then predicts the next token in the `forward_tokens`
        function. The loss is the sum of the `encoder` loss and the `decoder` loss.

        Args:
            hidden_states (`torch.Tensor`):
                Hidden states which should be raw audio
            metadata (`List[torch.LongTensor]`, *optional*):
                List containing the metadata conditioning tensorwith the lyric and the metadata tokens.
            decode (`bool`, *optional*, defaults to `False`):
                Whether or not to decode the encoded to tokens.
            get_preds (`bool`, *optional*, defaults to `False`):
                Whether or not to return the actual predicitons of the model.
        """
        ...
    


class JukeboxPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = JukeboxConfig
    base_model_prefix = ...
    supports_gradient_checkpointing = ...
    def __init__(self, *inputs, **kwargs) -> None:
        ...
    


JUKEBOX_SAMPLING_INPUT_DOCSTRING = ...
@add_start_docstrings("""The bare JUKEBOX Model used for music generation. 4 sampling techniques are supported : `primed_sample`, `upsample`,
    `continue_sample` and `ancestral_sample`. It does not have a `forward` method as the training is not end to end. If
    you want to fine-tune the model, it is recommended to use the `JukeboxPrior` class and train each prior
    individually.
    """, JUKEBOX_START_DOCSTRING)
class JukeboxModel(JukeboxPreTrainedModel):
    _no_split_modules = ...
    def __init__(self, config) -> None:
        ...
    
    def set_shared_params(self, model_config): # -> None:
        """
        Initialises the parameters that are shared. This has to be done here because the list of `JukeboxPriorConfig`
        is nest, and is thus unreachable in the `from_dict` function
        """
        ...
    
    def decode(self, music_tokens, start_level=..., end_level=..., bs_chunks=...): # -> Tensor:
        ...
    
    def encode(self, input_audio, start_level=..., end_level=..., bs_chunks=...): # -> list[Tensor]:
        ...
    
    def split_batch(self, obj, n_samples, split_size): # -> Tuple[Tensor, ...] | list[Any]:
        ...
    
    def sample_partial_window(self, music_tokens, labels, offset, sampling_kwargs, level, tokens_to_sample, max_batch_size):
        ...
    
    def sample_single_window(self, music_tokens, labels, offset, sampling_kwargs, level, start, max_batch_size):
        ...
    
    def sample_level(self, music_tokens, labels, offset, sampling_kwargs, level, total_length, hop_length, max_batch_size):
        ...
    
    @add_start_docstrings("""
        Generates music tokens based on the provided `labels. Will start at the desired prior level and automatically
        upsample the sequence. If you want to create the audio, you should call `model.decode(tokens)`, which will use
        the VQ-VAE decoder to convert the music tokens to raw audio.

        Args:
            labels (`List[torch.LongTensor]`) :
                List of length `n_sample`, and shape `(self.levels, 4 + self.config.max_nb_genre +
                lyric_sequence_length)` metadata such as `artist_id`, `genre_id` and the full list of lyric tokens
                which are used to condition the generation.
            n_samples (`int`, *optional*, default to 1) :
                Number of samples to be generated in parallel.
        """)
    def ancestral_sample(self, labels, n_samples=..., **sampling_kwargs) -> List[torch.LongTensor]:
        """
        Example:

        ```python
        >>> from transformers import AutoTokenizer, JukeboxModel, set_seed

        >>> model = JukeboxModel.from_pretrained("openai/jukebox-1b-lyrics", min_duration=0).eval()
        >>> tokenizer = AutoTokenizer.from_pretrained("openai/jukebox-1b-lyrics")

        >>> lyrics = "Hey, are you awake? Can you talk to me?"
        >>> artist = "Zac Brown Band"
        >>> genre = "Country"
        >>> metas = tokenizer(artist=artist, genres=genre, lyrics=lyrics)
        >>> set_seed(0)
        >>> music_tokens = model.ancestral_sample(metas.input_ids, sample_length=400)

        >>> with torch.no_grad():
        ...     model.decode(music_tokens)[:, :10].squeeze(-1)
        tensor([[-0.0219, -0.0679, -0.1050, -0.1203, -0.1271, -0.0936, -0.0396, -0.0405,
            -0.0818, -0.0697]])
        ```
        """
        ...
    
    @add_start_docstrings("""Generates a continuation of the previously generated tokens.

        Args:
            music_tokens (`List[torch.LongTensor]` of length `self.levels` ) :
                A sequence of music tokens which will be used as context to continue the sampling process. Should have
                `self.levels` tensors, each corresponding to the generation at a certain level.
        """, JUKEBOX_SAMPLING_INPUT_DOCSTRING)
    def continue_sample(self, music_tokens, labels, **sampling_kwargs) -> List[torch.LongTensor]:
        ...
    
    @add_start_docstrings("""Upsamples a sequence of music tokens using the prior at level `level`.

        Args:
            music_tokens (`List[torch.LongTensor]` of length `self.levels` ) :
                A sequence of music tokens which will be used as context to continue the sampling process. Should have
                `self.levels` tensors, each corresponding to the generation at a certain level.
        """, JUKEBOX_SAMPLING_INPUT_DOCSTRING)
    def upsample(self, music_tokens, labels, **sampling_kwargs) -> List[torch.LongTensor]:
        ...
    
    @add_start_docstrings("""Generate a raw audio conditioned on the provided `raw_audio` which is used as conditioning at each of the
        generation levels. The audio is encoded to music tokens using the 3 levels of the VQ-VAE. These tokens are
        used: as conditioning for each level, which means that no ancestral sampling is required.

        Args:
            raw_audio (`List[torch.Tensor]` of length `n_samples` ) :
                A list of raw audio that will be used as conditioning information for each samples that will be
                generated.
        """, JUKEBOX_SAMPLING_INPUT_DOCSTRING)
    def primed_sample(self, raw_audio, labels, **sampling_kwargs) -> List[torch.LongTensor]:
        ...
    


