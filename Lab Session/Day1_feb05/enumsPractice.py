#Enumeration through List
#Q1 What is the output?
print(list(enumerate(['a', 'b', 'c'])))

print("------------")
#What is the output?
for i, v in enumerate([10, 20, 30]):
    print(i, v)

print("------------")
#Q3 Write code to print index + value from: index starts 1
colors = ['red', 'green', 'blue']
for i, v in enumerate(colors, start=1):
    print(i, v)

print("------------")
#Q4 What is the output?
print(list(enumerate("PYTHON", start=1)))

print("------------")
#Q5 Find the index of value 50 using enumerate():
nums = [10, 20, 30, 40, 50, 60]
for i, v in enumerate(nums):
    if v == 50:
        print(i)

print("------------")
#Q6 What is the output?
for i, n in enumerate(range(10, 60, 10)):
    print(i, n)

print("------------")
#Q8 What is printed?
items = ['a', 'b', 'c']
for i in enumerate(items):
    print(i)

print("------------")
#Q10 What is the output?
for i, v in enumerate([100, 200, 300], start=-1):
    print(i, v)

list(enumerate([], start=5))

