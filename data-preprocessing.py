import os
import numpy as np
import tifffile
import warnings
from pathlib import Path
from matplotlib import pyplot as plt
from numpy import lib
from medpy.io import load, save
from numpy.lib.stride_tricks import sliding_window_view

image_path = Path("/Users/nate/PycharmProjects/segmentation/images/Scan_Iter_0000_CamA_ch0_CAM1_stack0000_488nm_0000000msec_0016966725msec_decon.tif")
crops_path = Path.cwd() / image_path.stem
crops_path.mkdir(parents=True, exist_ok=True)

mask = tifffile.imread(image_path)
print(mask.shape)
img_dims = mask.shape
crop_size = (100, 100, 100)
step_size = 90

for i in range(len(mask.shape)):
    if (mask.shape[i] - crop_size[i]) % step_size != 0:  # Nate's theorem
        warnings.warn("Wrong crop/step size for array")

print(mask.shape)
img_crops = sliding_window_view(mask, crop_size)
img_crops = img_crops[::step_size, ::step_size, ::step_size, :, :, :]
crops_dims = img_crops.shape
print(crops_dims)

for x in range(crops_dims[0]):
    for y in range(crops_dims[1]):
        for z in range(crops_dims[2]):
            crop_name = str(str(x) + str(y) + str(z)) + ".tif"

            tifffile.imwrite(crops_path / crop_name, img_crops[x, y, z, :, :, :])

