import numpy as np
from medpy.io import load, save
from skimage.draw import polygon
import matplotlib.pyplot as plt

mask, header = load('/Users/nate/Adam curated/watershed/Scan_Iter_0000_CamA_ch0_CAM1_stack0000_488nm_0000000msec_0016966725msecAbs_decon.mha')

r = np.array([18, 120, 121, 38, 117, 117, 40, 116, 116, 38, 108, 966, 965])
c = np.array([3, 52, 61, 61, 97, 109, 109, 146, 156, 150, 189, 189, 3])
row, col = polygon(r, c)

mask_crop = mask.copy()
mask_crop[:, row, col] = 1
labels_to_remove = np.unique(mask_crop)

mask_without_labels = np.where(np.isin(mask, labels_to_remove), 1, mask)
save(mask_without_labels, "nate_the_great.mha", header)


