# Move all zeroes in a list to the end while maintaining the order of other elements.

# Approach:
# We can solve this problem by using two pointers. p1 will keep track of the
# current position to insert the next non-zero element, and p2 will iterate
# through the list to find non-zero elements. When p2 finds a non-zero element,
# we swap it with the element at p1 and increment p1. This way, all non-zero
# elements will be moved to the beginning of the list, and all zeroes will be
# moved to the end.


def move_zeros(nums):
    p1 = 0
    p2 = 0

    while p2 < len(nums):
        if nums[p2] != 0:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
        p2 += 1

    return nums


list1 = [0, 1, 0, 3, 12, 2, 0, 5]

print(move_zeros(list1))  # [1, 3, 12, 2, 5, 0, 0, 0]
