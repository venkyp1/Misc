"""

Quick sort
Venky, 10/08/2017

"""


def qsort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        # Just use the + operator to join lists
        # Note that you want equal ^^^^^ not pivot
        return qsort(less) + equal + qsort(greater)
    # You need to handle the part at the end of the recursion - when you only
    # have one element in your array, just return the array.
    else:
        return array


if __name__ == "__main__":
    a = [0, 4, 5, 6, 7, 3, 1, -15]
    print("unsorted array: ", a)
    print("sorted array: ", qsort(a))
