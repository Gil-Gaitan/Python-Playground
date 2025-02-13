# This program calculates the sum of all multiples of m or p that are less than n.
# The function sum_all_multiples(n, m, p) takes three arguments: n, m, and p.
# It returns the sum of all multiples of m or p that are less than n.
# The function uses a for loop to iterate over the range from 1 to n.
# If the current number i is divisible by m or p, it adds i to the sum.


def sum_all_multiples(n, m, p):
    sum = 0
    for i in range(1, n):
        if i % m == 0 or i % p == 0:
            sum += i
    return sum


print(sum_all_multiples(10, 5, 3))
print(sum_all_multiples(1000, 100, 99))
print(sum_all_multiples(pow(3, 5), 2, 7))
print(sum_all_multiples(pow(5, 6), 10, 11))
print(sum_all_multiples(pow(9, 7), 9, 8))
