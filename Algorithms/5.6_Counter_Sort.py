# Implements the counter sort algorithm
# Counter sort is a sorting algorithm that uses a counter array
# to store the count of each element in the input list.
# The algorithm then uses the counter array to reconstruct the sorted list.


def counter_sort(arr):
    # Find the maximum element in the input list
    max_element = max(arr)

    # Create a counter array with the size of the maximum element
    counter = [0] * (max_element + 1)

    # Count the occurrences of each element in the input list
    for element in arr:
        counter[element] += 1

    # Reconstruct the sorted list using the counter array
    sorted_list = []
    for i in range(len(counter)):
        sorted_list.extend([i] * counter[i])

    return sorted_list


# test
list = [1, 5, 10, 33, 2, 7, 80]
print("Original list:", list)
sorted_list = counter_sort(list)
print("Sorted list:", sorted_list)
