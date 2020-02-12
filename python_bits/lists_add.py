'''
Venky, Fri Jan 10 20:23:52 PST 2020

Program to add to lists
Example:
  [2, 3, 5] + [4, 5, 2] produces [6, 8, 7]
  [4, 5, 7] + [6, 7, 2, 4] produces [7, 1, 8, 1]

'''
   
def add_lists(a, b):
    la = len(a)
    lb = len(b)
    # Error scenarios
    if la == 0:
        return b
    if lb == 0:
        return a
    if la < lb:
        d = lb - la
        for i in range(d):
            a.insert(0, 0)
    if la > lb:
        d = la - lb
        for i in range(d):
            b.insert(0, 0)
    result = []
    l = len(a)
    carry = 0
    remind = 0
    val = 0
    for i in range(l-1,-1,-1):
        val = a[i] + b[i] + carry
        if val > 9:
           carry = int(val/10)
           remind = int(val%10)
           result.insert(0, remind)
        else:
           carry = 0; remind = 0
           result.insert(0, val)
    return result
     

print(add_lists([3,4,9,7,1], [4,3]))
print(add_lists([5, 6, 7, 3, 9], [2, 3, 4, 5, 6, 7, 8]))
print(add_lists([4, 5, 7], [6, 7, 2, 4]))
