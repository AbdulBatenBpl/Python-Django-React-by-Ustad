"""
#convert to uppercase
text = "hello world"
print(text.upper())
"""

""" 
#convert to lowercase
text = "HELLO WORLD"
print(text.lower())
"""
""" 
#capitalize the first letter
text = "hello world"
print(text.capitalize())

"""
"""
#title case
text = "hello world"
print(text.title())
"""
"""
#swap case
text = "hello world"
text2 = "Hello World"
print(text.swapcase())
print(text2.swapcase())
"""

"""
#Replace a substring
text = "hello world"
print(text.replace("world", "python"))
"""

"""
#Split the string into a list
text = "Hello-World-in-the-world-of-python-web-development"
print(text.split("-"))'
#join a list into a string
text = ['Hello', 'World', 'in', 'the', 'world', 'of', 'python', 'web', 'development']
print(" ".join(text))
print("-".join(text))
"""

"""
#strip whitespace from both ends
text = "   hello world   "
print(text)
print(text.strip())

"""

text = "   hello world   "
#remove leading whitespace
print(text.lstrip())
#remove trailing whitespace
print(text.rstrip())