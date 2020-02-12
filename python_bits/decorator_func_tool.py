 
######################################################
        # Venky, Thu Mar 26 15:58:42 2015 # 
######################################################
        

# Decorators are functions that return functions. When "passing 
# a parameter to the decorator" what you are actually doing is calling a 
# function that returns a decorator. So decAny() should be a function 
# that returns a function that returns a function.

import functools

def decAny(tag):
    print("here 1")
    def dec(f0):
        print("here 2")
        @functools.wraps(f0)
        def wrapper(*args, **kwargs):
            print("here 3")
            return "<%s> %s </%s>" % (tag, f0(*args, **kwargs), tag)
        return wrapper
    return dec

@decAny( 'xxx' )
def test2():
    print("here 4")
    return 'test1XML'


print (test2())
