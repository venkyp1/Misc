 
######################################################
        # Venky, Thu Dec 12 21:27:51 2019 # 
######################################################


from functools import reduce

temp_c = [10, 3, -5, 25, 1, 9, 29, -10, 5]
temp_K = list(map(lambda x: x + 273.15, temp_c))
print(list(temp_K))

numbers = range(-15, 15)
less_than_zero = list(filter(lambda x: x < 0, numbers))
print(less_than_zero)

# we define a list of integers
numbers = [1, 4, 6, 2, 9, 10]
# Define a new function combine
# Convert x and y to strings and create a tuple from x,y
def combine(x,y):
  return "(" + str(x) + ", " + str(y) + ")"

# Use reduce to apply combine to numbers
from functools import reduce

print(numbers)
reduce(combine,numbers)



