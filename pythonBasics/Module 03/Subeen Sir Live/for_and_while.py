"""
def add_1_to_n(n):
    result = 0

    for x in range(1, n+1):
        result = result + x

    return result

n = int(input("Enter a number: "))

while n != 0:
    r = add_1_to_n(n)
    print(r)
    n = int(input("Enter a number: "))

"""

n = int(input("Enter a number: "))

while n != 0:
    r = 0
    for i in range(1, n+1):
        r = r + i
    print(r)
    n = int(input("Enter a number: "))