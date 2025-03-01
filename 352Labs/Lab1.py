# Overview of Python’s decision structure, iterative structure, functions, and reading/writing from files
# The following programs are implemented:
#   1. Table of Squares and Cubes
#       Calculates the squares and cubes of the numbers from 0 through a number
#   2. Odd or Even
#       Uses bitwise operation
#   3. Temperature Conversion
#       Converts Celsius to Fahrenheit. Test prints 0-100 Celsius
#   4. Palindrome
#       Only accepts 7-digit integers
#   5. Write and read from a file
#       Only accepts (A, B, C, D, F, q)


# Program 1: Table of Squares and Cubes
def table_of_squares_and_cubes(num):
    print("number\tsquare\tcube")
    for i in range(1, num + 1):
        print(f"{i}\t{i ** 2}\t{i ** 3}")


# Program 2: Odd or Even
def odd_or_even(num):
    if num & 1:  # check LSB
        print(f"{num} is odd")
    else:
        print(f"{num} is even")


# Program 3: Temperature Conversion
def temperature_conversion(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}\t{fahrenheit:.1f}")


def temperature_conversion_table_zero_through(num):
    print("Celsius\tFahrenheit")
    for i in range(num + 1):
        temperature_conversion(i)


# Program 4: Palindrome
def is_seven_digit_palindrome(int):
    return is_seven_digits(int) and is_palindrome(int)


def is_palindrome(int):
    return str(int) == str(int)[::-1]


def is_seven_digits(int):
    return len(str(int)) == 7


def user_input_seven_digit_int():
    while True:
        int = input("Enter a seven-digit integer: ")
        if int.isdigit() and is_seven_digits(int):
            return int
        else:
            print("Invalid input. Please enter a seven-digit integer.")


# Program 5: Write and read from a file
def write_to_file(file_name, data):
    with open(file_name, "w") as file:
        file.write(data)


def read_from_file(file_name):
    with open(file_name, "r") as file:
        print("Reading from file:")
        for line in file:
            print(line, end="")


def analyze_file(file_name):
    with open(file_name, "r") as file:
        print("Analyzing file:")
        # Create a dictionary to count each grade
        dict = {}
        for line in file:
            line = line.strip()
            if line in dict:
                dict[line] += 1
            else:
                dict[line] = 1
        # Print the dictionary
        for key, value in dict.items():
            print(f"{key}: {value}")
        print("GPA: " + get_GPA(dict))


def grade_value(grade):
    # Dictionary to map grades to values
    grade_dict = {"F": 0.0, "D": 1.0, "C": 2.0, "B": 3.0, "A": 4.0}
    return grade_dict.get(grade, 0.0)


def get_GPA(dict):
    # Calculate the GPA
    total = 0
    count = 0
    for key, value in dict.items():
        total += grade_value(key) * value
        count += value
    return f"{total / count:.2f}"


def get_grades_from_user():
    data = ""
    valid_grades = {"A", "B", "C", "D", "F"}
    while True:
        line = input("Enter grade as CAPITAL letter (A, B, C, D or F) or 'q' to quit: ")
        if line == "q":
            break
        elif line in valid_grades:
            data += line + "\n"
        else:
            print(
                "Invalid input. Please enter a valid grade (A, B, C, D, F) or 'q' to quit."
            )
    return data


# Main Program

# Test Program 1
print("Program 1: Table of Squares and Cubes")
table_of_squares_and_cubes(5)

# Test Program 2
print("\nProgram 2: Odd or Even")
odd_or_even(5)
odd_or_even(6)

# Test Program 3
print("\nProgram 3: Temperature Conversion")
temperature_conversion_table_zero_through(100)

# Test Program 4
int = 7654321
print("\nProgram 4: Palindrome")
print(f"{int} is a palindrome: {is_seven_digit_palindrome(int)}")
int = 1234321
print(f"{int} is a palindrome: {is_seven_digit_palindrome(int)}")
int = user_input_seven_digit_int()
print(f"{int} is a palindrome: {is_seven_digit_palindrome(int)}")

# Test Program 5
print("\nProgram 5: Write and read from a file")
file_name = "grades.txt"
print(f"Writing to file: {file_name}")
data = get_grades_from_user()
write_to_file(file_name, data)
read_from_file(file_name)
analyze_file(file_name)
