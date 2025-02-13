# Implement insertion sort on a list of integers.

list = [1, 5, 10, 33, 2, 7, 80]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


print(list)
insertion_sort(list)
print(list)
