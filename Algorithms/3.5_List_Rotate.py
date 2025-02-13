# Rotate a list to the right by k places.
# This means that the rightmost elements will move to the leftmost positions.

# 1. Slicing operator to rotate the list.
# 2. Modulo operator to find the effective rotation.

# Complexity Analysis:
# 1. The time complexity for this approach is O(n).
# 2. The space complexity for this approach is O(n).

# Let's implement the code:


def rotate_list(l, k):
    n = len(l)
    k = k % n
    return l[-k:] + l[:-k]


list1 = [1, 2, 3, 4, 5, 6]

print(list1)
print(rotate_list(list1, 2))  # [5, 6, 1, 2, 3, 4]
