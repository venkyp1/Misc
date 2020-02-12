"""

Note: Binary search works only on a sorted array
Venky, 02/21/18

"""


def binary_search(arr, element, lower, upper):

    if upper > lower:
        mid = int((lower + (upper - 1)) / 2)
        # print("Element = {}  mid = {}  lower = {}  upper = {}".format(element, mid, lower, upper))
        if element == arr[mid]:
            print("Found: element {} at index {}".format(element, mid))
            return
        elif element > arr[mid]:
            return binary_search(arr, element, mid + 1, upper)
        else:
            return binary_search(arr, element, 0, mid - 1)
    else:
        print("Not Found: element {}".format(element))
        return


if __name__ == "__main__":

    # Odd count
    #      0  1  2   3  4   5   6    7    8    9
    arr = [3, 5, 7, 11, 22, 55, 92, 101, 174, 220]
    binary_search(arr, 2, 0, len(arr))
    binary_search(arr, 500, 0, len(arr))
    binary_search(arr, 2, 0, len(arr))
    binary_search(arr, 65, 0, len(arr))
    binary_search(arr, 7, 0, len(arr))
    binary_search(arr, 220, 0, len(arr))
    binary_search(arr, 55, 0, len(arr))

    # Even count
    #      0  1  2   3  4   5   6    7    8    9    10
    arr = [3, 5, 7, 11, 22, 55, 92, 101, 174, 220, 400]
    binary_search(arr, 2, 0, len(arr))
    binary_search(arr, 65, 0, len(arr))
    binary_search(arr, 220, 0, len(arr))
    binary_search(arr, 55, 0, len(arr))
    binary_search(arr, 400, 0, len(arr))
    binary_search(arr, 500, 0, len(arr))
