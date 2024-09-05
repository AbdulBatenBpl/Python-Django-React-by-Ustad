"""
#loop in list
fruits = ["apple", "banana", "cherry", "A", "B", "C", "D"]

for eachFruit in fruits:
    print(eachFruit)
"""
from enum import unique

"""
#loop in string
word = "ostad"
for letter in word:
    print(letter)
"""

"""
#loop in integer 
for item in range(1, 101):
    print(item)
"""

"""
#loop in dictionary
all_marks = {'Math' : 98, 'stat' : 96, 'bangla' : 75, 'english' : 82}
for subject, marks in all_marks.items():
    print("{} : {}".format(subject, marks))
"""

"""
#loop in set
unique_number = {1,2,3,4,5}
for eachNumber in unique_number:
    print(eachNumber)
"""

#break and continue in loop
for num in range(10):
    if num == 3:
        continue
    if num == 8:
        break
    print(num)