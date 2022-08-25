#!/usr/bin/env python3

def reverse_dictionary(d):
    dct = {}
    for word in d:
        print(d[word])
        for i in d[word]:
            if i not in dct:
                dct[i] = [word]
            else:
                dct[i].append(word)
    return dct

def main():
    print(reverse_dictionary({'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}))

if __name__ == "__main__":
    main()
