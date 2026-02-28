import numpy as np
#changing shape

#reshape
a = np.arange(1,7)
print("Original array", a)

#reshape the array
reshaped = a.reshape(2, 3)
print(reshaped)

#flat = return a 1D iterator over the array
arr = np.array([[1,2], [3,4]])
for x in arr.flat:
    print(x)

#flatten - returns a copy of the array collapsed into one dimension
arr = np.array([[1,2], [3,4]])
print(arr)
at_arr = arr.flatten()
print(at_arr)

#ravel() - returns a flattened string
arr = np.array([[1,2], [3,4]])
print(arr)
at_arr = arr.ravel()
print(at_arr)

#pad() - returns a padded array with shape increased according to the pad_width
arr = np.array([1,2,3])
padded = np.pad(arr, 2, mode='constant')
print(padded)


''' Transpose operations
1   transpose
Permutes the dimensions of an array
2   ndarray.T
 as self.transpose()
3   rollaxis
Rolls the specified axis backwards
4   swapaxes
Interchanges the two axes of an array
5   moveaxis()
Move axes of an array to new positions
'''

#1  transpose
# reorders the dimensions of an array.
# rows will become the columns

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.transpose()
print(transpose)

#2 ndarray.T
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.T
print(transpose)

#rollaxis - Rolls the specified axis backwards

arr = np.zeros((2,3,4))
print(arr)

# 2 is the blocks - axis 0
# 3 - rows - axis 1
# 4 columns - axis 2

#(0,1 ,2) - (2,3,4)
#(2,0,1) - (4,2,3)

#arr[block][row][column]

new_arr = np.rollaxis(arr, 2)
print(new_arr)

#swapaxes() - Interchanges two axes of an array.
#$Axis 0 and Axis 2 swapped.
arr = np.zeros((2,3,4))
print(arr)

new_arr = np.swapaxes(arr, 0 , 2)
print(new_arr)
# (4 3, 2) - output

#moveaxis() - Moves specified axes to new positions.
arr = np.zeros((2,3,4))
print(arr)
new_arr = np.moveaxis(arr, 0, -1)
print(new_arr)

# (3 ,4 2) - output

#joining arrays
#concattenate()-joining 2 arrays
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(np.concatenate((a, b), axis = 0))
print(np.concatenate((a, b), axis = 1))

#stack - joins the arrays  along the new axis
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.stack((a,b),axis=0))
print(np.stack((a,b),axis=1))

#hstack - stack arrays horizontally
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.hstack((a,b)))

#vstack - stack arrays vertical
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.vstack((a,b)))

#column stack 1D to 2D
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.column_stack((a,b)))

#row stack 1D to 2D
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.vstack((a,b)))

#splitting array

arr = np.array([1,2,3,4,5,6])
result = np.split(arr, 3)
print(result)

#split for 2D array
arr2 = np.array([[1,2,3,4],[5,6,7,8]])
print(np.hsplit(arr2, 2))

#vsplit
arr2 = np.array([[1,2],[3,4],[5,6],[7,8]])
print(np.vsplit(arr2, 2))

#array_split
arr = np.array([1,2,3,4,5])
print(np.array_split(arr, 3))


#adding and removing of elements
#the elements will repeat in the new array
arr = np.array([1,2,3,4,5])
new_arr = np.resize(arr, (2,3))
print(new_arr)

#append()
arr = np.array([1,2,3,4])
new_arr = np.append(arr, [4,5])
print(new_arr)

#2D array
a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])
np.append(a, b, axis=0)

#insert
arr = np.array([10,20,30])
new_arr = np.insert(arr, 2,15)
print(new_arr)

#Delete
arr = np.array([10,20,30])
new_arr = np.delete(arr, 2)
print(new_arr)

#unique
arr = np.array([1,2,2,3,3])
print(np.unique(arr))

#repeating
arr = np.array([1,2,3])
print(np.repeat(arr, 3))

#Different repeats for each eleemnt
arr = np.array([10,20,30])
print(np.repeat(arr, [1,2,3]))

arr2 = np.array([[1,2],
                [3,4]])
print(np.repeat(arr,2,axis = 0))

#tile
my_array = np.array([1,2,3])
tiled_array = np.tile(my_array,2)
print("Original Array:", my_array)
print("Tiled Array:", tiled_array)


#sorting and searching
#sort() - returns a sorted copy of an array (or sorts in place if using ndarray method)
arr = np.array([5, 2, 9, 1])
sorted_arr = np.sort(arr)
print(sorted_arr)


#argsort() returns the indices that would sirt the array return the in dex positions
arr = np.array([5, 2, 9, 1])
sorted_arr = np.sort(arr)
print(sorted_arr)
indices = np.argsort(arr)
print(indices)

#lexsort() - used ofr sorting with multiple columns(like sorting by last name, then firstname
#sort by a first
#then by b (secondary key)
#sorting happens form right to left
a = np.array([1, 1, 0, 0])
b = np.array([1, 0, 1, 0])
result = np.lexsort((b, a))
print(result)






