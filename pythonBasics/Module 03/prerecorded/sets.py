"""
Sets
    - Unordered
    - mutable
    - No duplicate allowed
    - dynamic sized
    - Heterogeneous

Sets Methods
    - add()
    - update()
    - remove()
    - clear()
    - union()
    - intersection()
    - difference()
    - issubset()
    - issuperset()
    
"""


""" 
fruits = {"apple", "banana", "cherry", 3, 5.44, False}
#print(fruit[1]) # due to unordered, index num can't return required value
print(id(fruits))
fruits.add("mango")
print(fruits)
print(id(fruits))
"""

""" 
fruits = {"apple", "banana", "cherry", 3, 5.44, False}
fruits.add(True)
print(fruits)
fruits.update(["grape","strawberry"])
print(fruits)
fruits.remove("cherry")
print(fruits)
fruits.clear()
print(fruits)
"""
set1 = {1,2,3}
set2 = {4,5,6}
set3 = {2,3}

result1 = set1.union(set2)
print(result1)
print(id(result1))
result1 = set1.union(set3)
print(result1)
print(id(result1))
result1.add(9)
print(result1)
print(id(result1))
result1 = set1.intersection(set3)
print(result1)
result1 = set1.difference(set3)
print(result1)
print(set3.issubset(set1))
print(set1.issuperset(set3))