'''
    Using numpy.array() Function
    Using numpy.zeros() Function
    Using numpy.ones() Function
    Using numpy.arange() Function
    Using numpy.linspace() Function
    Using numpy.random.rand() Function
    Using numpy.empty() Function
    Using numpy.full() Function
'''
import numpy as np

#1D array
#this function creates a Numpy array filled with zeros
#By default the data type is float64
a = np.zeros(5)
print(a)

#2D arrays of zero
a_2D = np.ones((4, 3))
print(a_2D)

# using numpy.ones() Function
a = np.ones(5)
print(a)

#2D array of ones
a = np.ones((4,3))
print(a)

#using numpy.arange() Function
#the numpy.arange() function creates an array by generating a sequence of numbers based on
#it is similar to python's built-in range() function

#with only the stop
a = np.arange(10)
print(a)
#providing the start, stop and step values
a = np.arange(1, 10, 2)
print(a)

#using numpy.linespace() Function
#linespace() is used to generate numbers over a specified interval
#include the last number
a = np.linspace(1, 10,num=5,endpoint=True)
print(a)
#exclude the last number
a = np.linspace(1, 10,num=5,endpoint=False)
print(a)

#using numpy.random.rand() Function
#generates an array of the specified  shape with random values b/w o and 1
#if no argument is provided, it returns a single random float value

a = np.random.rand(5)
print(a)
#2D
a = np.random.rand(2,3)
print(a)
#3D
a = np.random.rand(2,3,4)
print(a)

#using numpy.empty() function
#2D
a = np.empty((2,3))
print(a)

#in the following example, we are using the numpy.full() to
#using numpy.full() function
a = np.full((2,3), 5)
print(a)

#numpy.eye()
#The Numpy eye() function is used to
#create a 2d array with ones on the diagonal and zeroes in all other positions

identity_matrix = np.eye((4))
print(identity_matrix)

#numpy identity - function is used to generate a square identity matrix
identity_matrix = np.eye((5))
print(identity_matrix)

#numpy.diag
#in case of 2D array, the function extracts the diagonal elements of the array
#in case of 1D array , the function creates a diagonal matrix with the elements of the array
#The diagonal values and zeroes in remaining positions

Matrix = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("Original Matrix" ,Matrix)
Diagonal_elements = np.diag(Matrix)
print("Diagonal_elements" ,Diagonal_elements)


