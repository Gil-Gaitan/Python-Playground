# Find a missing number in a sorted array of distinct integers
# Given a sorted array of distinct integers, return missing number.


def find_missing(arr):
    n = len(arr)
    total = (n + 1) * (n + 2) // 2
    for i in arr:
        total -= i
    return total


arr = [1, 5, 2, 3, 4, 6, 7, 8]
print(find_missing(arr))
