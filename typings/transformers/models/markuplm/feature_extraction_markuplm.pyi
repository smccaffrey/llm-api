"""
This type stub file was generated by pyright.
"""

from ...feature_extraction_utils import BatchFeature, FeatureExtractionMixin
from ...utils import is_bs4_available

"""
Feature extractor class for MarkupLM.
"""
if is_bs4_available():
    ...
logger = ...
class MarkupLMFeatureExtractor(FeatureExtractionMixin):
    r"""
    Constructs a MarkupLM feature extractor. This can be used to get a list of nodes and corresponding xpaths from HTML
    strings.

    This feature extractor inherits from [`~feature_extraction_utils.PreTrainedFeatureExtractor`] which contains most
    of the main methods. Users should refer to this superclass for more information regarding those methods.

    """
    def __init__(self, **kwargs) -> None:
        ...
    
    def xpath_soup(self, element): # -> tuple[list[Any], list[Any]]:
        ...
    
    def get_three_from_single(self, html_string): # -> tuple[list[Any], list[Any], list[Any]]:
        ...
    
    def construct_xpath(self, xpath_tags, xpath_subscripts): # -> str:
        ...
    
    def __call__(self, html_strings) -> BatchFeature:
        """
        Main method to prepare for the model one or several HTML strings.

        Args:
            html_strings (`str`, `List[str]`):
                The HTML string or batch of HTML strings from which to extract nodes and corresponding xpaths.

        Returns:
            [`BatchFeature`]: A [`BatchFeature`] with the following fields:

            - **nodes** -- Nodes.
            - **xpaths** -- Corresponding xpaths.

        Examples:

        ```python
        >>> from transformers import MarkupLMFeatureExtractor

        >>> page_name_1 = "page1.html"
        >>> page_name_2 = "page2.html"
        >>> page_name_3 = "page3.html"

        >>> with open(page_name_1) as f:
        ...     single_html_string = f.read()

        >>> feature_extractor = MarkupLMFeatureExtractor()

        >>> # single example
        >>> encoding = feature_extractor(single_html_string)
        >>> print(encoding.keys())
        >>> # dict_keys(['nodes', 'xpaths'])

        >>> # batched example

        >>> multi_html_strings = []

        >>> with open(page_name_2) as f:
        ...     multi_html_strings.append(f.read())
        >>> with open(page_name_3) as f:
        ...     multi_html_strings.append(f.read())

        >>> encoding = feature_extractor(multi_html_strings)
        >>> print(encoding.keys())
        >>> # dict_keys(['nodes', 'xpaths'])
        ```"""
        ...
    


