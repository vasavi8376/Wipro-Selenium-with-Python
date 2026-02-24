#runtime errors which will disrupt the norma;program flow
#benefits
#helps in debugging
#prevents program crashing
#handling errors and exceptions in the code

#try except

# try- code tp be excuted


try:
    a = int(input("enter the number"))
    b = int(input("enter the number"))
    print(a/b)
except ZeroDivisionError:
        print("Cannot divide by zero")
except ValueError:
        print("Please enter the valid numbers")

#generic
try:
    a=10/2
except Exception as e:
    print(e)
else:
    print("Division Succesfull")
finally:
    print("close the browser")

#custom exceptions - create our own exceptions

age= int(input("Enter the age"))
if age<18:
    raise ValueError("Age must be 18 or above")


















