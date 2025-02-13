# Implement quick sort on a list of integers.

list = [1, 5, 10, 33, 2, 7, 80, 2, 44]


def quick(a):
    if len(a) <= 1:
        return a
    else:
        p = a[len(a) // 2]
        left = [x for x in a if x < p]
        middle = [x for x in a if x == p]
        right = [x for x in a if x > p]
        return quick(left) + middle + quick(right)


print("Original list:", list)
sorted_list = quick(list)
print("Sorted list:", sorted_list)
