"""
This type stub file was generated by pyright.
"""

import torch
from typing import List, Optional, Tuple, Union
from torch import nn
from ...modeling_outputs import BaseModelOutput, BaseModelOutputWithPastAndCrossAttentions, SampleTSPredictionOutput, Seq2SeqTSModelOutput
from ...modeling_utils import PreTrainedModel
from ...utils import add_start_docstrings, add_start_docstrings_to_model_forward, replace_return_docstrings
from .configuration_time_series_transformer import TimeSeriesTransformerConfig

"""PyTorch Time Series Transformer model."""
logger = ...
_CONFIG_FOR_DOC = ...
class TimeSeriesFeatureEmbedder(nn.Module):
    """
    Embed a sequence of categorical features.

    Args:
        cardinalities (`list[int]`):
            List of cardinalities of the categorical features.
        embedding_dims (`list[int]`):
            List of embedding dimensions of the categorical features.
    """
    def __init__(self, cardinalities: List[int], embedding_dims: List[int]) -> None:
        ...
    
    def forward(self, features: torch.Tensor) -> torch.Tensor:
        ...
    


class TimeSeriesStdScaler(nn.Module):
    """
    Standardize features by calculating the mean and scaling along the first dimension, and then normalizes it by
    subtracting from the mean and dividing by the standard deviation.
    """
    def __init__(self, config: TimeSeriesTransformerConfig) -> None:
        ...
    
    def forward(self, data: torch.Tensor, observed_indicator: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """
        Parameters:
            data (`torch.Tensor` of shape `(batch_size, sequence_length, num_input_channels)`):
                input for Batch norm calculation
            observed_indicator (`torch.BoolTensor` of shape `(batch_size, sequence_length, num_input_channels)`):
                Calculating the scale on the observed indicator.
        Returns:
            tuple of `torch.Tensor` of shapes
                (`(batch_size, sequence_length, num_input_channels)`,`(batch_size, 1, num_input_channels)`,
                `(batch_size, 1, num_input_channels)`)
        """
        ...
    


class TimeSeriesMeanScaler(nn.Module):
    """
    Computes a scaling factor as the weighted average absolute value along the first dimension, and scales the data
    accordingly.
    """
    def __init__(self, config: TimeSeriesTransformerConfig) -> None:
        ...
    
    def forward(self, data: torch.Tensor, observed_indicator: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """
        Parameters:
            data (`torch.Tensor` of shape `(batch_size, sequence_length, num_input_channels)`):
                input for Batch norm calculation
            observed_indicator (`torch.BoolTensor` of shape `(batch_size, sequence_length, num_input_channels)`):
                Calculating the scale on the observed indicator.
        Returns:
            tuple of `torch.Tensor` of shapes
                (`(batch_size, sequence_length, num_input_channels)`,`(batch_size, 1, num_input_channels)`,
                `(batch_size, 1, num_input_channels)`)
        """
        ...
    


class TimeSeriesNOPScaler(nn.Module):
    """
    Assigns a scaling factor equal to 1 along the first dimension, and therefore applies no scaling to the input data.
    """
    def __init__(self, config: TimeSeriesTransformerConfig) -> None:
        ...
    
    def forward(self, data: torch.Tensor, observed_indicator: torch.Tensor = ...) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """
        Parameters:
            data (`torch.Tensor` of shape `(batch_size, sequence_length, num_input_channels)`):
                input for Batch norm calculation
        Returns:
            tuple of `torch.Tensor` of shapes
                (`(batch_size, sequence_length, num_input_channels)`,`(batch_size, 1, num_input_channels)`,
                `(batch_size, 1, num_input_channels)`)
        """
        ...
    


def nll(input: torch.distributions.Distribution, target: torch.Tensor) -> torch.Tensor:
    """
    Computes the negative log likelihood loss from input distribution with respect to target.
    """
    ...

def weighted_average(input_tensor: torch.Tensor, weights: Optional[torch.Tensor] = ..., dim=...) -> torch.Tensor:
    """
    Computes the weighted average of a given tensor across a given `dim`, masking values associated with weight zero,
    meaning instead of `nan * 0 = nan` you will get `0 * 0 = 0`.

    Args:
        input_tensor (`torch.FloatTensor`):
            Input tensor, of which the average must be computed.
        weights (`torch.FloatTensor`, *optional*):
            Weights tensor, of the same shape as `input_tensor`.
        dim (`int`, *optional*):
            The dim along which to average `input_tensor`.

    Returns:
        `torch.FloatTensor`: The tensor with values averaged along the specified `dim`.
    """
    ...

class TimeSeriesSinusoidalPositionalEmbedding(nn.Embedding):
    """This module produces sinusoidal positional embeddings of any length."""
    def __init__(self, num_positions: int, embedding_dim: int, padding_idx: Optional[int] = ...) -> None:
        ...
    
    @torch.no_grad()
    def forward(self, input_ids_shape: torch.Size, past_key_values_length: int = ...) -> torch.Tensor:
        """`input_ids_shape` is expected to be [bsz x seqlen]."""
        ...
    


class TimeSeriesValueEmbedding(nn.Module):
    def __init__(self, feature_size, d_model) -> None:
        ...
    
    def forward(self, x): # -> Any:
        ...
    


class TimeSeriesTransformerAttention(nn.Module):
    """Multi-headed attention from 'Attention Is All You Need' paper"""
    def __init__(self, embed_dim: int, num_heads: int, dropout: float = ..., is_decoder: bool = ..., bias: bool = ..., is_causal: bool = ..., config: Optional[TimeSeriesTransformerConfig] = ...) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor, key_value_states: Optional[torch.Tensor] = ..., past_key_value: Optional[Tuple[torch.Tensor]] = ..., attention_mask: Optional[torch.Tensor] = ..., layer_head_mask: Optional[torch.Tensor] = ..., output_attentions: bool = ...) -> Tuple[torch.Tensor, Optional[torch.Tensor], Optional[Tuple[torch.Tensor]]]:
        """Input shape: Batch x Time x Channel"""
        ...
    


class TimeSeriesTransformerEncoderLayer(nn.Module):
    def __init__(self, config: TimeSeriesTransformerConfig) -> None:
        ...
    
    def forward(self, hidden_states: torch.FloatTensor, attention_mask: torch.FloatTensor, layer_head_mask: torch.FloatTensor, output_attentions: Optional[bool] = ...) -> Tuple[torch.FloatTensor, Optional[torch.FloatTensor]]:
        """
        Args:
            hidden_states (`torch.FloatTensor`): input to the layer of shape `(batch, seq_len, embed_dim)`
            attention_mask (`torch.FloatTensor`): attention mask of size
                `(batch, 1, tgt_len, src_len)` where padding elements are indicated by very large negative values.
            layer_head_mask (`torch.FloatTensor`): mask for attention heads in a given layer of size
                `(encoder_attention_heads,)`.
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
        """
        ...
    


TIME_SERIES_TRANSFORMER_ATTENTION_CLASSES = ...
class TimeSeriesTransformerDecoderLayer(nn.Module):
    def __init__(self, config: TimeSeriesTransformerConfig) -> None:
        ...
    
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = ..., encoder_hidden_states: Optional[torch.Tensor] = ..., encoder_attention_mask: Optional[torch.Tensor] = ..., layer_head_mask: Optional[torch.Tensor] = ..., cross_attn_layer_head_mask: Optional[torch.Tensor] = ..., past_key_value: Optional[Tuple[torch.Tensor]] = ..., output_attentions: Optional[bool] = ..., use_cache: Optional[bool] = ...) -> Tuple[torch.FloatTensor, Optional[Tuple[torch.FloatTensor, torch.FloatTensor]]]:
        """
        Args:
            hidden_states (`torch.FloatTensor`): input to the layer of shape `(batch, seq_len, embed_dim)`
            attention_mask (`torch.FloatTensor`): attention mask of size
                `(batch, 1, tgt_len, src_len)` where padding elements are indicated by very large negative values.
            encoder_hidden_states (`torch.FloatTensor`):
                cross attention input to the layer of shape `(batch, seq_len, embed_dim)`
            encoder_attention_mask (`torch.FloatTensor`): encoder attention mask of size
                `(batch, 1, tgt_len, src_len)` where padding elements are indicated by very large negative values.
            layer_head_mask (`torch.FloatTensor`): mask for attention heads in a given layer of size
                `(encoder_attention_heads,)`.
            cross_attn_layer_head_mask (`torch.FloatTensor`): mask for cross-attention heads in a given layer of
                size `(decoder_attention_heads,)`.
            past_key_value (`Tuple(torch.FloatTensor)`): cached past key and value projection states
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
        """
        ...
    


class TimeSeriesTransformerPreTrainedModel(PreTrainedModel):
    config_class = TimeSeriesTransformerConfig
    base_model_prefix = ...
    main_input_name = ...
    supports_gradient_checkpointing = ...


TIME_SERIES_TRANSFORMER_START_DOCSTRING = ...
TIME_SERIES_TRANSFORMER_INPUTS_DOCSTRING = ...
class TimeSeriesTransformerEncoder(TimeSeriesTransformerPreTrainedModel):
    """
    Transformer encoder consisting of *config.encoder_layers* self attention layers. Each layer is a
    [`TimeSeriesTransformerEncoderLayer`].

    Args:
        config: TimeSeriesTransformerConfig
    """
    def __init__(self, config: TimeSeriesTransformerConfig) -> None:
        ...
    
    def forward(self, attention_mask: Optional[torch.Tensor] = ..., head_mask: Optional[torch.Tensor] = ..., inputs_embeds: Optional[torch.FloatTensor] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple, BaseModelOutput]:
        r"""
        Args:
            attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.

                [What are attention masks?](../glossary#attention-mask)
            head_mask (`torch.Tensor` of shape `(encoder_layers, encoder_attention_heads)`, *optional*):
                Mask to nullify selected heads of the attention modules. Mask values selected in `[0, 1]`:

                - 1 indicates the head is **not masked**,
                - 0 indicates the head is **masked**.

            inputs_embeds (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
                Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation.
                This is useful if you want more control over how to convert `input_ids` indices into associated vectors
                than the model's internal embedding lookup matrix.
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
            output_hidden_states (`bool`, *optional*):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more detail.
            return_dict (`bool`, *optional*):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
        """
        ...
    


class TimeSeriesTransformerDecoder(TimeSeriesTransformerPreTrainedModel):
    """
    Transformer decoder consisting of *config.decoder_layers* layers. Each layer is a
    [`TimeSeriesTransformerDecoderLayer`]

    Args:
        config: TimeSeriesTransformerConfig
    """
    def __init__(self, config: TimeSeriesTransformerConfig) -> None:
        ...
    
    def forward(self, attention_mask: Optional[torch.Tensor] = ..., encoder_hidden_states: Optional[torch.FloatTensor] = ..., encoder_attention_mask: Optional[torch.LongTensor] = ..., head_mask: Optional[torch.Tensor] = ..., cross_attn_head_mask: Optional[torch.Tensor] = ..., past_key_values: Optional[List[torch.FloatTensor]] = ..., inputs_embeds: Optional[torch.FloatTensor] = ..., use_cache: Optional[bool] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Tuple, BaseModelOutputWithPastAndCrossAttentions]:
        r"""
        Args:
            attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.

                [What are attention masks?](../glossary#attention-mask)
            encoder_hidden_states (`torch.FloatTensor` of shape `(batch_size, encoder_sequence_length, hidden_size)`, *optional*):
                Sequence of hidden-states at the output of the last layer of the encoder. Used in the cross-attention
                of the decoder.
            encoder_attention_mask (`torch.LongTensor` of shape `(batch_size, encoder_sequence_length)`, *optional*):
                Mask to avoid performing cross-attention on padding tokens indices of encoder input_ids. Mask values
                selected in `[0, 1]`:

                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.

                [What are attention masks?](../glossary#attention-mask)
            head_mask (`torch.Tensor` of shape `(decoder_layers, decoder_attention_heads)`, *optional*):
                Mask to nullify selected heads of the attention modules. Mask values selected in `[0, 1]`:

                - 1 indicates the head is **not masked**,
                - 0 indicates the head is **masked**.

            cross_attn_head_mask (`torch.Tensor` of shape `(decoder_layers, decoder_attention_heads)`, *optional*):
                Mask to nullify selected heads of the cross-attention modules in the decoder to avoid performing
                cross-attention on hidden heads. Mask values selected in `[0, 1]`:

                - 1 indicates the head is **not masked**,
                - 0 indicates the head is **masked**.

            past_key_values (`tuple(tuple(torch.FloatTensor))`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
                Tuple of `tuple(torch.FloatTensor)` of length `config.n_layers`, with each tuple having 2 tensors of
                shape `(batch_size, num_heads, sequence_length, embed_size_per_head)`) and 2 additional tensors of
                shape `(batch_size, num_heads, encoder_sequence_length, embed_size_per_head)`.

                Contains pre-computed hidden-states (key and values in the self-attention blocks and in the
                cross-attention blocks) that can be used (see `past_key_values` input) to speed up sequential decoding.

                If `past_key_values` are used, the user can optionally input only the last `decoder_input_ids` (those
                that don't have their past key value states given to this model) of shape `(batch_size, 1)` instead of
                all `decoder_input_ids` of shape `(batch_size, sequence_length)`.
            inputs_embeds (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
                Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation.
                This is useful if you want more control over how to convert `input_ids` indices into associated vectors
                than the model's internal embedding lookup matrix.
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
            output_hidden_states (`bool`, *optional*):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more detail.
            return_dict (`bool`, *optional*):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
        """
        ...
    


@add_start_docstrings("The bare Time Series Transformer Model outputting raw hidden-states without any specific head on top.", TIME_SERIES_TRANSFORMER_START_DOCSTRING)
class TimeSeriesTransformerModel(TimeSeriesTransformerPreTrainedModel):
    def __init__(self, config: TimeSeriesTransformerConfig) -> None:
        ...
    
    def get_lagged_subsequences(self, sequence: torch.Tensor, subsequences_length: int, shift: int = ...) -> torch.Tensor:
        """
        Returns lagged subsequences of a given sequence. Returns a tensor of shape (N, S, C, I),
            where S = subsequences_length and I = len(indices), containing lagged subsequences. Specifically, lagged[i,
            j, :, k] = sequence[i, -indices[k]-S+j, :].

        Args:
            sequence: Tensor
                The sequence from which lagged subsequences should be extracted. Shape: (N, T, C).
            subsequences_length : int
                Length of the subsequences to be extracted.
            shift: int
                Shift the lags by this amount back.
        """
        ...
    
    def create_network_inputs(self, past_values: torch.Tensor, past_time_features: torch.Tensor, static_categorical_features: Optional[torch.Tensor] = ..., static_real_features: Optional[torch.Tensor] = ..., past_observed_mask: Optional[torch.Tensor] = ..., future_values: Optional[torch.Tensor] = ..., future_time_features: Optional[torch.Tensor] = ...): # -> tuple[Tensor, Any, Any, Tensor]:
        ...
    
    def get_encoder(self): # -> TimeSeriesTransformerEncoder:
        ...
    
    def get_decoder(self): # -> TimeSeriesTransformerDecoder:
        ...
    
    @add_start_docstrings_to_model_forward(TIME_SERIES_TRANSFORMER_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=Seq2SeqTSModelOutput, config_class=_CONFIG_FOR_DOC)
    def forward(self, past_values: torch.Tensor, past_time_features: torch.Tensor, past_observed_mask: torch.Tensor, static_categorical_features: Optional[torch.Tensor] = ..., static_real_features: Optional[torch.Tensor] = ..., future_values: Optional[torch.Tensor] = ..., future_time_features: Optional[torch.Tensor] = ..., decoder_attention_mask: Optional[torch.LongTensor] = ..., head_mask: Optional[torch.Tensor] = ..., decoder_head_mask: Optional[torch.Tensor] = ..., cross_attn_head_mask: Optional[torch.Tensor] = ..., encoder_outputs: Optional[List[torch.FloatTensor]] = ..., past_key_values: Optional[List[torch.FloatTensor]] = ..., output_hidden_states: Optional[bool] = ..., output_attentions: Optional[bool] = ..., use_cache: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Seq2SeqTSModelOutput, Tuple]:
        r"""
        Returns:

        Examples:

        ```python
        >>> from huggingface_hub import hf_hub_download
        >>> import torch
        >>> from transformers import TimeSeriesTransformerModel

        >>> file = hf_hub_download(
        ...     repo_id="hf-internal-testing/tourism-monthly-batch", filename="train-batch.pt", repo_type="dataset"
        ... )
        >>> batch = torch.load(file)

        >>> model = TimeSeriesTransformerModel.from_pretrained("huggingface/time-series-transformer-tourism-monthly")

        >>> # during training, one provides both past and future values
        >>> # as well as possible additional features
        >>> outputs = model(
        ...     past_values=batch["past_values"],
        ...     past_time_features=batch["past_time_features"],
        ...     past_observed_mask=batch["past_observed_mask"],
        ...     static_categorical_features=batch["static_categorical_features"],
        ...     static_real_features=batch["static_real_features"],
        ...     future_values=batch["future_values"],
        ...     future_time_features=batch["future_time_features"],
        ... )

        >>> last_hidden_state = outputs.last_hidden_state
        ```"""
        ...
    


@add_start_docstrings("The Time Series Transformer Model with a distribution head on top for time-series forecasting.", TIME_SERIES_TRANSFORMER_START_DOCSTRING)
class TimeSeriesTransformerForPrediction(TimeSeriesTransformerPreTrainedModel):
    def __init__(self, config: TimeSeriesTransformerConfig) -> None:
        ...
    
    def output_params(self, dec_output): # -> Any:
        ...
    
    def get_encoder(self): # -> TimeSeriesTransformerEncoder:
        ...
    
    def get_decoder(self): # -> TimeSeriesTransformerDecoder:
        ...
    
    @torch.jit.ignore
    def output_distribution(self, params, loc=..., scale=..., trailing_n=...) -> torch.distributions.Distribution:
        ...
    
    @add_start_docstrings_to_model_forward(TIME_SERIES_TRANSFORMER_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=Seq2SeqTSModelOutput, config_class=_CONFIG_FOR_DOC)
    def forward(self, past_values: torch.Tensor, past_time_features: torch.Tensor, past_observed_mask: torch.Tensor, static_categorical_features: Optional[torch.Tensor] = ..., static_real_features: Optional[torch.Tensor] = ..., future_values: Optional[torch.Tensor] = ..., future_time_features: Optional[torch.Tensor] = ..., future_observed_mask: Optional[torch.Tensor] = ..., decoder_attention_mask: Optional[torch.LongTensor] = ..., head_mask: Optional[torch.Tensor] = ..., decoder_head_mask: Optional[torch.Tensor] = ..., cross_attn_head_mask: Optional[torch.Tensor] = ..., encoder_outputs: Optional[List[torch.FloatTensor]] = ..., past_key_values: Optional[List[torch.FloatTensor]] = ..., output_hidden_states: Optional[bool] = ..., output_attentions: Optional[bool] = ..., use_cache: Optional[bool] = ..., return_dict: Optional[bool] = ...) -> Union[Seq2SeqTSModelOutput, Tuple]:
        r"""
        Returns:

        Examples:

        ```python
        >>> from huggingface_hub import hf_hub_download
        >>> import torch
        >>> from transformers import TimeSeriesTransformerForPrediction

        >>> file = hf_hub_download(
        ...     repo_id="hf-internal-testing/tourism-monthly-batch", filename="train-batch.pt", repo_type="dataset"
        ... )
        >>> batch = torch.load(file)

        >>> model = TimeSeriesTransformerForPrediction.from_pretrained(
        ...     "huggingface/time-series-transformer-tourism-monthly"
        ... )

        >>> # during training, one provides both past and future values
        >>> # as well as possible additional features
        >>> outputs = model(
        ...     past_values=batch["past_values"],
        ...     past_time_features=batch["past_time_features"],
        ...     past_observed_mask=batch["past_observed_mask"],
        ...     static_categorical_features=batch["static_categorical_features"],
        ...     static_real_features=batch["static_real_features"],
        ...     future_values=batch["future_values"],
        ...     future_time_features=batch["future_time_features"],
        ... )

        >>> loss = outputs.loss
        >>> loss.backward()

        >>> # during inference, one only provides past values
        >>> # as well as possible additional features
        >>> # the model autoregressively generates future values
        >>> outputs = model.generate(
        ...     past_values=batch["past_values"],
        ...     past_time_features=batch["past_time_features"],
        ...     past_observed_mask=batch["past_observed_mask"],
        ...     static_categorical_features=batch["static_categorical_features"],
        ...     static_real_features=batch["static_real_features"],
        ...     future_time_features=batch["future_time_features"],
        ... )

        >>> mean_prediction = outputs.sequences.mean(dim=1)
        ```"""
        ...
    
    @torch.no_grad()
    def generate(self, past_values: torch.Tensor, past_time_features: torch.Tensor, future_time_features: torch.Tensor, past_observed_mask: Optional[torch.Tensor] = ..., static_categorical_features: Optional[torch.Tensor] = ..., static_real_features: Optional[torch.Tensor] = ..., output_attentions: Optional[bool] = ..., output_hidden_states: Optional[bool] = ...) -> SampleTSPredictionOutput:
        r"""
        Greedily generate sequences of sample predictions from a model with a probability distribution head.

        Parameters:
            past_values (`torch.FloatTensor` of shape `(batch_size, sequence_length)` or `(batch_size, sequence_length, input_size)`):
                Past values of the time series, that serve as context in order to predict the future. The sequence size
                of this tensor must be larger than the `context_length` of the model, since the model will use the
                larger size to construct lag features, i.e. additional values from the past which are added in order to
                serve as "extra context".

                The `sequence_length` here is equal to `config.context_length` + `max(config.lags_sequence)`, which if
                no `lags_sequence` is configured, is equal to `config.context_length` + 7 (as by default, the largest
                look-back index in `config.lags_sequence` is 7). The property `_past_length` returns the actual length
                of the past.

                The `past_values` is what the Transformer encoder gets as input (with optional additional features,
                such as `static_categorical_features`, `static_real_features`, `past_time_features` and lags).

                Optionally, missing values need to be replaced with zeros and indicated via the `past_observed_mask`.

                For multivariate time series, the `input_size` > 1 dimension is required and corresponds to the number
                of variates in the time series per time step.
            past_time_features (`torch.FloatTensor` of shape `(batch_size, sequence_length, num_features)`):
                Required time features, which the model internally will add to `past_values`. These could be things
                like "month of year", "day of the month", etc. encoded as vectors (for instance as Fourier features).
                These could also be so-called "age" features, which basically help the model know "at which point in
                life" a time-series is. Age features have small values for distant past time steps and increase
                monotonically the more we approach the current time step. Holiday features are also a good example of
                time features.

                These features serve as the "positional encodings" of the inputs. So contrary to a model like BERT,
                where the position encodings are learned from scratch internally as parameters of the model, the Time
                Series Transformer requires to provide additional time features. The Time Series Transformer only
                learns additional embeddings for `static_categorical_features`.

                Additional dynamic real covariates can be concatenated to this tensor, with the caveat that these
                features must but known at prediction time.

                The `num_features` here is equal to `config.`num_time_features` + `config.num_dynamic_real_features`.
            future_time_features (`torch.FloatTensor` of shape `(batch_size, prediction_length, num_features)`):
                Required time features for the prediction window, which the model internally will add to sampled
                predictions. These could be things like "month of year", "day of the month", etc. encoded as vectors
                (for instance as Fourier features). These could also be so-called "age" features, which basically help
                the model know "at which point in life" a time-series is. Age features have small values for distant
                past time steps and increase monotonically the more we approach the current time step. Holiday features
                are also a good example of time features.

                These features serve as the "positional encodings" of the inputs. So contrary to a model like BERT,
                where the position encodings are learned from scratch internally as parameters of the model, the Time
                Series Transformer requires to provide additional time features. The Time Series Transformer only
                learns additional embeddings for `static_categorical_features`.

                Additional dynamic real covariates can be concatenated to this tensor, with the caveat that these
                features must but known at prediction time.

                The `num_features` here is equal to `config.`num_time_features` + `config.num_dynamic_real_features`.
            past_observed_mask (`torch.BoolTensor` of shape `(batch_size, sequence_length)` or `(batch_size, sequence_length, input_size)`, *optional*):
                Boolean mask to indicate which `past_values` were observed and which were missing. Mask values selected
                in `[0, 1]`:

                - 1 for values that are **observed**,
                - 0 for values that are **missing** (i.e. NaNs that were replaced by zeros).

            static_categorical_features (`torch.LongTensor` of shape `(batch_size, number of static categorical features)`, *optional*):
                Optional static categorical features for which the model will learn an embedding, which it will add to
                the values of the time series.

                Static categorical features are features which have the same value for all time steps (static over
                time).

                A typical example of a static categorical feature is a time series ID.
            static_real_features (`torch.FloatTensor` of shape `(batch_size, number of static real features)`, *optional*):
                Optional static real features which the model will add to the values of the time series.

                Static real features are features which have the same value for all time steps (static over time).

                A typical example of a static real feature is promotion information.
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers.
            output_hidden_states (`bool`, *optional*):
                Whether or not to return the hidden states of all layers.

        Return:
            [`SampleTSPredictionOutput`] where the outputs `sequences` tensor will have shape `(batch_size, number of
            samples, prediction_length)` or `(batch_size, number of samples, prediction_length, input_size)` for
            multivariate predictions.
        """
        ...
    

