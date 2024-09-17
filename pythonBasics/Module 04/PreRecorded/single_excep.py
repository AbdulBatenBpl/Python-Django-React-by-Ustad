
# single exception
try:
    result = 10/0
    print(result)
except ZeroDivisionError:
    print("Division by Zero")