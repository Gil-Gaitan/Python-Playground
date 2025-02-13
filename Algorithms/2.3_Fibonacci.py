# Generate Fibonacci: Print the first N numbers in the Fibonacci sequence.


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b


print(fibonacci(10))
print(fibonacci(20))
print(fibonacci(pow(10, 4)))
