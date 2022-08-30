#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    answ = []
    cnt = 0
    with open(filename, "r") as f:
        for line in f:
            cnt += 1
            if cnt == 1:
                continue
            l = re.search(r'(\d+)\s+(\d+)\s+(\d+)\s+(\w+\s*\w*)', line)
            new_line = "\t".join(l.groups())
            answ.append(new_line)
    return answ


def main():
    print(red_green_blue())

if __name__ == "__main__":
    main()
