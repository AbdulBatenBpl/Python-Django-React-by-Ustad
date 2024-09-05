"""
#string repeation
name = "Ustad "
repeat = name * 10
print(repeat)

"""

#string concatenation
str1 = "Hello "
str2 = "World"
combine = "".join([str1,str2])
combine2 = "".join([str1, str2]) + "!"
combine3 = "{} {}!".format(str1, str2)
combine4 = "%s %s!" %(str1, str2)

print(combine)
print(combine2)
print(combine3)
print(combine4)