# Author: Gil Gaitan
# Course: ICS 352-50 Machine Learning
#         Spring 2024 - Bradford Armitage
#
# Lab 3: Numpy Arrays
# This is a collection of methods that work with numpy to manipulate data.
# Program 1 is an exercise in creating an array with slicing, then
# selecting specific parts of the data.
# Program 2 is an exercise in stacking arrays horizontally and vertically.
# Program 3 uses the tile function to extend a pattern into a checkerboard.

import numpy as np

# Program 1: Array Slicing
print("\nProgram 1: Array Slicing")
print("------------------------")

# An array containing the values 1–15.
# Remember the terminating value is exclusive.
array = np.arange(1, 16)
print("\nArray with values 1-15:")
print(array)

# reshape array into a 3-by-5 array
# 3 rows, 5 columns, so (3, 5) is the shape
array = array.reshape(3, 5)
print("\nReshaped array (3x5):\n", array)

# indexing and slicing techniques

# a) Select row 2
# 0 indexed, so row 2 is the thrird row down
row2 = array[2]
print("\n1.a. Select Row at index 2:", row2)

# b) Select column 4
# 0 indexed, so column 4 is at index 3
# slicing is [row, column]
column4 = array[:, 4]
print("\n1.b. Select Column at index 4:")
for value in column4:
    print(value)

# c) Select rows 0 and 1
# again, we are selecting rows and columns
# 0:2 is the range of rows, 0 - 2, exclusive
# : is the range of columns, all columns, 0-0
row0_1 = array[0:2, :]
print("\n1.c. Rows 0 and 1:")
print(row0_1)

# d) Select columns 2–4
# Here we want the entire row, so :, 0-0 all
# for columns 2-4, start at 2 - terminate at 5
columns2_4 = array[:, 2:5]
print("\n1.d. Columns 2 to 4:")
print(columns2_4)

# e) Select the element that is in row 1 and column 4
row1_col4 = array[1, 4]
print("\n1.e. Element at row 1, column 4:", row1_col4)

# f) Select all elements from rows 1 and 2 that are in columns 0, 2 and 4
# row 1 and 2 are 1:3, for the split set of column indexes, we make
# a list of the columns we want to select and put in brackets
row1_2_col0_2_4 = array[1:3, [0, 2, 4]]
print("\n1.f. Elements from rows 1 and 2 in columns 0, 2, and 4:")
print(row1_2_col0_2_4)

# Program 2: Horizontal and Vertical Stacking
print("\n\nProgram 2: Horizontal and Vertical Stacking")
print("-------------------------------------------")

# Create the 2D arrays array1 and array2
array1 = np.array([[0, 1], [2, 3]])
print("\nArray1:\n", array1)
array2 = np.array([[4, 5], [6, 7]])
print("\nArray2:\n", array2)

# a) Use vertical stacking to create the 4-by-2 array
# with array1 *vertically stacked on* array2
array3 = np.vstack((array1, array2))
print("\n2.a. array3 (vertical stacking):\n", array3)

# b) Use horizontal stacking to create the 2-by-4 array named array4 with array2 to the right of array1
array4 = np.hstack((array1, array2))
print("\n2.b. Array4 (horizontal stacking):\n", array4)

# c) Use vertical stacking with two copies of array4 to create a 4-by-4 array5
array5 = np.vstack((array4, array4))
print("\n2.c. Array5 (vertical stacking of array4):\n", array5)

# d) Use horizontal stacking with two copies of array3 to create a 4-by-4 array6
array6 = np.hstack((array3, array3))
print("\n2.d. Array6 (horizontal stacking of array3):\n", array6)

# Program 3: Research NumPy tile Function
print("\nProgram 3: NumPy Tile Function")
print("-------------------------------")

# Research and use NumPy’s tile function to create a checkerboard pattern of dashes and asterisks
# Checkerboard pattern is 8x8, so we need a 4x4 pattern and we can
# make a 2D array and tile it to get the 8x8 pattern
checkerboard = np.tile([["-", "*"], ["*", "-"]], (4, 4))
print("\nCheckerboard pattern:\n", checkerboard)

# End of Lab 3
print("\nEnd of Lab 3 Programming Exercises\n\n")
