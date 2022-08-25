#!/usr/bin/env python3

def merge(L1, L2):
    new_list = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            new_list.append(L1[i])
            i += 1
        elif L1[i] == L2[j]:
            new_list.append(L1[i])
            new_list.append(L2[j])
            i += 1
            j += 1
        else:
            new_list.append(L2[j])
            j += 1
    while j < len(L2):
        new_list.append(L2[j])
        j += 1
    while i < len(L1):
        new_list.append(L1[i])
        i += 1

    return new_list

def main():
    print(merge([1, 5, 9, 12], [2, 6, 10]))

if __name__ == "__main__":
    main()
