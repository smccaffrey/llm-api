"""
This type stub file was generated by pyright.
"""

from typing import List, Union
from ...image_utils import ImageInput
from ...processing_utils import ProcessingKwargs, ProcessorMixin, Unpack
from ...tokenization_utils_base import BatchEncoding, PreTokenizedInput, TextInput

"""
Image/Text processor class for ALIGN
"""
class AlignProcessorKwargs(ProcessingKwargs, total=False):
    _defaults = ...


class AlignProcessor(ProcessorMixin):
    r"""
    Constructs an ALIGN processor which wraps [`EfficientNetImageProcessor`] and
    [`BertTokenizer`]/[`BertTokenizerFast`] into a single processor that interits both the image processor and
    tokenizer functionalities. See the [`~AlignProcessor.__call__`] and [`~OwlViTProcessor.decode`] for more
    information.
    The preferred way of passing kwargs is as a dictionary per modality, see usage example below.
        ```python
        from transformers import AlignProcessor
        from PIL import Image
        model_id = "kakaobrain/align-base"
        processor = AlignProcessor.from_pretrained(model_id)

        processor(
            images=your_pil_image,
            text=["What is that?"],
            images_kwargs = {"crop_size": {"height": 224, "width": 224}},
            text_kwargs = {"padding": "do_not_pad"},
            common_kwargs = {"return_tensors": "pt"},
        )
        ```

    Args:
        image_processor ([`EfficientNetImageProcessor`]):
            The image processor is a required input.
        tokenizer ([`BertTokenizer`, `BertTokenizerFast`]):
            The tokenizer is a required input.

    """
    attributes = ...
    image_processor_class = ...
    tokenizer_class = ...
    def __init__(self, image_processor, tokenizer) -> None:
        ...
    
    def __call__(self, images: ImageInput = ..., text: Union[TextInput, PreTokenizedInput, List[TextInput], List[PreTokenizedInput]] = ..., audio=..., videos=..., **kwargs: Unpack[AlignProcessorKwargs]) -> BatchEncoding:
        """
        Main method to prepare text(s) and image(s) to be fed as input to the model. This method forwards the `text`
        arguments to BertTokenizerFast's [`~BertTokenizerFast.__call__`] if `text` is not `None` to encode
        the text. To prepare the image(s), this method forwards the `images` arguments to
        EfficientNetImageProcessor's [`~EfficientNetImageProcessor.__call__`] if `images` is not `None`. Please refer
        to the doctsring of the above two methods for more information.

        Args:
            images (`PIL.Image.Image`, `np.ndarray`, `torch.Tensor`, `List[PIL.Image.Image]`, `List[np.ndarray]`, `List[torch.Tensor]`):
                The image or batch of images to be prepared. Each image can be a PIL image, NumPy array or PyTorch
                tensor. Both channels-first and channels-last formats are supported.
            text (`str`, `List[str]`):
                The sequence or batch of sequences to be encoded. Each sequence can be a string or a list of strings
                (pretokenized string). If the sequences are provided as list of strings (pretokenized), you must set
                `is_split_into_words=True` (to lift the ambiguity with a batch of sequences).
            return_tensors (`str` or [`~utils.TensorType`], *optional*):
                If set, will return tensors of a particular framework. Acceptable values are:
                    - `'tf'`: Return TensorFlow `tf.constant` objects.
                    - `'pt'`: Return PyTorch `torch.Tensor` objects.
                    - `'np'`: Return NumPy `np.ndarray` objects.
                    - `'jax'`: Return JAX `jnp.ndarray` objects.
        Returns:
            [`BatchEncoding`]: A [`BatchEncoding`] with the following fields:

            - **input_ids** -- List of token ids to be fed to a model. Returned when `text` is not `None`.
            - **attention_mask** -- List of indices specifying which tokens should be attended to by the model (when
              `return_attention_mask=True` or if *"attention_mask"* is in `self.model_input_names` and if `text` is not
              `None`).
            - **pixel_values** -- Pixel values to be fed to a model. Returned when `images` is not `None`.
        """
        ...
    
    def batch_decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to BertTokenizerFast's [`~PreTrainedTokenizer.batch_decode`]. Please
        refer to the docstring of this method for more information.
        """
        ...
    
    def decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to BertTokenizerFast's [`~PreTrainedTokenizer.decode`]. Please refer to
        the docstring of this method for more information.
        """
        ...
    
    @property
    def model_input_names(self): # -> list[Any]:
        ...
    


__all__ = ["AlignProcessor"]