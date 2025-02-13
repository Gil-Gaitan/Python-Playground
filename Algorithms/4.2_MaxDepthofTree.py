# Find the maximum depth of a binary tree
# The maximum depth of a binary tree is the number of nodes on longest path
# from the root node to the farthest leaf node


# Implement Tree Traversals
# Inorder Traversal
def find_max_depth(root):  # Return value of tree depth
    if root is None:  # Base Case
        return 0
    else:  # Recursively count every node
        left_depth = find_max_depth(root.left)  # get left depth
        right_depth = find_max_depth(root.right)  # get right depth

        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1


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

root.right.right.right = Node("8")

print(find_max_depth(root))  # 3
