""" """

# Check if string starts or ends with a substring
text = "Hello World"
print(text.startswith("Hello"))
print(text.endswith("World"))

#find the position of a substring
print(text.find("World"))

#count occurrences of a substring
print(text.count("o"))

#check all characters are alphanumeric
print(text.isalnum())

#check all characters are alphabetic
print(text.isalpha())

#check all characters are digit
print(text.isdigit())
num = "21"
print(num.isdigit())

#check string only contain whitespaces
space = "    "
print(space.isspace())

#check string is in titlecase
print(text.istitle())

