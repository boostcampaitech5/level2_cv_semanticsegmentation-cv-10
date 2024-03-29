import torch
import torch.nn as nn


class DiceLoss(nn.Module):
    def __init__(self):
        super(DiceLoss, self).__init__()

    def forward(self, pred, true, eps=0.0001):
        pred = torch.sigmoid(pred)
        # pred = (pred > thr)
        # true = true

        pred_flat = pred.flatten(2)
        true_flat = true.flatten(2)
        inter = torch.sum(true_flat * pred_flat, -1)
        dice = (2.0 * inter + eps) / (
            torch.sum(true_flat, -1) + torch.sum(pred_flat, -1) + eps
        )

        return 1 - dice.mean()


class IoULoss(nn.Module):
    def __init__(self):
        super(IoULoss, self).__init__()

    def forward(self, pred, true, eps=0.0001):
        pred = torch.sigmoid(pred)
        pred = pred.view(-1)
        true = true.view(-1)

        inter = (pred * true).sum()
        union = (pred + true).sum() - inter
        iou = (inter + eps) / (union + eps)

        return 1.0 - iou
