
'''
1. Positional arguments will have a '*' in the function def
2. Positional arguments will store all of the positional arguments
    passed to the function
positional arguments should be first and keyword-value args should be
last
3. Any number of arguments can be passed as positional args

venky, 10/8/16

'''

def func(*positional):
    print (positional)
    y=0
    for x in positional:  # positional is like a Tuple
        print (y,". ", x)
        y+=1

def check(*positional):
    print (positional[0])
    print (positional[1])
    print (positional[2])
    


#Both positional and key-word args
def func_def(*positional, **kwargs):
    print ("In: func_def()")
    print (positional)
    print ("X = ", x, " y= ", y)


func('a', 'b', 'c')
func()  # passing NO positional params
check('a', 'b', 'c')
