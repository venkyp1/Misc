 
######################################################
        # Venky, Wed Mar 11 09:12:34 2015 # 
######################################################
        

# In python functions can use 'keyword arguments' 
# which does not even have to specify the arguments
# but while calling pass the arguments with values.
# The key args should have '**' in the function definition

# IMPORTANT: In key-value args, ORDER of the arguments DOES NOT matter
# All data will go into a Hash or Dictionary data
# Note: The keyword values are provided as part of the function call. 
# The values defined in the function defintion are DEFAULT values.


def func(**kwargs):
    print (kwargs)

def func_def(x=22, y=88, **kwargs):   ## first 2 params are with default values
    print ("In: func_def()")
    print (kwargs)
    print ("X = ", x, " y= ", y)

def venky_func(**venky):
    print ("In: venky_func()")
    print (venky)


def venky_nokey(x=10, y=12):
    print ("In: venky_nokey()")


## MAIN


func(a=10, b=100)
func()  # passing NO key args

func_def(98.8, 23.7, a=10, b=100)  #Gets passed to key-value args as Dict type

venky_func(y='yes', n='no')

venky_nokey(a='yes', b='no')  # Causes TypeError as no '**keyargs' defined


