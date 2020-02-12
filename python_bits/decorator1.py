 
######################################################
        # Venky, Wed Mar 11 12:14:48 2015 # 
######################################################
        
        
        
# Using a class decorator.
# The class should have implemented __call_() method
# for the class to be 'callable' otherwise this WILL NOT work

# When a decorator is applied to a function, the orginal function is replaced
# by the decorator. The decorator can be used to do some 'initialization' that
# is needed before the actual function call.

#Note:
# When calling a decorator like a function, it needs to return another function which is the actual decorator:

# The outer function will be given any arguments you pass explicitly, and should return the inner function. The inner function will be passed the function to decorate, and return the wrapped function.


class mydecor:

    def __init__(self,func):
        print("mydecor.init() called")
        self.f = func  # Just save it in the class

    def __call__(self):
        print("mydecor.call() called")
        self.f()  # call the function here

@mydecor
def myfun():
    print("myfun() called")

myfun()

## Here before calling myfun(), the decorator which is a class gets called.
## This will call the __init__, (), calls __call__() method and then 
## myfun() gets called.

# Result:
#
# $ ./decorator1.py 
# mydecor.init() called
# mydecor.call() called
# myfun() called




