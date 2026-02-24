#function is a block of code that performs specific code
#def function name

def printdata():
    print("Hello world")

#call the function
printdata()

#functions with parameters
def printdata(name):
    print("Hello", name)

#pass the argument
printdata("Tina")
printdata("Rita")

#return statements
#to return the function value return statement is used

def sq(num):
    result = num * num
    return result

square =sq(3)
print('square:',square)

#function pass
def func_pass():
    pass

#call the function
func_pass()

#multiple return values

def cal(a,b):
    return a-b,a+b,a*b

add, sub, mul = cal(10,5)
print(add)
print(sub)
print(mul)

#function calling a another function

def areaofrect(len, width):
    return len*width

def areaofsq(side):
    return side*side

value = areaofrect(4,6)
sq= areaofsq(value)
print(sq)

#function with a loop
def even(limit):
    for i in range(2, limit +1, 2):
        print(i)

even(10)

#with if else cod
def even(limit):
    if limit %2==0:
        return "even"
    else:
        return "odd"

print(even(10))
print(even(11))

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Example
nums = [10, 20, 30, 40]
print(sum_list(nums))


















