n = input()
n = int(n)

"""

if n >= 0:
    if n % 2 == 0:
        print(n, "is a positive and even number")
    else:
        print(n, "is a positive and odd number")
else:
    if n % 2 == 0:
        print(n, "is a negative and even number")
    else:
        print(n, "is a negative and odd number")
"""


if n >= 0 and n % 2 == 0:
    print(n, "is a positive and even Number")
elif n >= 0 and n % 2 == 1:
    print(n, "is a positive and odd Number")
elif n < 0 and n % 2 == 0:
    print(n, "is a negative and even Number")
else:
    print(n, "is a negative and odd Number")