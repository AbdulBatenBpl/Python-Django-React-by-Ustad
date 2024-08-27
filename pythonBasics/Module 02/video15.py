
def multiplication_table(n):
    for i in range(1, 11):
        print("{} x {} = {}".format(n, i, n * i))


n = input("Enter a number (0 to exit): ")
n = int(n)

while n != 0:
    multiplication_table(n)
    print("")
    n = input("Enter a number (0 to exit): ")
    n = int(n)

