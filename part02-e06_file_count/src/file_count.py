#!/usr/bin/env python3

import sys

def file_count(filename):
    with open(filename, "r") as f:
        linecount = 0
        wordcount = 0
        charactercount = 0
        for line in f:
            linecount += 1
            words = line.split()
            wordcount += len(words)
            charactercount += len(line)
    return (linecount, wordcount, charactercount)

def main():
    for f in sys.argv[1:]:
        nums = file_count(f)
        print(f"{nums[0]}\t{nums[1]}\t{nums[2]}\t{f}")

if __name__ == "__main__":
    main()
