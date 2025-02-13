print("\nHello, World\n")

print("Syntax Checkers")

# 1.1 Syntax Error - Missing Parentheses

string1 = "Assignment (5+5)"
string2 = "Assignment (5+5"
string3 = "Assignment )5+5)"


def check_paren(string):
    stack = []  # stack push and pop Found Parentheses
    for char in string:
        if char == "(":
            stack.append(char)
        elif char == ")":  # if closing paren
            if not stack:
                return False  # not balanced
            stack.pop()  # if stack has a paren, pop it
    return not stack  # Does stack have nothing in it? If yes, it is balanced


print(check_paren(string1))
print(check_paren(string2))
print(check_paren(string3))
print(check_paren("Assignment(+5(+%(+%)))"))
