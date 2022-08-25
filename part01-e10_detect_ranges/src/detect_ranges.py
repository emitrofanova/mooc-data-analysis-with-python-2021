#!/usr/bin/env python3

def detect_ranges(lst):
    lst_sort = sorted(lst)
    answ = []
    interval = []
    j = 0
    for i in lst_sort[:-1]:
        if i + 1 != lst_sort[j + 1]:
            if i - 1 == lst_sort[j - 1]:
                interval.append(i)
            else:
                answ.append(i)
            if interval != []:
                answ.append((interval[0], interval[-1] + 1))
                interval = []
        else:
            interval.append(i)
        j += 1

    if lst_sort[-1] == lst_sort[-2] +  1:
        interval.append(lst_sort[-1])
    else:
        answ.append(lst_sort[-1])
    if interval != []:
        answ.append((interval[0], interval[-1] + 1))
    return answ

def main():
    L = [2,5,4,8,12,6,7,10,13]
    L = sorted(L)
    print(L)
    result = detect_ranges(L)
    print(result)


if __name__ == "__main__":
    main()
