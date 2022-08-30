#!/usr/bin/env python3

import sys
import statistics

def summary(filename):
    with open(filename, "r") as f:
        text = f.read()
    text = text.split()
    nums = []
    for num in text:
        try:
            nums.append(float(num))
        except:
            pass
    sum_nums = sum(nums)
    mean_nums = statistics.mean(nums)
    stddev = statistics.stdev(nums, mean_nums)
    return (sum_nums, mean_nums, stddev)

def main():
    for f in sys.argv[1:]:
        nums = summary(f)
        print(f"File: {f} Sum: {nums[0]:.6f} Average: {nums[1]:.6f} Stddev: {nums[2]:.6f}")

if __name__ == "__main__":
    main()
