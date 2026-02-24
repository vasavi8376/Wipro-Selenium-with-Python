#integer as a key
my_dict = {1: "one", 2: "two", 3: "three"}
print(my_dict)

my_dict = {1: "four", 2: "two", 3: "three", 1: "one"}
print(my_dict)

#tuples as a key
my_dict = {(1,2): "one two" ,3:"three"}
print(my_dict)
my_dict = {(1,2): "one two" ,3:"three",1: "one"}
print(my_dict)

country = {"India": "Delhi", "Canada": "Ottawa", "England": "London"}
print(country)

#remove elements
del country["India"]
print(country)

#list as a key
my_dict ={1:"one", 2:"two",3:"three", 1:"four"}
print(my_dict)

#pop as a key
student = {
    "name": "vivek",
    "age": 21,
    "course": "Python"
}
result = student.pop("age")
print(student)

#update
student = {"name": "Vasavi", "age": 21}
student.update({"course": "Python"})
print(student)

#keys
student = {
    "name": "Vasavi",
    "age": 21,
    "course": "Python"
}
a= student.keys()
print(a)

#values
student = {
    "name": "Vasavi",
    "age": 21,
    "course": "Python"
}

k = student.values()
print(k)

#copy
student = {
    "name": "Vasavi",
    "age": 21,
    "course": "Python"
}

k = student.copy()
print(k)

#dict inside the list
student = [{"id": 1, "name": "harsha", "role": "QA"}, {"id": 2, "name": "harsha", "role": "dev"}, {
