"""

Kandane' algorithm

  Find the largest sequence of numbers
  [or] Find the largest value of a sub array

  Venky, 12/08/2017

"""


def kandane(arr):

    max_current = max_global = arr[0]
    l = len(arr)

    for i in range(1, l):
        max_current = max(max_current + arr[i], a[i])
        # print("max_current = {}  max_global = {}".format(max_current, max_global))
        if max_current > max_global:
            max_global = max_current
    return max_global


if __name__ == "__main__":

    a = [7, 4, -3, 6, 2, 0, -13, 11, 1]

    print(kandane(a))
