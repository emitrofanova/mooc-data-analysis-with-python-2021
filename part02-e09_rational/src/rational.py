
#!/usr/bin/env python3
from fractions import Fraction

class Rational(object):
    def __init__(self, first, second):
        self.num = Fraction(first, second)

    def __mul__(self, second_num):
        return self.num * second_num.num

    def __truediv__(self, second_num):
        return self.num / second_num.num

    def __add__(self, second_num):
        return self.num + second_num.num

    def __sub__(self, second_num):
        return self.num - second_num.num

    def __eq__(self, second_num):
        if type(second_num) == Fraction:
            return self.num == second_num
        return self.num == second_num.num

    def __gt__(self, second_num):
        if type(second_num) == Fraction:
            return self.num > second_num
        return self.num > second_num.num
    
    def __lt__(self, second_num):
        if type(second_num) == Fraction:
            return self.num < second_num
        return self.num < second_num.num

    def __str__(self):
        return f"{self.num}"

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))
    print(r1*r2 < Rational(2,12))

if __name__ == "__main__":
    main()