year = input("Year: ")
year = int(year)


"""
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is leap year")
else:
    print(year, "is not a leap year")
"""
if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print(year, "is not a leap year")
else:
    print(year, "is leap year")