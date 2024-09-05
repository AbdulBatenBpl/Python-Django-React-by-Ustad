"""
Immutable
    -immutable objects cannot be modified after creation
    -you can reassign it, but memory location not remained same.
    -after reassign am immutable typed data, it possessed new memory location
immutable datatypes
    -integers
    -floating-point numbers
    -strings
    -tuples
    -frozenset
"""

"""
a = 8
a_location_first = id(a)
a = 10
a_location_second = id(a)
print(a_location_first)
print(a_location_second)


a = 3.53
a_location_first = id(a)
a = 4.23
a_location_second = id(a)
print(a_location_first)
print(a_location_second)


a = "Hello"
a_location_first = id(a)
a = "World"
a_location_second = id(a)
print(a_location_first)
print(a_location_second)




a = ("mango", "apple", 4, 5.55)
a_location_first = id(a)
a = ("mango", "apple", 4, 5.55, "banana")
a_location_second = id(a)
print(a_location_first)
print(a_location_second)

"""

a = frozenset([2, 5, 6])
a_location_first = id(a)
a = frozenset([1, 4, 5])
a_location_second = id(a)
print(a_location_first)
print(a_location_second)