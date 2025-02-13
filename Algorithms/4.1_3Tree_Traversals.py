# Implement Tree Traversals


# Inorder Traversal
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)


# Preorder Traversal
def preorder_traversal(root):
    if root:
        print(root.data, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)


# Postorder Traversal
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end=" ")


# Create a Binary Tree pyramid values
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

print("Inorder Traversal:")
inorder_traversal(root)
print()
print("Preorder Traversal:")
preorder_traversal(root)
print()
print("Postorder Traversal:")
postorder_traversal(root)
print()
