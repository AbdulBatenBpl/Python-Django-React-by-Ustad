"""
#Simple greetings program
name = input("Enter your name: ")
#print("Hello "+ name +"!")
print("Hello {} !".format(name))

"""
"""
#simple sum calculator

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

num1 = int(num1)
num2 = int(num2)

sum = num1 + num2

print("The sum is: ",sum)

"""


"""
#Tempareture Converter

celsius = input("Enter Celsius: ")
celsius = float(celsius)

fahrenheit = (celsius * 9/5) + 32

print(fahrenheit)
"""

principal = input("Enter the principal amount: ")
rate = input("Enter the rate of interest: ")
time = input("Enter the time (in years): ")

principal = float(principal)
rate = float(rate)
time = float(time)

interest = (principal * rate * time)/100
print("Interest amount is: {}".format(interest))
