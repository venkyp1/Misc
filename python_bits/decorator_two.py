 
######################################################
        # Venky, Wed Mar 11 11:20:52 2015 # 
######################################################
        

# See the order of decorators..and how they change the output

def makebold(strData):
    print ("makebold Data Received: ", strData)
    def wrapped():
        return "<b>" + strData() + "</b>"
    return wrapped

def makeitalic(strData):
    print ("makeitalic Data Received: ", strData)
    def wrapped():
        return "<i>" + strData() + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello world!"



@makeitalic
@makebold
def chumma():
    return "hello chumma"


print (hello())
print (chumma())


# Results:
#  <b><i>hello world!</i></b>
#  <i><b>hello chumma</b></i>

