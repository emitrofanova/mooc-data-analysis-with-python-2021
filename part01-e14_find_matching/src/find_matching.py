#!/usr/bin/env python3

def find_matching(L, pattern):
    answ = []
    for i, x in enumerate(L):
        if pattern in x:
            answ.append(i)
    return answ

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
