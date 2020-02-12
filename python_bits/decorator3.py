 
######################################################
        # Venky, Wed Nov  6 09:52:08 2019 # 
######################################################
        


# Using a class decorator.
# The class should have implemented __call_() method
# for the class to be 'callable' otherwise this WILL NOT work

# When a decorator is applied to a function, the orginal function is replaced
# by the decorator. The decorator can be used to do some 'initialization' that
# is needed before the actual function call.

#Note:  Change 2
# Here passing arguments to decorated function 'myfun()'
# The arguements are passed to __call__() method.



class mydecor:           #< <===== Decorator class

    #__init__ gets the decorated func name
    def __init__(self,func):
        print("mydecor.init() called")
        self.f = func  # Just save it in the class

                                          # Decorated func arguments are passed to __call__
    def __call__(self, *args):
        print("mydecor.call() called")
        self.f(*args)  # call the function here with the args

@mydecor                 #<<==== Decorator
def myfun(a, b, c, d):   #<<===== Decorated method/function
    print("myfun() called")
    print ("A : ", a, " B: ", b, " C: ", c, " D: ", d)

myfun(2,4,6,8)



#Note: The __init__ will get called only ONCE.
# __call__() gets called every time the decorated function is called.

# $ ./decorator3.py
# mydecor.init() called
# mydecor.call() called   <====== Called ONLY once
# myfun() called
# A :  2  B:  4  C:  6  D:  8
# mydecor.call() called
# myfun() called
# A :  1  B:  3  C:  5  D:  7


## Here before calling myfun(), the decorator which is a class gets called.
## This will call the __init__, (), calls __call__() method and then 
## myfun() gets called.

# Result:
#
# $ ./decorator1.py 
# mydecor.init() called
# mydecor.call() called
# myfun() called




