"""
This type stub file was generated by pyright.
"""

import torch
from typing import Any, Dict, List, Optional, Union
from ..utils import is_accelerate_available, is_torch_available

if is_torch_available():
    ...
if is_accelerate_available():
    ...
MIN_PEFT_VERSION = ...
logger = ...
class PeftAdapterMixin:
    """
    A class containing all functions for loading and using adapters weights that are supported in PEFT library. For
    more details about adapters and injecting them on a transformer-based model, check out the documentation of PEFT
    library: https://huggingface.co/docs/peft/index

    Currently supported PEFT methods are all non-prefix tuning methods. Below is the list of supported PEFT methods
    that anyone can load, train and run with this mixin class:
    - Low Rank Adapters (LoRA): https://huggingface.co/docs/peft/conceptual_guides/lora
    - IA3: https://huggingface.co/docs/peft/conceptual_guides/ia3
    - AdaLora: https://arxiv.org/abs/2303.10512

    Other PEFT models such as prompt tuning, prompt learning are out of scope as these adapters are not "injectable"
    into a torch module. For using these methods, please refer to the usage guide of PEFT library.

    With this mixin, if the correct PEFT version is installed, it is possible to:

    - Load an adapter stored on a local path or in a remote Hub repository, and inject it in the model
    - Attach new adapters in the model and train them with Trainer or by your own.
    - Attach multiple adapters and iteratively activate / deactivate them
    - Activate / deactivate all adapters from the model.
    - Get the `state_dict` of the active adapter.
    """
    _hf_peft_config_loaded = ...
    def load_adapter(self, peft_model_id: Optional[str] = ..., adapter_name: Optional[str] = ..., revision: Optional[str] = ..., token: Optional[str] = ..., device_map: Optional[str] = ..., max_memory: Optional[str] = ..., offload_folder: Optional[str] = ..., offload_index: Optional[int] = ..., peft_config: Dict[str, Any] = ..., adapter_state_dict: Optional[Dict[str, torch.Tensor]] = ..., low_cpu_mem_usage: bool = ..., adapter_kwargs: Optional[Dict[str, Any]] = ...) -> None:
        """
        Load adapter weights from file or remote Hub folder. If you are not familiar with adapters and PEFT methods, we
        invite you to read more about them on PEFT official documentation: https://huggingface.co/docs/peft

        Requires peft as a backend to load the adapter weights.

        Args:
            peft_model_id (`str`, *optional*):
                The identifier of the model to look for on the Hub, or a local path to the saved adapter config file
                and adapter weights.
            adapter_name (`str`, *optional*):
                The adapter name to use. If not set, will use the default adapter.
            revision (`str`, *optional*, defaults to `"main"`):
                The specific model version to use. It can be a branch name, a tag name, or a commit id, since we use a
                git-based system for storing models and other artifacts on huggingface.co, so `revision` can be any
                identifier allowed by git.

                <Tip>

                To test a pull request you made on the Hub, you can pass `revision="refs/pr/<pr_number>"`.

                </Tip>

            token (`str`, `optional`):
                Whether to use authentication token to load the remote folder. Userful to load private repositories
                that are on HuggingFace Hub. You might need to call `huggingface-cli login` and paste your tokens to
                cache it.
            device_map (`str` or `Dict[str, Union[int, str, torch.device]]` or `int` or `torch.device`, *optional*):
                A map that specifies where each submodule should go. It doesn't need to be refined to each
                parameter/buffer name, once a given module name is inside, every submodule of it will be sent to the
                same device. If we only pass the device (*e.g.*, `"cpu"`, `"cuda:1"`, `"mps"`, or a GPU ordinal rank
                like `1`) on which the model will be allocated, the device map will map the entire model to this
                device. Passing `device_map = 0` means put the whole model on GPU 0.

                To have Accelerate compute the most optimized `device_map` automatically, set `device_map="auto"`. For
                more information about each option see [designing a device
                map](https://hf.co/docs/accelerate/main/en/usage_guides/big_modeling#designing-a-device-map).
            max_memory (`Dict`, *optional*):
                A dictionary device identifier to maximum memory. Will default to the maximum memory available for each
                GPU and the available CPU RAM if unset.
            offload_folder (`str` or `os.PathLike`, `optional`):
                If the `device_map` contains any value `"disk"`, the folder where we will offload weights.
            offload_index (`int`, `optional`):
                `offload_index` argument to be passed to `accelerate.dispatch_model` method.
            peft_config (`Dict[str, Any]`, *optional*):
                The configuration of the adapter to add, supported adapters are non-prefix tuning and adaption prompts
                methods. This argument is used in case users directly pass PEFT state dicts
            adapter_state_dict (`Dict[str, torch.Tensor]`, *optional*):
                The state dict of the adapter to load. This argument is used in case users directly pass PEFT state
                dicts
            low_cpu_mem_usage (`bool`, *optional*, defaults to `False`):
                Reduce memory usage while loading the PEFT adapter. This should also speed up the loading process.
                Requires PEFT version 0.13.0 or higher.
            adapter_kwargs (`Dict[str, Any]`, *optional*):
                Additional keyword arguments passed along to the `from_pretrained` method of the adapter config and
                `find_adapter_config_file` method.
        """
        ...
    
    def add_adapter(self, adapter_config, adapter_name: Optional[str] = ...) -> None:
        r"""
        If you are not familiar with adapters and PEFT methods, we invite you to read more about them on the PEFT
        official documentation: https://huggingface.co/docs/peft

        Adds a fresh new adapter to the current model for training purpose. If no adapter name is passed, a default
        name is assigned to the adapter to follow the convention of PEFT library (in PEFT we use "default" as the
        default adapter name).

        Args:
            adapter_config (`~peft.PeftConfig`):
                The configuration of the adapter to add, supported adapters are non-prefix tuning and adaption prompts
                methods
            adapter_name (`str`, *optional*, defaults to `"default"`):
                The name of the adapter to add. If no name is passed, a default name is assigned to the adapter.
        """
        ...
    
    def set_adapter(self, adapter_name: Union[List[str], str]) -> None:
        """
        If you are not familiar with adapters and PEFT methods, we invite you to read more about them on the PEFT
        official documentation: https://huggingface.co/docs/peft

        Sets a specific adapter by forcing the model to use a that adapter and disable the other adapters.

        Args:
            adapter_name (`Union[List[str], str]`):
                The name of the adapter to set. Can be also a list of strings to set multiple adapters.
        """
        ...
    
    def disable_adapters(self) -> None:
        r"""
        If you are not familiar with adapters and PEFT methods, we invite you to read more about them on the PEFT
        official documentation: https://huggingface.co/docs/peft

        Disable all adapters that are attached to the model. This leads to inferring with the base model only.
        """
        ...
    
    def enable_adapters(self) -> None:
        """
        If you are not familiar with adapters and PEFT methods, we invite you to read more about them on the PEFT
        official documentation: https://huggingface.co/docs/peft

        Enable adapters that are attached to the model. The model will use `self.active_adapter()`
        """
        ...
    
    def active_adapters(self) -> List[str]:
        """
        If you are not familiar with adapters and PEFT methods, we invite you to read more about them on the PEFT
        official documentation: https://huggingface.co/docs/peft

        Gets the current active adapters of the model. In case of multi-adapter inference (combining multiple adapters
        for inference) returns the list of all active adapters so that users can deal with them accordingly.

        For previous PEFT versions (that does not support multi-adapter inference), `module.active_adapter` will return
        a single string.
        """
        ...
    
    def active_adapter(self) -> str:
        ...
    
    def get_adapter_state_dict(self, adapter_name: Optional[str] = ...) -> dict:
        """
        If you are not familiar with adapters and PEFT methods, we invite you to read more about them on the PEFT
        official documentation: https://huggingface.co/docs/peft

        Gets the adapter state dict that should only contain the weights tensors of the specified adapter_name adapter.
        If no adapter_name is passed, the active adapter is used.

        Args:
            adapter_name (`str`, *optional*):
                The name of the adapter to get the state dict from. If no name is passed, the active adapter is used.
        """
        ...
    

