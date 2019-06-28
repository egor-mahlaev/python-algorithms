# Works on sorted array.
# Best case: O(1)
# Worst case: O(log n)

def binary_search_iterative(array, x):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            right = mid - 1
        elif array[mid] < x:
            left = mid + 1
    return -1


def binary_search_recursive(array, x, left, right):
    if left > right:
        return -1
    else:
        mid = (left + right) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binary_search_recursive(array, x, left, mid - 1)
        elif array[mid] < x:
            return binary_search_recursive(array, x, mid + 1, right)
