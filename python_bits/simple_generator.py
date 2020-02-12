'''
Generator to create a even number list
Remember yield() returns value
venky, 2/1/17
'''


def get_even(start, end):
    for e in range(start,end):
        if (e % 2 == 0):
            yield e
        

even_list = list(get_even(20,80))
print (even_list)
    
'''
using a generator to print fibonocci series
'''

def fibonocci(max):

    a, b = 0, 1
    while a < max:
        yield a
        a,b = b, a+b

for x in fibonocci(500):
    print (x)
