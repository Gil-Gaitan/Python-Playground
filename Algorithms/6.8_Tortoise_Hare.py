# Floyd's Cycle-Finding Algorithm
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# Function that returns true if there is a loop in linked
# list else returns false.
def detect_loop(head):

    # Fast and slow pointers initially points to the head
    slow = head
    fast = head

    # Loop that runs while fast and slow pointer are not
    # None and not equal
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # If fast and slow pointer points to the same node,
        # then the cycle is detected
        if slow == fast:
            return True
    return False


# Create a hard-coded linked list:
# 10 -> 20 -> 30 -> 40 -> 50 -> 60
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)

head.next.next.next.next = head

if detect_loop(head):
    print("true")
else:
    print("false")
