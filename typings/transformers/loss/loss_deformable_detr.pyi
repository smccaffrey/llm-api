"""
This type stub file was generated by pyright.
"""

import torch
from ..utils import is_scipy_available
from .loss_for_object_detection import HungarianMatcher, ImageLoss

if is_scipy_available():
    ...
class DeformableDetrHungarianMatcher(HungarianMatcher):
    @torch.no_grad()
    def forward(self, outputs, targets): # -> list[tuple[Tensor, Tensor]]:
        """
        Differences:
        - out_prob = outputs["logits"].flatten(0, 1).sigmoid() instead of softmax
        - class_cost uses alpha and gamma
        """
        ...
    


class DeformableDetrImageLoss(ImageLoss):
    def __init__(self, matcher, num_classes, focal_alpha, losses) -> None:
        ...
    
    def loss_labels(self, outputs, targets, indices, num_boxes): # -> dict[str, Any]:
        """
        Classification loss (Binary focal loss) targets dicts must contain the key "class_labels" containing a tensor
        of dim [nb_target_boxes]
        """
        ...
    


def DeformableDetrForSegmentationLoss(logits, labels, device, pred_boxes, pred_masks, config, outputs_class=..., outputs_coord=..., **kwargs): # -> tuple[int, Any, list[dict[str, Any]] | None]:
    ...

def DeformableDetrForObjectDetectionLoss(logits, labels, device, pred_boxes, config, outputs_class=..., outputs_coord=..., **kwargs): # -> tuple[int, Any, list[dict[str, Any]] | None]:
    ...

