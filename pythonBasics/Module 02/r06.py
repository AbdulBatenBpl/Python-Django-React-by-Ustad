"""
Mutable Data Types
    -mutable objects can be modified after creation
    -if you reassign it, memory location remained same.
    -after reassign a mutable typed data, it possessed same memory location
Mutable datatype:
    -Lists
    -Dictionaries
    -Sets
"""
"""
l = [1, 4, 5]
first_location = id(l)

l[0] = 4
second_location = id(l)

print(first_location)
print(second_location)


l = {'a' : 1, 'b' : 2}
first_location = id(l)

l['b'] = 3
second_location = id(l)

print(first_location)
print(second_location)
"""

l = {1, 2, 3}
first_location = id(l)

l.add(4)
second_location = id(l)

print(first_location)
print(second_location)