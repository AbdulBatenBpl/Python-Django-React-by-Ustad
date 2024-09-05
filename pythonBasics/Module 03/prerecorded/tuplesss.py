"""
Tuples
    - ordered
    - allow duplicates
    - heterogeneous
    - fixed sized
    - immutable
Tuples methods:
    - count()
    - index()

Tuples can be converted into list
Tuples can be sliced as list
Tuples items can be iterate by loops
"""
""" 
numbers = (1,2,3,2,3,4,5,6,7)
num_count = numbers.count(1)
print(num_count)
num_count = numbers.count(2)
print(num_count)
"""
""" 
numbers = (1,2,3,2,3,4,5,6,7)
num_index = numbers.index(2)
print(num_index)
"""
""" 
numbers = (1,2,3,2,3,4,5,6,7)
num_list = list(numbers)
print(num_list)
"""
""" 
fruits = ("apple", "banana", "apple", "cherry")
print(fruits[0:2])
print(fruits[0:4])
print(fruits[:3])
print(fruits[3:])
print(fruits[1:])
print(fruits[1:-1])
print(fruits[-4:-1])
"""

fruits = ("apple", "banana", "apple", "cherry")
for fruit in fruits:
    print(fruit)