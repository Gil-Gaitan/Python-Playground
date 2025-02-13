# Given an array of sorted integers,
# return two numbers that sum to target.
# Hash discovered values with their index.


def two_sum(arr, target):
    discovered = {}
    for i, num in enumerate(arr):
        if target - num in discovered:
            return [discovered[target - num], i]
        discovered[num] = i
    return None


array1 = [2, 7, 11, 15, 30, 99, 100]

print(two_sum(array1, 9))  # [0, 1]
print(two_sum(array1, 109))  # None
print(two_sum(array1, 130))  # [4, 6]
print(two_sum(array1, 101))  # [0, 5]

# Do it again with two pointers:


def two_sum_pointers(arr, target):
    left, right = 0, len(arr) - 1  # set left and right index values 0 and last item
    while left < right:  # while left is less than right (on opposite sides)
        if arr[left] + arr[right] == target:  # found target
            return [left, right]  # return the indexes
        elif arr[left] + arr[right] < target:  # if sum is less than target
            left += 1  # move left pointer to the right to increase sum
        else:
            right -= 1  # move right pointer to the left to decrease sum
    return None


print()
print(two_sum_pointers(array1, 9))  # [0, 1]
print(two_sum_pointers(array1, 109))  # None
print(two_sum_pointers(array1, 130))  # [4, 6]
print(two_sum_pointers(array1, 101))  # [0, 5]

# first two_sum function works on unsorted arrays
list_unsorted = [2, 7, 1, 11, 44, 15, 30, 99, 8, 100]

print()
print(two_sum(list_unsorted, 9))  # [0, 1]
print(two_sum(list_unsorted, 109))  # None
print(two_sum(list_unsorted, 130))  # [6, 9]
