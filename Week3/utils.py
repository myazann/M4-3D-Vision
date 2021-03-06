import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import random

def line_draw(line, canv, size):
    def get_y(t):
        return -(line[0] * t + line[2]) / line[1]

    def get_x(t):
        return -(line[1] * t + line[2]) / line[0]

    w, h = size

    if line[0] != 0 and abs(get_x(0) - get_x(w)) < w:
        beg = (get_x(0), 0)
        end = (get_x(h), h)
    else:
        beg = (0, get_y(0))
        end = (w, get_y(w))
    canv.line([beg, end], width=4)


def plot_img(img, do_not_use=[0]):
    plt.figure(do_not_use[0])
    do_not_use[0] += 1
    plt.imshow(img)


def Inliers(F, x, xp, th):

    t_x = F@x
    t_xp = F.T@xp
    d = np.diag(xp.T@F@x)
    dn = (t_x[0]**2 + t_x[1]**2 + t_xp[0]**2 + t_xp[1]**2)
    final = d**2/dn
    
    return np.where(np.array(final) < th)[0]
