import numpy as np


def id():
    return np.identity(3)


def translate(x, y):
    H = id()
    H[0, 2] = x
    H[1, 2] = y
    return H


def scale(x, y):
    H = id()
    H[0, 0] = x
    H[1, 1] = y
    return H


def rotate(angle):
    theta = np.radians(angle)
    H = id() * np.cos(theta)
    H[1, 0] = np.sin(theta)
    H[0, 1] = -H[1, 0]
    H[2, 2] = 1
    return H


def shear(ang_x, ang_y):
    th_x, th_y = np.radians(ang_x), np.radians(ang_y)
    H = id()
    H[0, 1] = np.tan(th_x)
    H[1, 0] = np.tan(th_y)
    return H


def affinity(theta, tau, sx, sy, tx, ty):
    D = scale(sx, sy)
    Rtheta = rotate(theta)
    Rtau_minus = rotate(-tau)
    Rtau_normal = rotate(tau)
    A = ((Rtheta @ Rtau_minus) @ D) @ Rtau_normal
    A[0:2, 2] += translate(tx, ty)[0:2, 2]
    return A


def projective(theta, tau, sx, sy, tx, ty, v1, v2):
    A = affinity(theta, tau, sx, sy, tx, ty)
    A[2, 0] = v1
    A[2, 1] = v2
    return A
