 
######################################################
        # Venky, Tue Aug 22 20:18:30 2017 # 
######################################################
        

#This code to demonstrate ways of how a method can be added to a class instance dynamically (at run time).

from types import MethodType

class classA : pass

def funA(self, data):
  print ("data = ", data)


# Create an instance of classA

ca = classA()

# Add method to the instance (not to the class) using MethodType()
# Syntax:  instance.methodname = MethodType(methodName, instance, className)

#ca.fun = MethodType(funA, ca, classA)  # className is optional
ca.fun = MethodType(funA, ca)

# Note: Now, the method is available to the instance ONLY (not to the class). So another instance
# of the class will not have the method available.

ca.fun(100)


#  OTHER WAYS TO ADD A METHOD DYNAMICALLY   ################################

# The following adds a method to the class so the new method will be available to all its instances.
# including the objects created before adding the method.

def dynaFun(self):             # Make sure to pass 'self' as it will be a classMethod
  print ("dynaFun() called")


classA.dynaFun = dynaFun

new_ca = classA()

new_ca.dynaFun()

ca.dynaFun()  # The instance was created before adding the method. How this works??


