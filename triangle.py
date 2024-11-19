from math import sqrt
def area(a, b, c):
    x = (a + b + c) / 2
    return sqrt(x * (x - a) * (x - b) * (x - c))

def perimeter(a, b, c):
    return a + b + c
