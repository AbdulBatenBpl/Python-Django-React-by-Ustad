
numbers = [1,3,6,4,8,9,10,2,5,11]

""" 
max_number = max(numbers)
print(max_number)
"""
# linear search
max_num = float('-inf')
for n in numbers:
    if n > max_num:
        max_num = n
print(max_num)

