#!/usr/bin/env python


# Multiprocess will create separate process which will show up in the
# OS process table. Each process will be bound to a CPU.
# In a multi-core system, multiple processes can run to improve the performance
# of the work to be done.


from multiprocessing import *
import os

def func(i):
    print ("PID : ", os.getpid())
    print ("Received: ", i)


if __name__ == '__main__':
    
    # This is FYI--
    y = [1,2,3,4,5] #List
    func(y)

    y = 2,3,4,5,6   #Tuple
    func(y)


    # Important code starts here

    x = 99
    p = Process(target=func, args=(x,))  # , is needed here. This 
                                         # shows it is iterable :-(
    p.start()
    print ("PID : ", os.getpid())
    p.join()

    # call another method
    pos = [3,4,5,6]   # This will be a list
    p = Process(target=func, args=(pos,))  
    p.start()
    p.join()


    pos = 3,4,5,6   #This will be Tuple
    p = Process(target=func, args=(pos,))  
    p.start()
    p.join()
