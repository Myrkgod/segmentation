import os.path
import numpy as np
import tifffile
from pathlib import Path
from matplotlib import pyplot as plt
from numpy import lib
from medpy.io import load, save
from numpy.lib.stride_tricks import sliding_window_view
mask, header = load(r"C:\Users\natel\Documents\Scan_Iter_0000_CamA_ch0_CAM1_stack0000_488nm_0000000msec_0016966725msecAbs_decon.mha")

print(mask.shape)
v = sliding_window_view(mask, (30, 30, 30))
print(v.shape)
# print(v)



