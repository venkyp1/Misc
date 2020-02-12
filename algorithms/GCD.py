"""
GCD = Greatest Common Denominator

Find the GCD of TWO numbers using Euclid's approach

Note: Same approach but different coding.

Venky, 02/10/2018

"""


def gcd(a, b):
    if a == b:
        print("a = {}  b = {}".format(a, b))
        return a
    if a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)


def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


def gcd_find(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    a = 60
    b = 48
    print("GCD of {0} and {1} is: ".format(a, b), gcd(a, b))
    print("GCD of {} and {} is: ".format(a, b), gcd_recursive(a, b))
    print("GCD of {} and {} is: ".format(a, b), gcd_find(a, b))
