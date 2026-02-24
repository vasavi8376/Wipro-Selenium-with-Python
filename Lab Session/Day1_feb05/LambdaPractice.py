from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

evens = filter(lambda x: x % 2 == 0, nums)
squares = map(lambda x: x * x, evens)
print(evens)
print(squares)
print(reduce(lambda x ,y : x + y,nums))

salaries = [25000, 40000, 32000,18000]
s1 = list(filter(lambda x: x > 30000,salaries))
print(s1)

print(list(map(lambda x: x * 1.10,s1)))

print(reduce(lambda x, y : x + y, s1))

total_payout = sum(s * 1.10 for s in salaries if s > 30000)
print(total_payout)

#1.Write a Python program to sort a list of tuples using Lambda
data = [(1, 3), (4, 1), (2, 2), (5, 0)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)

#2.Write a Python program to extract year, month, date and time using Lambda.
from datetime import datetime
now = datetime.now()
extract = lambda d: (d.year, d.month, d.day, d.time())
print(extract(now))

#3️.Concatenate dictionaries to create a new one
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d3 = {"e": 5}

new_dict = {}
new_dict.update(d1)
new_dict.update(d2)
new_dict.update(d3)

print(new_dict)
