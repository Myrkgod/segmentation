import os.path
import numpy as np
import tifffile
from medpy.io import load, save

path = "~/Documents/Segmentation/Scan_Iter_0000_CamA_ch0_CAM1_stack0000_488nm_0000000msec_0016966725msec_dedcon.tif"
print(os.path.isfile(os.path.expanduser(path)))
tifffile.imread(os.path.expanduser(path))