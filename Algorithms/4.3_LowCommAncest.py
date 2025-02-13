# Find the lowest common ancestor of two nodes in a binary tree.

# as function traverses, doesnt always return the lca, at each level,
# it checks if leafs match a target, if so, return parent as the root,
# as it moves back up th tree, it checks if the left and right return
# values are not None, if so, it returns the ancetor root


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

# Find the lowest common ancestor of two nodes in a binary tree
# The lowest common ancestor is the node that is the ancestor of both nodes
# and is the lowest in the tree


def find_lca(root, node1, node2):
    if root is None:  # Base Case
        return None
    if root.data == node1 or root.data == node2:  # find a root?
        return root  # return it
    left = find_lca(root.left, node1, node2)  # recursively search left
    right = find_lca(root.right, node1, node2)  # recursively search right
    if left and right:
        return root
    if left is None and right is None:
        return None
    return left if left else right


print(find_lca(root, "4", "5").data)  # 2
print(find_lca(root, "6", "8").data)  # 3
print(find_lca(root, "2", "3").data)  # 1
print(find_lca(root, "5", "8").data)  # 1
