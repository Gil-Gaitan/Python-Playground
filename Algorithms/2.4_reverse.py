# Reverse an integer at index k


def reverse(n, k):
    n = str(n)
    n = n[:k] + n[k:][::-1]
    return int(n)


# test cases
print(reverse(123456, 2))  # 126543
print(reverse(123456, 3))  # 123654
print(reverse(123456, 0))  # 654321
print(reverse(1234567777, 5))  # 123456
