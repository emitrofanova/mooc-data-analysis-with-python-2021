#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    a = a**2
    answ = np.sum(a, axis = 1)
    answ = np.sqrt(answ)
    return answ

def main():
    np.random.seed(9)
    a=np.random.randint(0, 10, (3,4))
    print(vector_lengths(a))

if __name__ == "__main__":
    main()
