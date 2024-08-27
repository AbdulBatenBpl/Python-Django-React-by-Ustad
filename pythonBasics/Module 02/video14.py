from itertools import count

s = "abc"
print(type(s))
s = 'abcd'
print(type(s))
print(10 + 10)
print("10" + "10")
print("abc" + 'def')
#print(10 + "10") #invalid: int + string can't concatenate
print("10" * 3)
print("Bangadesh" * 2)

st = "abcdef"
print(len(st))
print(s[0:3])
print(s[1:2])
print(s[3])
print(s[-1])
print(s[-2])
print(s[-3])
print(s[:])

#string immutable

name = "jewel"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name)

#search in string
country = "Bangladesh"
print(country.find("Bangla"))
print(country.find("desh"))
print(country.find("ccc"))
print(country.startswith("Bangla"))
print(country.startswith("bangla"))
print(country.endswith("desh"))
print(country.endswith("desH"))


new_list = "A, B, C, D".split(",")
print(new_list)
print(new_list[2])

new = ",".join(new_list)
print(new)
print(new * 3)