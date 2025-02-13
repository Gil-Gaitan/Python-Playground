def romanToInt(s: str):
    # Map Roman numerals to their integer values
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    total = 0
    prev_value = 0

    # Process each character in the string
    for char in s:
        current_value = d[char]
        # If the previous value is less than the current, it means subtraction
        if prev_value < current_value:
            total += current_value - 2 * prev_value
        else:
            total += current_value
        prev_value = current_value

    return total


print(romanToInt("III"))  # Output: 3

print()


# Example usage:
print(romanToInt("CDIII"))  # Output: 3
print(romanToInt("LVIII"))  # Output: 58
print(romanToInt("MCMXCIV"))  # Output: 1994
