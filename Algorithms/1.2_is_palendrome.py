def is_palendrome(s):
    return s == s[::-1]


string = "racecar"

print(is_palendrome(string))

string = "hello"

print(is_palendrome(string))
