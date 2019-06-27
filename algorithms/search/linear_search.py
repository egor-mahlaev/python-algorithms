# Works on any array.
# Best case: O(1)
# Worst case: O(n)

def linear_search(array, x):
    for i in range(len(array)):
        if array[i] == x:
            return i
    return -1
