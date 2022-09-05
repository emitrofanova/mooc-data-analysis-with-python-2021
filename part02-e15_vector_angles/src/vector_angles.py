#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    xy= np.sum(X*Y, axis = 1)
    x = np.sum(X*X, axis = 1)
    y = np.sum(Y*Y, axis = 1)
    x = np.sqrt(x)
    y = np.sqrt(y)
    cos = xy / (x * y)
    cos = np.clip(cos, a_min = -1, a_max = 1)
    answ = np.arccos(cos)
    answ = np.degrees(answ)
    return answ

def main():
    np.random.seed(9)
    a = np.array([[0, 0, 1],
        [-1, 1, 0]])
    b = np.array([[0, 1, 0],
        [1, 1, 0]])
    print(vector_angles(a, b))

if __name__ == "__main__":
    main()
