"""
Stable Sort with Custom comparator
Approach
I am going to use an iterative bottom up merge sort to avoid recursion and to use 1 auxilliary array.
I will start by merging the subarrays of size 1, then 2, 4, 8, ... ,
Then use a comparator for all comparisons, then compile all the merged results back to one array
"""

def stableSort(arr, comp):
    n = len(arr)
    temp = [None] * n
    width = 1

    while width < n:
        for left in range(0, n, 2 * width):
            mid = min(left + width, n)
            right = min(left + 2 * width, n)

            i, j, k = left, mid, left

            while i < mid and j < right:
                if comp(arr[i], arr[j]) <= 0:
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    j += 1
                k += 1

            while i < mid:
                temp[k] = arr[i]
                i += 1
                k += 1

            while j < right:
                temp[k] = arr[j]
                j += 1
                k += 1

        for i in range(n):
            arr[i] = temp[i]

        width *= 2


def comp(a, b):
    return a - b

arr = [5, -3, 3, 8, 3, 7, 8, 3, -2]
stableSort(arr, comp)
print(arr)








