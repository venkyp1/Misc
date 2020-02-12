 
######################################################
        # Venky, Tue Nov 17 13:24:12 2015 # 
######################################################
        

# See the order of decorators..and how they change the output

def makebold(strData):  #<== strData is a function passed as argument
    print ("makebold Data Received: ", strData)
    def wrapit():
        return "<b>" + strData() + "</b>"
    return wrapit

def makeitalic(strData):  #<== strData is a function passed as argument
    print ("makeitalic Data Received: ", strData)
    def wrapped():
        return "<i>" + strData() + "</i>"
    return wrapped



@makeitalic
@makebold
def chumma():
    return "hello chumma"


print (chumma())

# ==========================================================


# another use of decorators
# Try: Verify the login params before accepting them



