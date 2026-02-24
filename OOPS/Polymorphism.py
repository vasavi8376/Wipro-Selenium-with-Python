#polymorphism means taking many forms
#same method / function name will behave differently depending on the
#object type, input arguments, class implementation

#object type
print (len("python"))
print (len ([1, 2, 3] ))
print (len ({1, 2, 3}))

#input arguments no of arguments / data types
class calculator:
    def add(sel, a, b=0, c=0):
        return a+b+c
c = calculator()
print(c.add(5))
print(c.add(5, 10))
print(c.add(5, 10, 15))

#runtime polymorphism is supported
#achieved method over riding - child class method will over ride the parent class

class Animal:
    def sound(self):
        print("animal makes sound")

class Dog(Animal):
    def sound(self):
        print("animal does not make sound")

a = Dog()
a.sound()