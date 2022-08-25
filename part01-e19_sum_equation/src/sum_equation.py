#!/usr/bin/env python3

def sum_equation(L):
    if L == []:
        return "0 = 0"
    return " + ".join(map(str, L)) + " = " + str(sum(L))

def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
