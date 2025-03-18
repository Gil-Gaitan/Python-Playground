import pandas as pd
import random

myList = [7, 11, 13, 17]  # Make the list
seriesFromList = pd.Series(myList)  # Creates Series from the list

element = 100.0  # Make the element
seriesOfFive100s = pd.Series([element] * 5)  # Create Series with 5 elements

listOf20RandomNumbers = [
    random.randint(0, 100) for i in range(20)
]  # Create list of 20 random numbers
series20RandomElements = pd.Series(listOf20RandomNumbers)  # Create Series from the list
print(series20RandomElements.describe())

grades = [98.6, 77.9, 100, 83.4]  # Create list of grades
index = ["Julie", "Charlie", "Sam", "Andera"]  # Create list of names for indexing
seriesGrades = pd.Series(grades, index)  # Create Series with values and index

print()
print(seriesFromList)
print()
print(seriesOfFive100s)
print()
print(series20RandomElements)
print()
print(seriesGrades)
