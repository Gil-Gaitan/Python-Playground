# Counter with a list
from collections import Counter

# Create a list
L = [
    "Mark",
    "John",
    "David",
    "Mark",
    "Luke",
    "John",
    "John",
    "Luke",
    "Mark",
    "John",
    "Luke",
]

# Count the occurrences of each element in the list
c = Counter(L)

# Print the count of each element
print(c)

# Print each element and its count
for element, count in c.items():
    print(f"{element}: {count}")

# Print frequencies
print(c.values())

# Print the most common element
print(c.most_common(1))

# Print the two most common elements
print(c.most_common(2))

# Print the three least common elements
print(c.most_common()[:-4:-1])

# Print the elements with a count of 2
print([element for element, count in c.items() if count == 3])

# Print the elements with a count of 2
print([element for element, count in c.items() if count == 2])

# pop an element (remove and return the count   )
print(c.pop("Mark"))

# Print the count of each element
print(c)

# Print just the name of the second most common item
print(c.most_common(2)[1][0])

# Print count of total items
print(sum(c.values()))

# Print number of items in the dictionary
print(len(c))

# print the name of the least common item
print(c.most_common()[:-4:-1][0][0])
