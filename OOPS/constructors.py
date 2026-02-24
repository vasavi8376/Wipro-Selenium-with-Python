#Constructors - first function of the class called, when an object of the class is created
#syntax - __init__()
# we can parametrise the constructor
#self is mandatory here
class Student:
    def __init__(self):
        print("Constructor is called")
    def addsum(self):
        print("Adding 2 numbers")
s1 = Student()
s1.addsum()

#parametrised constructor
#self.name is a instance variable or a global variable(belong to the object
#name is a local parameter(exists inside the method)
#if we dont assign it to the self.name the object will not remember the value
class Employee:
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(self.name, self.salary)
e1 = Employee("vasavi", 40000)
e2 = Employee("vivek", 98765)
e1.display()
e2.display()

##constuctor overloading is not supported
#using * arguments  in constructor
#constuctor overloading is supported by *arg keyword
#we can any numer of parameters to the constructor using *args
class Numbers:
    def __init__(self, * args):
        self.values = args
n = Numbers(10, 20, 30)
print(n.values)

m = Numbers(3, 4)
print(m.values)

# parent and child constructors
#super keyword fro constructors for accessing parent constructor

class parent:
    def __init__(self):
        print("I am the parent constructor")
class child(parent):
    def __init__(self):
        super().__init__()# if we want to call parent constructor we have to call with super()
        print("I am the child constructor")

c = child()
