
"""
List
    - maintain order/ordered
    - mutable
    - allowed duplicate value
    - heterogeneous
    - dynamic size

list Methods
    - list.append()
    - list.insert()
    - list1.extend(list2)
    - list.remove("item")
    - list.pop()
    - list.pop(item index)
    - list.clear()
    - list.index("item")
    - list.count("item")
    - list.sort()
    - list.reverse()
    - len(list)

list slicing
list loop



"""
"""
lived_town = ["Dhaka", "Khulna", "Jashore"]
print(id(lived_town)) # check memory location for checking mutability
lived_town.append("Benapole") # append method
print(lived_town)
print(id(lived_town)) # check memory location for checking mutability
lived_town.insert(1, "Sharsha") # insert method
print(lived_town)

visited_town = ["Cox's Bazar", "Chotogram", "Sylhet"]

visited_town.extend(lived_town)

print(visited_town)
"""
""" 
fruits = ["apple", "banana", "apple", "cherry"]

fruits.remove("apple")
print(fruits)
fruits.remove("apple")
print(fruits)
"""
""" 
last_item = fruits.pop() # return last item by default
print(last_item)
print(fruits)

print(fruits.pop(0)) # return required indexed item
print(fruits)

fruits.clear()
print(fruits)



idx_num = fruits.index("cherry")
print(idx_num)


fre = fruits.count("apple")
print(fre)


fruits.sort()
fruits.reverse()
print(fruits)

"""
""" 
numbers = [4, 4, 2, 1, 3, 5, 5,9]

print(numbers)
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)


length = len(numbers)
print(length)

"""
""" 
fruits = ["apple", "banana", "apple", "cherry"]
print(fruits[0:2])
print(fruits[0:4])
print(fruits[:3])
print(fruits[3:])
print(fruits[1:])
print(fruits[1:-1])
print(fruits[-4:-1])
"""

fruits = ["apple", "banana", "apple", "cherry"]
for fruit in fruits:
    print(fruit)