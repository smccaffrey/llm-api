"""
This type stub file was generated by pyright.
"""

"""MMBT configuration"""
logger = ...
class MMBTConfig:
    """
    This is the configuration class to store the configuration of a [`MMBTModel`]. It is used to instantiate a MMBT
    model according to the specified arguments, defining the model architecture.

    Args:
        config ([`PreTrainedConfig`]):
            Config of the underlying Transformer models. Its values are copied over to use a single config.
        num_labels (`int`, *optional*):
            Size of final Linear layer for classification.
        modal_hidden_size (`int`, *optional*, defaults to 2048):
            Embedding dimension of the non-text modality encoder.
    """
    def __init__(self, config, num_labels=..., modal_hidden_size=...) -> None:
        ...
    


