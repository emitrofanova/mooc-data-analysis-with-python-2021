#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    i = np.arange(n)
    j = np.arange(n).reshape((n, 1))
    answ = i * j
    return answ

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
