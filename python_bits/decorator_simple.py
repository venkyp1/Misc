 
######################################################
        # Venky, Tue Aug 23 13:58:48 2016 # 
######################################################
        

# NOTE: When the decorator is not taking any arguments, there is only one wrapper in the
# decorator. If the decorator takes arguments, there is a need for another wrapper to
# receive those arguments.

# Also, the nested functions are written in such a way, the outer method calls the
# inner method and the inner most will call the 'function' that needed to be called.

#-----------

def wrap_with_prints(fn):      #  <<==  Function name here
    # This will only happen when a function decorated
    # with @wrap_with_prints is defined
    print('wrap_with_prints runs only once')
    print("Function to be called: %s " %fn.__name__)
 
    def my_wrapper(data):         # <<== Function arguements here
        # This will happen each time just before
        # the decorated function is called
        print('About to run %s' % fn.__name__)
        # Here is where the wrapper calls the decorated function
        fn(data)                #  <<===  Call the function here
        # This will happen each time just after
        # the decorated function is called
        print('Done running %s' % fn.__name__)
 
    return my_wrapper
 
@wrap_with_prints
def func_to_decorate(dataV):
    print('Running the function that was decorated.')
    print ("Data Received:", dataV)


##### Call ####

for i in (range(10)):
   func_to_decorate(i)



### another simple form  ###

print ("-------------------------------------------------------")

def my_decorator(f):
   def wrapper(x,y):
       print("Doing prework ....")
       print("Args: ", x, y)
       f(x,y)
   return wrapper
   

@my_decorator
def my_method(param1, param2):
    print ("Add: ", param1+param2)

##### Call ####

my_method(100,200)



### aother form of decorator ###
print ("-------------------------------------------------------")

def my_dec(d_arg1, d_arg2):  #<--- Decorator args are passed here
  print ("Args passed to decorator: ", d_arg1, d_arg2)
  def my_wrap(fn):                # <<----- function name(my_function) gets passed here
       def wrapper(x, y):
          print("In wrapper")
          fn(x,y)    #<-- calls the function
       return wrapper  #<---- Calls inner function
  return my_wrap  #<--- Calls inner function

@my_dec(5555, 9999)
def my_function(m, n):
    print ("Add: ", m + n)

my_function(10,20)


### Chaining of decorators ###
print ("-------------------------------------------------------")

# NOTE:  when decorators are chained, the inner most decorator is called first.
#  it passes the inner method as a parameter to the next outer decorator and so on.
#  make sure to pass the CORRECT arguments for the chained decorators to work.

# TIP:  Use f.__name__ internal variable to print wich function is getting called
# to make sure the arguments are correct.


def first_dec(fn):
  print ("first decorator called")
  def my_wrap(x, y):
     print ("1. Calling function: ", fn.__name__)
     fn(x,y)
  return my_wrap

def second_dec(d_arg1, d_arg2):  #<--- Decorator args are passed here
  def my_wrap(fn):                # <<----- function name(my_function) gets passed here
       print ("Args passed to decorator: ", d_arg1, d_arg2)
       print ("2. Calling function: ", fn.__name__)
       def wrapper(x, y):
          print("In wrapper")
          fn(x,y)    #<-- calls the function
       return wrapper  #<---- Calls inner function
  return my_wrap  #<--- Calls inner function


@first_dec
@second_dec(222, 777)
def callme_last(m, n):
    print ("Add: ", m + n)

##  call here #####


callme_last(10,20)


