def fizz_buzz(n):
    if n % 15 == 0:
        return str(n) + " FizzBuzz"
    elif n % 3 == 0:
        return str(n) + " Fizz"
    elif n % 5 == 0:
        return str(n) + " Buzz"
    else:
        return int(n)


def fizz_buzz_list(n):
    for i in range(1, n + 1):
        print(fizz_buzz(i))


fizz_buzz_list(pow(10, 4))
