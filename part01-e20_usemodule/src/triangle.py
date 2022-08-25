# Enter you module contents here
import math
def hypothenuse(side1, side2):
    "returns the length of the hypothenuse when given the lengths of two other sides of a right-angled triangle"
    return math.sqrt(side1**2 + side2**2)

def area(side1, side2):
    "returns the area of the right-angled triangle, when two sides, perpendicular to each other, are given as parameters"
    return side1 * side2 / 2

__doc__ = "hypothenuse and area functions for the right-angled triangle, when two sides, perpendicular to each other, are given as parameters"
__version__ = "1.0"
__author__ = "emitrofanova"
