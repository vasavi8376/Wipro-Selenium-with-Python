#Printing the Largest Number:

nums = [10, 45, 23, 89, 12]
print(max(nums))

#Using the Loops
largest = nums[0]

for n in nums:
    if n > largest:
        largest = n

print(largest)

#Printing the Odd Numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8]
odd_nums = []

for n in nums:
    if n % 2 != 0:
        odd_nums.append(n)

print(odd_nums)

#Multiplying each number in a list
nums = [1, 2, 3, 4]
result = 1
for n in nums:
    result *= n

print(result)

