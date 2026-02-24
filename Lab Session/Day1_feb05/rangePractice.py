a = range(5)
print(a)
for i in range(5):
    print(i)

# Range of two parameters
a = range(0, 5)
print(a[2])

# Range Function three parameters
a = range(12, 1, -1)
print(a[0])

# Range with if else statements
prices = [100, 200, 300, 400]
for i in range(len(prices)):
    if i % 2 == 0:
        print("Discount applied on ", prices[i])
    else:
        print("NO Matches")

# To check the password
pin = input("Enter the Pin")
for i in range(3):
    if pin == "1234":
        print("Password is valid!")
    else:
        print("Try Again!")

import time
for second in range(10):
    print("Second is printed", second)
    time.sleep(1)
#to find the sum of numbers from 1 to 100
def sum_numbers():
    total = 0
    for i in range(1, 101):
        total += i
    return total

print(sum_numbers())

#all numbers divisible by 5 between 1 and 100
for i in range(1, 101):
    if i % 5 == 0:
        print(i)
#list of numbers from 50 to 100 with a step of 5
numbers = list(range(50, 101, 5))
print(numbers)

#square of each number from 1 to 10
for i in range(1, 11):
    print(i, "square is", i * i)

#Print numbers between -10 and 10
for i in range(-10, 11):
    print(i)
