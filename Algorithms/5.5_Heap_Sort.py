# Python program for implementation of heap Sort
# To heapify a subtree rooted with node i
# which is an index in arr[].
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


def printArray(arr):
    for i in arr:
        print(i, end=" ")
    print()


arr = [9, 4, 3, 8, 10, 2, 5]
heapSort(arr)
print("Sorted array is ")
printArray(arr)
