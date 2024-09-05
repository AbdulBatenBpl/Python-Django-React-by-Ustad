from tabnanny import check

a = 10
b = 2.423
c = 1 + 4j
d = "Hello"
e = ["apple", "banana", "cherry"]
f = (1, 3, 5)
g = range(0, 11, 2)
h = {'name' : 'Alice', 'age' : '32'}
i = {1,3,4}
j = frozenset([1,3,5])
k = True
l = None



check = type(l)
print(check)