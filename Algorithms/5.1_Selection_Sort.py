# Implement selection sort on a list of integers.

list = [1, 5, 10, 33, 2, 7, 80]


def selection_sort(list):
    n = len(list)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if list[min_idx] > list[j]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]


print(list)
selection_sort(list)
print(list)
