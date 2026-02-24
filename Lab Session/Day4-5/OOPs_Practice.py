# Method Overriding with Inheritance
# Employee → Manager (Runtime Polymorphism)
class Employee:
    def calculate_salary(self):
        return 30000

class Manager(Employee):
    def calculate_salary(self):
        return 30000 + 10000   # bonus

emp = Employee()
mgr = Manager()

print(emp.calculate_salary())
print(mgr.calculate_salary())

# Lab 2: Polymorphism Using Function Arguments
class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")

class Cow:
    def speak(self):
        print("Cow moos")

def animal_sound(obj):
    obj.speak()

animal_sound(Dog())
animal_sound(Cat())
animal_sound(Cow())

# Lab 3: Multilevel Inheritance with Polymorphism

class Vehicle:
    def fuel_type(self):
        print("Generic fuel")

class Car(Vehicle):
    def fuel_type(self):
        print("Petrol or Diesel")

class ElectricCar(Car):
    def fuel_type(self):
        print("Electric")

v = Vehicle()
c = Car()
e = ElectricCar()

v.fuel_type()
c.fuel_type()
e.fuel_type()

# Lab 4: Operator Overloading

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance

    def __gt__(self, other):
        return self.balance > other.balance

acc1 = BankAccount(5000)
acc2 = BankAccount(3000)

print(acc1 + acc2)     # add balances
print(acc1 > acc2)     # compare balances

# Lab 6: Multiple Inheritance and MRO (Diamond Problem)

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

d = D()
d.show()

print(D.mro())

# Lab 7: Polymorphism with Exception Handling

class Calculator:
    def divide(self, a, b):
        return a / b

class SafeCalculator(Calculator):
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero"

calc = SafeCalculator()
print(calc.divide(10, 2))
print(calc.divide(10, 0))

# Lab 8: Real-Time Payment System (Polymorphism)

class Payment:
    def pay(self):
        pass

class CreditCard(Payment):
    def pay(self):
        print("Paid using Credit Card")

class UPI(Payment):
    def pay(self):
        print("Paid using UPI")

class NetBanking(Payment):
    def pay(self):
        print("Paid using Net Banking")


def process_payment(payment):
    payment.pay()

process_payment(CreditCard())
process_payment(UPI())
process_payment(NetBanking())
