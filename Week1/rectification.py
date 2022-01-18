from math import ceil

from PIL import Image, ImageDraw
import numpy as np
from scipy.ndimage import map_coordinates
import matplotlib.pyplot as plt
import homographies as Hf


def affine_rectification(l1,l2,l3,l4):
    inf_pt_1 = np.cross(l1,l2)
    inf_pt_1 /= inf_pt_1[2]
    
    inf_pt_2 = np.cross(l3,l4)
    inf_pt_2 /= inf_pt_2[2]
    
    inf_line = np.cross(inf_pt_1,inf_pt_2)
    inf_line /= inf_line[2]
    
    H_temp = Hf.id()
    H_temp[2,0] = inf_line[0]
    H_temp[2,1] = inf_line[1]
    H_temp[2,2] = inf_line[2]
    
    return H_temp