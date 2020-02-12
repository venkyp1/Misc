"""
Bubble sort
Venky, 01/23/2018

"""


def bubble_sort(a):

    l = len(a)  # Array length
    for i in range(l):
        for k in range(l - 1):
            if a[k] > a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]
        print("Loop count{} ".format(i), a)
    return a


if __name__ == "__main__":
    array = [3, 9, 5, 7, 1, 0, 8, -10, 8]
    print("Initial array: ", array)
    print("Sorted array: ", bubble_sort(array))
