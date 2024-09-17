"""
# here x and y declared in function is a local variable.
# its can't access outside of function (scope) block.
def myFun():
    x = 10
    y = 20
    print(x+y)

myFun()
#print(x+y) # x and y is local variable, so can't access from here.
"""
""" 
# global variable

x = 10
y = 30

def myFun():
    print(x+y)

myFun()
print(x+y)
"""

