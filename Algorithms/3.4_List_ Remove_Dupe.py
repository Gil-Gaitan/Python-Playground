# Given a sorted list, remove the duplicates in-place such that each element appears only once and return the new list.

list1 = [1, 2, 2, 2, 3, 3, 4, 4, 5, 5]


def remove_duplicates(l):
    i = 0
    while i < len(l) - 1:
        if l[i] == l[i + 1]:
            l.pop(i)
        else:
            i += 1
    return l


print(remove_duplicates(list1))  # [1, 2, 3, 4, 5]


# this time on a linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


def remove_duplicates_linked_list(node):
    current = node
    while current and current.next:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next
    return node


# test
node = Node(1)
node.next = Node(1)
node.next.next = Node(2)
node.next.next.next = Node(3)
node.next.next.next.next = Node(3)

current = remove_duplicates_linked_list(node)

while current:
    print(current.value, end=" ")
    current = current.next
print()
# Output: 1 2 3
# Time complexity: O(n)
