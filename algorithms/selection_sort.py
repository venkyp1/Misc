"""

Selection sort

1. Select index[0] as the min, then scan the remaining to find one smaller than that
2. Then swap the numbers at the end of the scan.
3. Now move to the next index and assign that as min
4. Repeat step(2)

Venky, 01/28/2018

"""


def selection_sort(a):

    l = len(a)
    for i in range(l):
        min = array[i]
        min_index = i
        for j in range(i, l):
            if min > a[j]:
                min = a[j]
                min_index = j
        print("Loop count{} ".format(i), a)
        # At end of the scan, place the min in the correct index
        a[i], a[min_index] = a[min_index], a[i]
    return a


if __name__ == "__main__":

    array = [22, 3, 44, 55, 7, 11, 10, 5, 2, 0]
    print("Before sorted: ", array)
    print("After sorted: ", selection_sort(array))
