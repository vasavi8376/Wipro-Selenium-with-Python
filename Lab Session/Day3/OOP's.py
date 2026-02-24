# More Examples of Constructors and Inheritance
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("------------------")

book1 = Book("Python Basics", "Guido van Rossum")
book2 = Book("Clean Code", "Robert C. Martin")
book3 = Book("Data Structures", "Mark Allen Weiss")

book1.display()
book2.display()
book3.display()

# 2nd one
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = length * width
        self.perimeter = 2 * (length + width)

    def display(self):
        print("Length:", self.length)
        print("Width:", self.width)
        print("Area:", self.area)
        print("Perimeter:", self.perimeter)

rect = Rectangle(10, 5)
rect.display()
print()
## 1Q} Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter
import math
class Circle:
    radius = 20
    def CalArea(self):
        area = math.pi * self.radius * self.radius
        print(f"Area of the Circle: {area} meters")

    def CalPerimeter(self):
        perimeter = 2 * math.pi * self.radius
        print(f"Perimeter of the Circle: {perimeter} cubic meters")

c = Circle()
c.CalArea()
c.CalPerimeter()
print()
# 2.Write a Python program to create a person class. Include attributes like name, country and date of birth.
# Implement a method to determine the person's age.
from datetime import date
class Person:
    name = "Satheesh"
    country = "India"
    DOP = 2003

    def findAge(self):
        today = date.today()
        age = today.year - self.DOP
        print(age)

p = Person()
p.findAge()
