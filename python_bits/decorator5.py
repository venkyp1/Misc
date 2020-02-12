 
######################################################
        # Venky, Tue Aug 23 13:49:26 2016 # 
######################################################
        

# Using a function decorator.

# When a decorator is applied to a function, the orginal function is replaced
# by the decorator. The decorator can be used to do some 'initialization' that
# is needed before the actual function call.

# Note:  Change 4
# Here passing arguments to both decorator and the decorated function 'myfun()'
# Note:
# Here the decorator is a FUNCTION and NOT a CLASS.
# Decarator is receiving hard coded values here


# Decorator ##
def my_new_decor_fn(x, y):
    print("mydecor.call() called")
    print ("1. Decorator Args: ", x, y)
    def wrap(f):
        print("Function To be called: %s" %f.__name__)
        def wrapped_f(*args):      #<=== Decorated myfun() args are here
            print("Inside wrapped")
            print ("2. Decorator Args: ", x, y)
            f(*args)  # call the function here with the args
            print("return from wrapped_f")
        return wrapped_f
        print("return from wrap")
    return wrap

## Decorated function ##
@my_new_decor_fn('hello', 'world') #<<==== Decorator HARD CODED args
def myfun(a, b, c, d):   #<<===== Decorated method/function
    print("myfun() called")
    print ("Decorated Args: A : ", a, " B: ", b, " C: ", c, " D: ", d)

## Function call

myfun(2,4,6,8)

## Result
##  $ ./decorator5.py 
##  mydecor.call() called
##  1. Decorator Args:  hello world
##  Inside wrapped
##  2. Decorator Args:  hello world
##  myfun() called
##  Decorated Args: A :  2  B:  4  C:  6  D:  8
##  return from wrapped_f





