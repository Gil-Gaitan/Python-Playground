# Perform a level-order traversal (BFS) on a binary tree.

# Approach:
# We can perform a level-order traversal (BFS) on a binary tree using a queue.
# We start by enqueuing the root node and iterate until the queue is empty.
# At each iteration, we dequeue a node, process it, and enqueue its children.
# We repeat this process until all nodes are processed.


# Here's the implementation of the level-order traversal on a binary tree:
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Function to perform a level-order traversal on a binary tree
def bfs(root):
    result = []
    if not root:  # If the tree is empty, return an empty list
        return result
    queue = [root]  # Initialize a queue with the root node
    while queue:
        level = []  # Initialize a list to store the nodes at the current level
        for _ in range(len(queue)):
            node = queue.pop(0)  # Dequeue the first node from the queue
            level.append(node.value)  # Add the node's value to the current level
            if node.left:  # Enqueue the left child if it exists
                queue.append(node.left)
            if node.right:  # Enqueue the right child if it exists
                queue.append(node.right)
        result.append(level)  # Add the current level to the result list
    return result


# Test case
# Construct the binary tree:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

# Perform a level-order traversal on the binary tree
print(bfs(root))  # [[1], [2, 3], [4, 5]]
