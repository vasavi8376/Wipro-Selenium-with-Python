#lamda function anonymous (nameless) functions, one line, for simple operations,
#syntax lamda arguments :expressions
# it can have any no of arguments
#must have only one expression
# the expression is automatically returned

#normal function of add 2 numbres
def add(a, b):
    return a+b
print (add(5, 3))

#lamda function
add = lambda a, b: a+b
print(add(5, 3))

#square of a number '
square = lambda x : x*x
print(square(5))

#even or odd
num = int(input("enter the number"))
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(num))

