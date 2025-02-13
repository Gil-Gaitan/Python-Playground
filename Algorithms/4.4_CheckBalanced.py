# Verify tree is balanced by height, meaning the difference
# between the left and right subtrees is no more than 1


# Create a Sorted Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


root = Node("1")
root.left = Node("2")
root.right = Node("3")

# Left Subtree
root.left.left = Node("4")
root.left.right = Node("5")

# Right Subtree
root.right.left = Node("6")
root.right.right = Node("7")

# extra node
root.right.right.right = Node("8")

# exra node
root.right.right.right.right = Node("9")


def is_balanced(root):
    if root is None:
        return True

    left_height = get_height(root.left)
    right_height = get_height(root.right)

    if abs(left_height - right_height) <= 1:
        return is_balanced(root.left) and is_balanced(root.right)
    else:
        return False


def get_height(root):
    if root is None:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))


print(is_balanced(root))  # True
