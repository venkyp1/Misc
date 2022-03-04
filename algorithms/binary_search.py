#!/usr/bin/python3

"""
Note: Binary search works only on a sorted array
Venky, 02/21/18
"""


def binary_search(arr, e, l, h):

    if h > l:
       mid = int((l + h)/2)
       print("Element = {}  mid = {}  lower = {}  upper = {}".format(e, mid, l, h))
       if arr[mid] == e:
           print("Element = {}  mid = {}  lower = {}  upper = {}".format(e, mid, l, h))
           print("Found {} at {}".format(e, mid))
           return
       elif arr[mid] < e:
           print("Element = {}  mid = {}  lower = {}  upper = {}".format(e, mid, l, h))
           binary_search(arr, e, mid+1, h)
       elif arr[mid] > e:
           print("Element = {}  mid = {}  lower = {}  upper = {}".format(e, mid, l, h))
           binary_search(arr, e, l, mid-1)
    else:
       print("INFO:  {} cannot be found in{}".format(e, arr))
       return


if __name__ == "__main__":

    arr = [3, 5, 7, 11, 22, 55, 92, 101, 174, 220]
    arr = [3, 5, 7, 11, 22, 55, 92, 101, 174, 220, 400]
    arr = [3, 5, 7, 11, 22, 55, 92, 101 ]
    arr = [5, 7, 11, 22, 55, 92, 101, 174, 220, 400]
    print(arr)
    for i in list(range(len(arr))):
        print("------- searching {} -------------------------".format(arr[i]))
        binary_search(arr, arr[i], 0, len(arr))
        print("--------------------------------")

    arr = [3, 5, 7, 11, 22, 55, 92, 101 ]
    binary_search(arr, 200, 0, len(arr))
    binary_search(arr, 500, 0, len(arr))
    binary_search(arr, 65, 0, len(arr))
    binary_search(arr, 7, 0, len(arr))
    binary_search(arr, 220, 0, len(arr))
    binary_search(arr, 55, 0, len(arr))


    # Odd count
    #      0  1  2   3  4   5   6    7    8    9
    arr = [3, 5, 7, 11, 22, 55, 92, 101, 174, 220]
    #binary_search(arr, 2, 0, len(arr))
    binary_search(arr, 500, 0, len(arr))
    binary_search(arr, 65, 0, len(arr))
    binary_search(arr, 7, 0, len(arr))
    binary_search(arr, 220, 0, len(arr))
    binary_search(arr, 55, 0, len(arr))

    # Even count
    #      0  1  2   3  4   5   6    7    8    9    10
    arr = [3, 5, 7, 11, 22, 55, 92, 101, 174, 220, 400]
    #binary_search(arr, 2, 0, len(arr))
    binary_search(arr, 65, 0, len(arr))
    binary_search(arr, 220, 0, len(arr))
    binary_search(arr, 55, 0, len(arr))
    binary_search(arr, 400, 0, len(arr))
    binary_search(arr, 500, 0, len(arr))

