 
######################################################
        # Venky, Mon Apr  6 14:25:54 2015 # 
######################################################
        

def apply(f, n):
    print(f(n))

# Create two lambdas.
square = lambda n: n * n
cube = lambda n: n * n * n

# Pass lambdas to apply method.
apply(square, 4)
apply(cube, 3)



