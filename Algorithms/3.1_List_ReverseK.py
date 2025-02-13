# Reverse a list starting from index `k` to the end.

list1 = [1, 2, 3, 4, 5, 6]
#        0  1  2  3  4  5


def reverse_at_k(l, k):
    return l[:k] + l[k:][::-1]


print(list1)
print(reverse_at_k(list1, 2))  # [1, 2, 6, 5, 4, 3]
