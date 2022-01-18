import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def work_with_numpy(f):
    def with_numpy(x, *args):
        res = f(np.array(x), *args)
        if type(res) == tuple:
            res, *rest = res
            tup = (Image.fromarray(res), *rest)
            return tup
        return Image.fromarray(res)

    return with_numpy


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


def compute_angle(line):
    if line[0] == 0:
        return 90
    res = np.degrees(np.arctan(line[1] / line[0]))
    return res if res >= 0 else 180 + res


def angle_diff(a, b, mod=180):
    diff = abs(a - b)
    return diff if diff < mod / 2 else mod - diff


def crop(I):

    ys, xs = np.where((I[:,:,0] != 0) & (I[:,:,1] != 0) & (I[:,:,2] != 0))
    x0, y0, x, y = np.min(xs), np.min(ys), np.max(xs), np.max(ys)
    return I[y0:y, x0:x]


# Computing S
def get_equation(l, r):
    a1 = l[0] * r[0]
    a2 = l[0] * r[1] + l[1] * r[0]
    a3 = l[1] * r[1]
    return np.array([a1, a2, a3])


def get_inters(l1, l2):
    res = np.cross(l1, l2)
    res /= res[2]
    return res
