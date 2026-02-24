students = {
    1: "Satheesh",
    2: "Anil",
    3: "Suresh"
}
print(students)

print(students.get(2))
print(students.get(3))
#Does not exist
print(students.get(4))

students[2] = "Rahul"
print(students)

del students[3]
print(students)

students.pop(1)
print(students)

print(len(students))

print(students.keys())

print(students.values())

print(students.items())

#Using the for Loop
for roll, name in students.items():
    print(roll,": ", name)

#Iterator
d = {'a': 1, 'b': 2, 'c': 3}
iterator = iter(d)
print(next(iterator))
print(next(iterator))

# Iteration with sentinel iter(callable, sentinel)

def get_input():
    return input("Enter value:")

for value in iter(get_input, "quit"):
    print("You entered: ", value)

print("Loop Ended")

