#!/usr/bin/env python3

import numpy as np

def diamond(n):
    ar_r_up = np.eye(n, dtype = int)
    ar_l_up = ar_r_up[::-1]
    ar_r_up = ar_r_up[:,1:]
    ar_lr_up = np.concatenate((ar_l_up, ar_r_up), axis = 1)
    answ = ar_lr_up
    for row in ar_lr_up[n-2::-1]:
        if row.all() == [1]:
            continue
        answ = np.concatenate((answ, row.reshape(1, len(row))))
    return answ

def main():
    print(diamond(4))

if __name__ == "__main__":
    main()
