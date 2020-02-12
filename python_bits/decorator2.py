 
######################################################
        # Venky, Tue Aug 16 09:08:02 2016 # 
######################################################
        
        

# Using a class decorator.
# The class should have implemented __call_() method
# for the class to be 'callable' otherwise this WILL NOT work

# When a decorator is applied to a function, the orginal function is replaced
# by the decorator. The decorator can be used to do some 'initialization' that
# is needed before the actual function call.

#Note: Change 1
#  No arguments being passed.
#  Note: __call__ () should be use d instead of constructor.  DO NOT USE THIS.


class mydecor:

    def __init__(self,func):
        print("mydecor.init() called")
        func()    #<< This calls myfun()
                  # Not a good idea.  When pass params, that will go to __call__ ONLY

    def __call__(self):  # Other params will be received by __call__() ONLY
        print("mydecor.call() called")

@mydecor
def myfun():
    print("myfun() called")

myfun()

## Here before calling myfun(), the decorator which is a class gets called.
## This will call the __init__, then the myfun(), finally 
## calls __call__() method.

#Result:
#
#$ ./decorator1.py 
#mydecor.init() called
#myfun() called
#mydecor.call() called
#papavv-dl:/export/venkyp/test/python
#$ 




