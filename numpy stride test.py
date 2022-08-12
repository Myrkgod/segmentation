import os.path
import numpy as np
import tifffile
from pathlib import Path
from matplotlib import pyplot as plt
from numpy import lib
from medpy.io import load, save
from numpy.lib.stride_tricks import sliding_window_view

a = np.array([[[0, 1, 2, 3, 4],
              [10, 11, 12, 13, 14],
              [20, 21, 22, 23, 24],
              [30, 31, 32, 33, 34],
              [40, 41, 42, 43, 44]],

            [[100, 101, 102, 103, 104],
             [110, 111, 112, 113, 114],
             [120, 121, 122, 123, 124],
             [130, 131, 132, 133, 134],
             [140, 141, 142, 143, 144]],

            [[200, 201, 202, 203, 204],
             [210, 211, 212, 213, 214],
             [220, 221, 222, 223, 224],
             [230, 231, 232, 233, 234],
             [240, 241, 242, 243, 244]]])
print(a)

b = sliding_window_view(a, (3, 3, 2))
print(a.shape)
print(b.shape)
print(b.reshape(12, 3, 3, 2))