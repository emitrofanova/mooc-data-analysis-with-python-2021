#!/usr/bin/env python3

def extract_numbers(s):
    answ = []
    s_split = s.split()
    for word in s_split:
        try:
            num = int(word)
        except:
            try:
                num = float(word)
            except:
                continue
        answ.append(num)      
    return answ

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
