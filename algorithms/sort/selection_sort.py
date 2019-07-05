# Stable: No
# Requires additional memory: No
# Number of exchanges: O(n)
# Best case: O(n^2)
# Worst case: O(n^2)

def selection_sort(array):
    def swap(i, j):
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp

    n = len(array)
    
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        swap(i, min_index)
