#!/usr/bin/env python3
def triple(x):
    return x*3
   
def square(y):
    return y**2

def main():
    for i in range(1, 11):
        i_triple = triple(i)
        i_square = square(i)
        if i_triple < i_square:
            break
        else:
            print(f"triple({i})=={i_triple} square({i})=={i_square}")

if __name__ == "__main__":
    main()
