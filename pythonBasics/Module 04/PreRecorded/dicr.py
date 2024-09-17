"""
# Creating a directory

import os

os.mkdir("new")
os.mkdir("new_two")

with open("new/test.txt", "w") as file:
    file.write("Hello World!")
"""
""" 
# Reading a Directory

import os

dir_items = os.listdir(".")
print(dir_items)

"""
""" 
# Rename Directory
import os
os.rename("new_two", "new_one")
"""

""" """

# make and remove directory and file

import os
""" 
os.mkdir("text")
with open("text/hi.txt", "w") as file:
    file.write("Hello Prithibi!")
"""

""" 
os.remove("text/hi.txt")
os.rmdir("text")
"""

file_list = os.listdir("new")
print(file_list)
