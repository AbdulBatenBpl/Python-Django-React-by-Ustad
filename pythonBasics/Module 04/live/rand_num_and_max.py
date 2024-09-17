import random



numbers = []
for _ in range(10):
    numbers.append(random.randint(1,100))
print(numbers)

max_num = float("-inf")
min_num = float('inf')

for n in numbers:
    if n > max_num:
        max_num = n
    if n < min_num:
        min_num = n
print(max_num)
print(min_num)