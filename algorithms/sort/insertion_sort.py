# Stable: Yes
# Requires additional memory: No
# Nubmer of exchanges: O(n^2)
# Best case: O(n)
# Worst case: O(n^2)

def insertion_sort(array):
    def swap(i, j):
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp

    n = len(array)

    for i in range(1, n):
        j = i - 1
        while j >= 0 and array[j] > array[j + 1]:
            swap(j, j + 1)
            j -= 1
