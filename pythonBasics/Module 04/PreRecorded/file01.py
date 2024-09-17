
"""
# Create
with open("example.text", "w") as file:
    print("created")
"""
""" 
# write, erase and write
with open("example.text", "w") as file:
    #file.write("Hello World!")
    file.write("Hello Python")

"""
""" 
# Read

with open("example.text", "r") as file:
    content = file.read()
    print(content)
"""

# rename and delete

import os
#os.rename("example.text", "new_exmple.text")
os.remove("new_exmple.text")