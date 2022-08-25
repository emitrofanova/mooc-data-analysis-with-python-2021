#!/usr/bin/env python3

def transform(s1, s2):
    return [nums[0] * nums[1] for nums in zip(map(int, s1.split()), map(int, s2.split()))] 

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
