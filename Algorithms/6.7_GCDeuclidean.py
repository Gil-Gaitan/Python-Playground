# Get greatest common divisor of two numbers
# The greatest common divisor (GCD) of two numbers is the largest number that divides both of them.

# The Euclidean algorithm is a method for finding the GCD of two numbers.
# It uses the fact that the GCD of two numbers also divides their difference.


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# test
print(gcd(12, 15))  # 3
print(gcd(15, 12))  # 3
print(gcd(12, 0))  # 12
print(gcd(8, 134))  # 12
