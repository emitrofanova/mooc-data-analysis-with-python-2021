#!/usr/bin/env python3

def interleave(*lists):
    answ = []
    for i in list(zip(*lists)):
        answ += i       
    return answ

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
