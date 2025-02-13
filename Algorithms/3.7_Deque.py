# practice with deque
# deque can be used as a queue or a stack
# It is a generalization of stacks and queues
# It supports adding and removing elements from both ends in O(1) time
# It is implemented using a doubly linked list
# It is faster than lists for adding and removing elements from the front

from collections import deque

print("Deque")

# Create a deque
L = [1, 2, 3, 4, 5]
q = deque(L)
for i in q:
    print(i, end=" ")

# Add elements to the right
q.append(6)
print(q)

# Add elements to the left
q.appendleft(0)
print(q)

# Remove elements from the right
q.pop()
print(q)

# Remove elements from the left
