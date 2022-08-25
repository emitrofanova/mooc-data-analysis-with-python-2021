#!/usr/bin/env python3

def distinct_characters(lst):
    dct = {}
    for i in lst:
        dct[i] = len(set(i))
    return dct

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
