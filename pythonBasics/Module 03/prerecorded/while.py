"""
# while in list
fruits = ["apple", "orange", "banana"]

index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1
"""

""" 
#while in string
word = "Bangladesh"
idx = 0
while idx < len(word):
    print(word[idx])
    idx += 1
"""

""" 
#while in int range
index = 1
end = 11
while index < end:
    if index == 6:
        index += 1 # just want to skip print index but to continue we have to increment index
        continue
    if index == 9:
        break
    print(index)
    index += 1
    
"""
""" 
# while in dictionary
all_marks = {'Math' : 98, 'stat' : 96, 'bangla' : 75, 'english' : 82}
keys = list(all_marks.keys())
#print(keys)
index = 0
while index < len(keys):
    each_key = keys[index]
    print("Subject: "+ each_key+ "Marks: "+ str(all_marks[each_key]))
    index += 1
"""
""" """
#while in set
my_set = {1,2,3,4,5}
my_list = list(my_set)

index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1