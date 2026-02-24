"""
1.Write a Python function to sum all the numbers in a list.

2.Write a Python function to find the maximum of three numbers.

"""
def findMax(a,b,c):
    if a >= b and a >= c :
        print(a,"is Greater")
    elif b >= a and b >= c :
        print(b,"is Greater")
    else:
        print(c,"is Greater")
findMax(4,8,1)

# Sum of the Numbers
def sumList(numbers):
    t = 0
    for num in numbers:
        t += num
    return t

print(sumList([1, 2, 3, 4, 5]))

#Finding the Prime Number
def findPrime(num):
    if num <= 1:
        return 0

    for i in range(2, int(num ** 0.5)):
        if num % i == 0:
            return 0

    return 1

print(findPrime(5))
print(findPrime(10))

# Modules
