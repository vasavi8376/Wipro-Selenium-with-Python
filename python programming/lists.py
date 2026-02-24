empty_list = []
numbers = [1, 2, 3, 4]
mixeddata = [1, "hello", True, 6.67, 1]
nested = [[1,2], [3,4]]

#accessing the list elements indexing concept
print(mixeddata[1])
print(mixeddata[2])

#modifying the data
mixeddata[4] = 6
print(mixeddata)

#add elements # insert at index
mixeddata.insert(0, 10)
print(mixeddata)

#remove elements
mixeddata.remove("hello")
print(mixeddata)
mixeddata.pop() #last element
print(mixeddata)
mixeddata.pop(1) #by index
print(mixeddata)

#ascending order
print(numbers.sort())
print(numbers.reverse())
print(numbers.count(3))
print(numbers.index(3))
numbers.clear()

fruits = ["apple", "banana", "cherry"]
for item in fruits:
    print(item)

for i, fruit in enumerate(fruits):
    print(i, fruit)

#slicing - access a portion of list
my_list = [ 'p', 'r', 'o', 'g', 'r', 'a', 'm']
print("my_list =", my_list)

#get the list with items from index 2 to 5
print(my_list[2: 5])

#from index 5 to last
print(my_list[5: ])

#from first item to last item
print(my_list[:])

#extends
numbers = [1, 3, 5]
even_numbers = [2, 4, 6]

#adding elements of one list to another
numbers.extend(even_numbers)
print(numbers)


