
"""
def addTwo(a, b): # a and b are parameters
    print(a + b)

addTwo(100, 400) # 100 and 400 are arguments

"""

""" 
# require parameter
# default parameter

def addTwo(a, b = 100 ): # b = 100 is default parameters
    print(a + b)

addTwo(100)
addTwo(30, 49)
"""

""" 
# variable length arguments (*args)
def printTuple(*numbers):
    for number in numbers:
        print(number)

printTuple(20, 40, -4, 3.53, "Hello", True)
"""

""" """
# key arguments
def printDct(**person):
    for key, value in person.items():
        print("{}: {}".format(key, value))

printDct(
    name = "Jewel",
    age = 34,
    city = "Benapole"
)
