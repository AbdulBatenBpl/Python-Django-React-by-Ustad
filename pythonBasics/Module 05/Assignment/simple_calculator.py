"""
function for: to check valid input
"""
def valid_num(a):
    try:
        return float(a)
    except (ValueError, TypeError):
        print("Invalid input. Try again")
        return None
"""
function for: sumation of two number and print it
"""
def sum_two_number():
    a = input("Enter first number: ")
    x = valid_num(a)
    if x == None:
        return
    b = input("Enter second number: ") 
    y = valid_num(b)
    if y == None:
        return
    z = x + y
    #if z%1 == 0:
        #z = int(z)
    print("Addition: {} + {} = {}".format(x, y, z)) 

"""
function for: substraction of two number and print it
"""
def subtract_two_number():
    a = input("Enter first number: ")
    x = valid_num(a)
    if x == None:
        return
    b = input("Enter second number: ") 
    y = valid_num(b)
    if y == None:
        return
    z = x - y
    #if z%1 == 0:
        #z = int(z)
    print("Subtraction: {} - {} = {}".format(x, y, z)) 
"""
function for: multiply of two number and print it
"""
def multiply_two_number():
    a = input("Enter first number: ")
    x = valid_num(a)
    if x == None:
        return
    b = input("Enter second number: ") 
    y = valid_num(b)
    if y == None:
        return 
    z = x * y
    #if z%1 == 0:
        #z = int(z)
    print("Multiplication: {} x {} = {}".format(x, y, z))
"""
function for: division of two number and print it
"""
def divide_two_number():
    a = input("Enter first number: ")
    x = valid_num(a)
    if x == None:
        return
    b = input("Enter second number: ") 
    y = valid_num(b)
    if y == None:
        return 
    try:
        z = x / y
        #if z%1 == 0:
            #z = int(z)
        print("Dividation: {} / {} = {}".format(x, y, round(z, 1)))
    except ZeroDivisionError:
        print("Can't divide by Zero!")

"""
function for: modulus of two number and print it
"""
def modulus_of_two_num():
    a = input("Enter first number: ")
    x = valid_num(a)
    if x == None:
        return
    b = input("Enter second number: ") 
    y = valid_num(b)
    if y == None:
        return 
    z = x % y
    #if z%1 == 0:
        #z = int(z)
    print("Modulus: {} % {} = {}".format(x, y, z))
"""
function for: validate and navigate of user input of operation choice of users
"""
def user_input():
    print("Select operation:")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. divide")
    print("5. Modulus")
    opt = input("Enter choice(1/2/3/4/5): ")
    try:
        opt = int(opt)
    except ValueError:
        print("Invalid choice. Please enter a number from 1 to 5")

    if opt == 1:
        sum_two_number()
    elif opt == 2:
        subtract_two_number()
    elif opt == 3:
        multiply_two_number()
    elif opt == 4:
        divide_two_number()
    elif opt == 5:
        modulus_of_two_num()
    else:
        print("Invalid Input! Please try again.")
        return 
        
         
      
print("Simple Calculator: Welcome.")
user_input()