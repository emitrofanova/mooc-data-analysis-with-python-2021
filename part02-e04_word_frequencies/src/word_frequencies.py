#!/usr/bin/env python3

def word_frequencies(filename):
    answ = {}
    with open(filename, "r") as f:
        text = f.read()
    text = text.split()
    for word in text:
        word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
        if word not in answ:
            answ[word] = 0
        answ[word] += 1
    return answ

def main():
    print(word_frequencies("src/alice.txt"))

if __name__ == "__main__":
    main()
