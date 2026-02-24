#sets do not allow duplicate elements
#unordered collection

#create s student_id set integer type
stu_id = {112, 113, 114, 115}
print(stu_id)
#create a string type set
letters = {'a', 'b', 'c', 'd', 'e'}
print (letters)

#create a mixed set
mixed_set = {"Hello", 1,-7,8.9}
print(mixed_set)

#create an empty set
empty_set = set()

#add elements to the set
a = {2, 3, 4}
a.add(5)
print(a)

#clear
a = {2, 3, 4}
a.clear()
print(a)

#copy
a = {1, 2, 3}
b = a.copy()
print (b)

#difference
a = {1, 2, 3, 4}
b = {3, 4, 5}
print (a.difference(b))

#difference update
a = {1, 2, 3, 4}
b = {3, 4, 5}
a. difference_update(b)
print (a)

#Discard
v = {10, 20, 30, 40}
v.discard(30)
print(v)

