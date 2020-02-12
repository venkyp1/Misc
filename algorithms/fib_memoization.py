"""
Fibonacci function using 'memoization' to calculate
A lookup table initialize the values which can be used
to find values when needed.
Venky, 01/12/2018

"""


lookup = []


def fib(n):

    global lookup
    if lookup[n] == 0:
        if n <= 1:
            lookup[n] = 1
        else:
            lookup[n] = fib(n - 1) + fib(n - 2)
    return lookup[n]


if __name__ == "__main__":

    # Initialize the array up to 50 numbers
    lookup = [0 for x in range(50)]

    print("fib 30: ", fib(30))  # this will init the  table up to 30
    print("fib 10: ", fib(10))  # This will be just a look up
    print("fib 20: ", fib(20))  # This will be just a look up
    print("fib 31: ", fib(31))  # This will up to 30 to calculate 31
