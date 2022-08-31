#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
    def __init__(self, object):
        self.start = object

    def write(self, end):
        print(self.start + end)


def main():
    p = Prepend("+++ ")
    p.write("Hello")

if __name__ == "__main__":
    main()
