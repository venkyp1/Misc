 
######################################################
        # Venky, Tue Jul 26 09:08:32 2016 # 
######################################################
        

#note: map() takes 2 arguments
# The first one is a function 
# The second is an iterable sequence (list, tuple or string)

# Usage:  map(aFunction, aSequence)

# Why and where we need map() ?

# problem:

# E.g: To find a (n**n) which is exponent of each item in a list
# A list [1,2,3,4,5] will print [1,4,27,256,3125]

#>>> x=[1,2,3,4,5]
#>>> def f(n):
#...     return (n**n)
#... 
#>>> l=[]
#>>> l=list(map(f,x))
#>>> print (l)
#[1, 4, 27, 256, 3125]
#>>> 

#Another example to multiply each item with 25

data = [2,4,5,8,9]

def multi(d):
    return (d * 25)

result = []
result = list(map(multi, data))
print (result)

#Result:  [50, 100, 125, 200, 225]

## Note, we have a function defined just for the purpose of using 
# with map() function.
# Here, we can actually eliminate the function definition with an
# anonymous function defined using lambda()


data = [2,4,5,8,9]
result = []
result = list(map((lambda x: x * 25), data))
print (result)

#Result: [50, 100, 125, 200, 225]

#---------------------------

res = []
res = list(map((lambda x: x * 25), range(10)))
print (res)

#res: [0, 25, 50, 75, 100, 125, 150, 175, 200, 225]


##  CHECK THIS ONE ###
## Uses 2 lists and produces a list with x1^x2

x1 = [2,3,4,5,6]
x2 = [5,10,15,20,25]
x12=list(map(pow, x1, x2))
print(x12)

#Result: [32, 59049, 1073741824, 95367431640625, 28430288029929701376]

#---------------------------

def multiply(a, b):
  return a*b

l1 = [1,2,3,4,5,6]
l2 = [2,4,6,8,9,10]

newl1 = list(map(multiply, l2, l1)) #Arguements must support iteration

print newl1

#---------------------------
