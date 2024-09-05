"""
age = int(input("Enter your age: "))
if age >= 18:
    print("You are a adult")
else:
    print("You are a child")
"""

marks = int(input("Enter your marks: "))
if marks <= 100 and marks >= 80:
    print("A+")
elif marks < 80 and marks >= 70:
    print("A")
elif marks < 70 and marks >= 60:
    print("A-")
elif marks < 60 and marks >= 50:
    print("B")
elif marks < 50 and marks >= 40:
    print("D")
else:
    print("F")