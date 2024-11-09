"""
This type stub file was generated by pyright.
"""

from torch.utils.data import Dataset, IterableDataset

class PipelineDataset(Dataset):
    def __init__(self, dataset, process, params) -> None:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def __getitem__(self, i):
        ...
    


class PipelineIterator(IterableDataset):
    def __init__(self, loader, infer, params, loader_batch_size=...) -> None:
        """
        Roughly equivalent to

        ```
        for item in loader:
            yield infer(item, **params)
        ```

                Arguments:
                    loader (`torch.utils.data.DataLoader` or `Iterable`):
                        The iterator that will be used to apply `infer` on.
                    infer (any function):
                        The function to apply of each element of `loader`.
                    params (`dict`):
                        The parameters passed to `infer` along with every item
                    loader_batch_size (`int`, *optional*):
                        If specified, the items of `loader` are supposed to come as batch, and are loader_batched here
                        making it roughly behave as


        ```
        for items in loader:
            for i in loader_batch_size:
                item = items[i]
                yield infer(item, **params)
        ```"""
        ...
    
    def __len__(self): # -> int:
        ...
    
    def __iter__(self): # -> Self:
        ...
    
    def loader_batch_item(self): # -> Tensor | None:
        """
        Return item located at `loader_batch_index` within the current `loader_batch_data`.
        """
        ...
    
    def __next__(self): # -> Tensor | None:
        ...
    


class PipelineChunkIterator(PipelineIterator):
    def __init__(self, loader, infer, params, loader_batch_size=...) -> None:
        """
        Roughly equivalent to

        ```
        for iterator in loader:
            for item in iterator:
                yield infer(item, **params)
        ```

                Arguments:
                    loader (`torch.utils.data.DataLoader` or `Iterable`):
                        The iterator that will be used to apply `infer` on.
                    infer (any function):
                        The function to apply of each element of `loader`.
                    params (`dict`):
                        The parameters passed to `infer` along with every item
        """
        ...
    
    def __iter__(self): # -> Self:
        ...
    
    def __next__(self):
        ...
    


class PipelinePackIterator(PipelineIterator):
    """
    Roughly equivalent to

    ```
    packed =  []
    for item in loader:
        packed.append(item)
        if item["is_last"]:
            yield packed
            packed = []
    ```

        but it also handles cases where `item` are batched (meaning it's a dict of Tensor with first dimension > 1. In
        that case it does

    ```
    packed =  []
    for batch in loader:
        # item is batched
        for item in batch:
            packed.append(item)
            if item["is_last"]:
                yield packed
                packed = []
    ```

        Arguments:
            loader (`torch.utils.data.DataLoader` or `Iterable`):
                The iterator that will be used to apply `infer` on.
            infer (any function):
                The function to apply of each element of `loader`.
            params (`dict`):
                The parameters passed to `infer` along with every item
            loader_batch_size (`int`, *optional*):
                If specified, the items of `loader` are supposed to come as batch, and are loader_batched here making
                it roughly behave as


    ```
    for items in loader:
        for i in loader_batch_size:
            item = items[i]
            yield infer(item, **params)
    ```"""
    def __iter__(self): # -> Self:
        ...
    
    def __next__(self): # -> list[Any]:
        ...
    


class KeyDataset(Dataset):
    def __init__(self, dataset: Dataset, key: str) -> None:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def __getitem__(self, i):
        ...
    


class KeyPairDataset(Dataset):
    def __init__(self, dataset: Dataset, key1: str, key2: str) -> None:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def __getitem__(self, i): # -> dict[str, Any]:
        ...
    

