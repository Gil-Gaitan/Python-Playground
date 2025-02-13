# Check if we have a vaild anagram


def char_exist(s1, s2):
    d = {}
    for char in s1:
        d[char] = 1
    print(d)
    for char in s2:
        if char not in d:
            return False
    return True


s1 = "avocado"
s2 = "oada"

print(char_exist(s1, s2))
