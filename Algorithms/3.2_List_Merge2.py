# Merge two lists and sort

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]


def merge_sort_lists(l1, l2):
    return sorted(l1 + l2)


print(merge_sort_lists(list1, list2))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
