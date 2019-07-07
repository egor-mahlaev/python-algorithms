# Stable: Yes
# Requires additional memory: No
# Number of exchanges: O(n^2)
# Best case: O(n)
# Worst case: O(n^2)

def bubble_sort(array):
    def swap(i, j):
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp

    n = len(array)
    i = 0
    f = True

    while f:
        f = False
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                swap(j, j + 1)
                f = True 
        i += 1
