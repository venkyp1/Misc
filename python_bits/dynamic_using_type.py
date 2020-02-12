 
######################################################
        # Venky, Thu Aug 11 09:21:28 2016 # 
######################################################
        

# In python, type() is a class which can be use to create other classes dynamically.
# In fact, the classes are internally considered as objects.



def sampledata(self,data):  # Note: the 1st argument is 'self'
  print ("data = ", data)

# Lets create a Base class dynamically using type()

BaseClass = type('BaseClass',(),{})

# Lets create  child class from the base class and add sampledata() method to it.

# Note: The syntax for the below type() is
# classname = type('classname',TupleOfBaseclass,keywordArgs_For_Params)

ChildClass = type('ChildClass',(BaseClass,),{'sampledata':sampledata})

# Create an instance of ChildClass

child = ChildClass()

# Call the method

child.sampledata(100)


