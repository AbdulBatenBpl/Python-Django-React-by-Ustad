#function return

"""
def addTwo(a, b):
    num1 = a
    num2 = b
    sum = num1 + num2
    return sum
x = addTwo(10, 20)
print(x)

"""
""" 
#return multiple value. by default multiple values return as tuple
def returnTuple(a, b):
    sum = a + b
    sub = a - b
    div = a / b
    mul = a * b
    #return sum, sub, round(div, 2), mul #return as tuple
    #return [sum, sub, round(div, 2), mul] #return as list
    return {"sum": sum, "sub": sub, "div":round(div, 2), "mul": mul}

x = returnTuple(10, 3)
print(x)
"""

# using return for early exit

def first_even_number(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number
    return None
print(first_even_number([1,2,3,4,5,6,7,8,9]))
print(first_even_number([1,3,5,7,9]))