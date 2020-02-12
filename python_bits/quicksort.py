'''
Quicksort

 How:
 Pick a number, called PIVOT. Now put numbers smaller than pivot
 on the LEFT and larger numbers on the RIGHT. Put the PIVOT at the middle.
 Now you got 2 arrays.
 Sort the tow arrays... recursively and then merge them.
 venky, 2/7/16

'''


def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    if begin >= end:
        return
    pivot = partition(array, begin, end)
    quicksort(array, begin, pivot-1)
    quicksort(array, pivot+1, end)

if __name__ == '__main__':

   array = [97, 200, 100, 101, 211, 107]
   
   print("Unsorted array: ", array)
   
   quicksort(array)
   
   print("Sorted array: ", array)

  
