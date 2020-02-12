 
######################################################
        # Venky, Mon Nov  4 19:14:59 2019 # 
######################################################
        

#------------------------------------------------------

print "Closure sample")

# Closures look more like the decorator function.
def sample_closure(n):
    print ("Outer Received: ", n)
    def add_num(x):
        print ("Inner Received  ", x)
        return (x+n)
    return add_num


fn = sample_closure(100)

print ("Result: ", fn(500))

#------------------------------------------------------
print ("Decorator sample ... using closure")
def dec_fun(f):
    print ("Here 1")
    def runme():
        print ("Do this first")
        f()
        return ("All Done")
    return runme


@dec_fun
def simple_fun():
    print ("Called here")
    
print (simple_fun())


#======================================================

print ("Generator sample")

def mk_even_list(val):
    for i in range(val):
        if i%2 == 0:
            yield i

x = mk_even_list(20)
print (list(x))
print (list(range(10)))


