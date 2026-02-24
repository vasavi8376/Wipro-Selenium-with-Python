import re

# Q1. Create a Car class with attributes brand, model, price.
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

car = Car("Toyota", "Camry", 3000000)
print("Q1 OUTPUT:", car.brand, car.model, car.price)


# Q2. Create a Student class with method get_grade() based on marks.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        return "Fail"

s = Student("Vijay", 82)
print("Q2 OUTPUT:", s.get_grade())


# Q3. Create a BankAccount class with deposit() and withdraw() methods.
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
print("Q3 OUTPUT:", acc.balance)


# Q4. Write a class Employee that initializes name, id, salary using __init__.
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

emp = Employee("Vijay", 101, 50000)
print("Q4 OUTPUT:", emp.name, emp.emp_id, emp.salary)


# Q5. Create a class that counts how many objects are created.
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
print("Q5 OUTPUT:", Counter.count)


# Q6. Create a class Company with a class variable company_name.
class Company:
    company_name = "Wipro"

print("Q6 OUTPUT:", Company.company_name)


# Q7. Implement a static method to validate email format.
class Validator:
    @staticmethod
    def validate_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(pattern, email))

print("Q7 OUTPUT:", Validator.validate_email("test@gmail.com"))


# Q8. Create a base class Vehicle and derived class Bike.
class Vehicle:
    def start(self):
        print("Vehicle started")

class Bike(Vehicle):
    pass

b = Bike()
print("Q8 OUTPUT:")
b.start()


# Q9. Create Person → Employee → Manager (multilevel inheritance).
class Person:
    def info(self):
        print("Person Info")

class Employee2(Person):
    def info(self):
        print("Employee Info")

class Manager(Employee2):
    def info(self):
        print("Manager Info")

m = Manager()
print("Q9 OUTPUT:")
m.info()


# Q10. Override a method in child class and call parent method using super().
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

d = Dog()
print("Q10 OUTPUT:")
d.sound()


# Q11. Create a class BankAccount with private balance.
class SafeBankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

sacc = SafeBankAccount(2000)
print("Q11 OUTPUT:", sacc.get_balance())


# Q12. Use getter and setter methods to update balance safely.
class SafeAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount

a = SafeAccount(1000)
a.set_balance(1500)
print("Q12 OUTPUT:", a.get_balance())


# Q13. Prevent negative salary using property decorators.
class Worker:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self._salary = value
        else:
            print("Salary cannot be negative")

w = Worker(50000)
w.salary = -100
print("Q13 OUTPUT:", w.salary)


# Q14. Create a Shape class with method area(). Implement Circle and Rectangle.
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

class Rectangle(Shape):
    def area(self):
        return 4 * 6

print("Q14 OUTPUT:", Circle().area(), Rectangle().area())


# Q15. Demonstrate method overloading using default arguments.
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print("Q15 OUTPUT:", calc.add(10), calc.add(10, 20), calc.add(10, 20, 30))


# Q16. Demonstrate operator overloading (__add__).
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)
print("Q16 OUTPUT:", n1 + n2)


# Q17. Create Engine class and use it inside Car class.
class Engine:
    def start(self):
        print("Engine started")

class CarWithEngine:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print("Car started")

print("Q17 OUTPUT:")
c = CarWithEngine()
c.start_car()


# Q18. Create Team class that contains multiple Player objects.
class Player:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def show_players(self):
        for p in self.players:
            print(p.name)

team = Team("India")
team.add_player(Player("Virat"))
team.add_player(Player("Rohit"))
print("Q18 OUTPUT:")
team.show_players()
