 
######################################################
        # Venky, Tue Aug 16 09:15:08 2016 # 
######################################################
        
        
# Using a class decorator.
# The class should have implemented __call_() method
# for the class to be 'callable' otherwise this WILL NOT work

# When a decorator is applied to a function, the orginal function is replaced
# by the decorator. The decorator can be used to do some 'initialization' that
# is needed before the actual function call.

# Note:  Change 3
# Here passing arguments to both decorator and the decorated function 'myfun()'
# However decorator arguments are 'HARD CODED'.


class mydecor:           #< <===== Decorator class

    def __init__(self, dx, dy):      #<=== Decorator args are here
        print("mydecor.init() called")
        self.dx = dx
        self.dy = dy
        print("Decorator Args: ", self.dx, self.dy)

    def __call__(self, f):
        print("mydecor.call() called")
        def wrapped_f(*args):      #<=== Decorated myfun() args are here
            print("Inside wrapped")
            f(*args)  # call the function here with the args
            print("return from wrapped")
        return wrapped_f


@mydecor('hello', 'world')     #<<==== Decorator HARD CODED args
def myfun(a, b, c, d):   #<<===== Decorated method/function
    print("myfun() called")
    print ("Decorated Args: A : ", a, " B: ", b, " C: ", c, " D: ", d)

myfun(2,4,6,8)


#  Result:
#  $ ./decorator4.py 
#  mydecor.init() called
#  Decorator Args:  hello world
#  mydecor.call() called
#  Inside wrapped
#  myfun() called
#  Decorated Args: A :  2  B:  4  C:  6  D:  8
#  return from wrapped

