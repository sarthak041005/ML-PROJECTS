import cv2
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

pred_dir = os.path.join(BASE_DIR, "predictions")
mask_dir = os.path.join(BASE_DIR, "masks")

ious = []

for file in os.listdir(pred_dir):

    pred = cv2.imread(os.path.join(pred_dir, file), 0)

    mask = cv2.imread(
        os.path.join(mask_dir, file.replace(".png", "_mask.png")),
        0
    )

    pred = pred > 0
    mask = mask > 0

    intersection = np.logical_and(pred, mask).sum()
    union = np.logical_or(pred, mask).sum()

    iou = intersection / union if union != 0 else 1

    print(file, "IoU =", round(iou, 3))
    ious.append(iou)

print("\nMean IoU =", round(np.mean(ious), 3))

# How IoU is Calculated

# The Intersection over Union (IoU) metric measures how well the predicted segmentation overlaps with the ground truth.

# IoU=
# Area of Union
# Area of Overlap
# 	​


# Where:

# Intersection = Pixels common to both the predicted mask and the ground truth.
# Union = Pixels present in either the predicted mask or the ground truth.

# Example:

# Ground Truth Pixels = 1200
# Predicted Pixels = 1180
# Overlap = 1100
# IoU=
# 1200+1180−1100
# 1100
# 	​

# =0.859