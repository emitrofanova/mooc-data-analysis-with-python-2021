#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    with open(filename, "r") as f:
        answ = []
        for line in f:
            l = re.search(r'(\d+)\s+([a-zA-Z]+)\s+(\d+)\s+(\d+)[:]+(\d+)\s+([\w\.]+)', line)
            new_line = int(l.groups(1)[0]), l.groups(1)[1], int(l.groups(1)[2]), int(l.groups(1)[3]), int(l.groups(1)[4]), l.groups(1)[5]
            answ.append(new_line)
    return answ

def main():
    print(file_listing())

if __name__ == "__main__":
    main()
