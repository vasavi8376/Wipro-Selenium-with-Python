#iter() method - built in method

a = [10, 20, 30, 40, 50]

#convert list into iterator
iterator = iter(a)
#naxt () allow the user to access the elements
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#convert the string to the iterator
s = "hello"
iterator = iter(s)
print(next(iterator))
print(next(iterator))
print(next(iterator))
#convert the dict to a iterator
a = {'a': 1, 'b': 2, 'c': 3}
iterator = iter(a)
print(next(iterator))
print(next(iterator))
# for loop to iterate
for key in iterator:
    print(key)

a = {'a': 1, 'b': 2, 'c': 3}
for key,value in a.items():
    print(key, "->", value)

#iter(callable, sentinel)
def get_input():
    return input("Enter value":)
for value in iter(get_input, "quit"):

#lambda function
#filter failed test cases
atus = ['pass']