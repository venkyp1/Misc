#!/usr/bin/env python3.1


'''
Insertion sort
Venky, Jan/18/2014
'''


arr = [3,5,1,54,6,2,6,9,0]
data = arr[:]

def insertion_sort(a):
 aL = len(a)
 for j in range(2,aL):
    key = a[j]
    i = j - 1
    while (i >= 0 and a[i] > key):
       a[i+1] = a[i]
       i = i-1
    a[i+1] = key
 return arr

print ("Initial:  ", data)
print ("Solved:  ", insertion_sort(arr))
