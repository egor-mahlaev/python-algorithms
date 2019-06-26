#
# Works in any array.
# Best case: O(1)
# Worst case: O(n)
#

def linear_search(array, number):
    for i in range(len(array)):
        if array[i] == number:
            return i
    return -1
