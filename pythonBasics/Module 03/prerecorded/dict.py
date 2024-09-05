"""
Dictionary
    - unordered
    - mutable
    - Key uniqueness
    - Heterogeneous
Methods
    - keys()
    - items()
    - values()
    - update()
    - pop()
    - clear()
    - get()

"""
person = {
    "name" : "Baten",
    "age" : "32",
    "occupation" : "student",
    "city" : "Jashore",
    "isBangladeshi" : True
}
""" 
print(person)
print(person["name"])

print(person.get("age"))
print(id(person))
person.update({"name":"Jewel"})
print(id(person))
print(person)
"""

print(person.keys())
print(person.values())
print(person.items())
person.update({"age":34})
print(person)
user_city = person.pop("city")
print(user_city)
print(person)
print(person.get("isBangladeshi"))
person.clear()
print(person)