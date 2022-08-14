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
v = sliding_window_view(mask, (100, 100, 100))
v = v[::90, ::90, ::90, :, :, :]

shape = v.shape
v = v.reshape((shape[0]*shape[1]*shape[2], shape[3], shape[4], shape[5]))
print(v.shape)



