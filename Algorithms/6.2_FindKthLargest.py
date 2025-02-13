# Find the kth largest element in a list


def findKthLargest(nums, k):
    nums.sort()
    return nums[-k]


# Test cases
print(findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
print(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4

# Time complexity: O(nlogn)

# The above solution is not optimal. We can solve this problem in O(n) time using the quickselect algorithm.
# The quickselect algorithm is a selection algorithm to find the kth smallest element in an unordered list.
# It is similar to the quicksort algorithm, but instead of sorting the entire list, it only focuses on the kth element.
# The algorithm works by selecting a pivot element and partitioning the list into two sublists: one with elements smaller
# than the pivot and one with elements larger than the pivot. If the pivot is the kth element, we return it. Otherwise, we
# recursively apply the algorithm to the appropriate sublist.


# Here's the implementation of the quickselect algorithm to find the kth largest element in a list:
def quick_k_select(list, k):
    if list:
        pivot = list[0]  # choose the first element as the pivot
        less = [x for x in list if x < pivot]  # elements less than the pivot
        greater = [x for x in list if x > pivot]  # elements greater than the pivot
        equal = [x for x in list if x == pivot]  # elements equal to the pivot

        if k <= len(greater):
            return quick_k_select(greater, k)
        elif k <= len(greater) + len(equal):
            return pivot
        else:
            return quick_k_select(less, k - len(greater) - len(equal))


# Test cases

print(quick_k_select([3, 2, 1, 5, 6, 4], 2))  # 5
print(quick_k_select([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
