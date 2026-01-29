'''
You are given an array arr of length n.​
Implement a stable sorting algorithm that sorts the array using a provided comparator
function.
merge sort 
'''

def stable_sort(arr, cmp):
    n = len(arr)
    if n <= 1:
        return arr 

    aux = [None] * n
    width = 1

    while width < n:
        for left in range(0, n, 2 * width):
            mid = min(left + width, n)
            right = min(left + 2 * width, n)

            i, j, k = left, mid, left

            #merge using cmp
            while i < mid and j < right:
                if cmp(arr[i], arr[j]) <= 0:
                    aux[k] = arr[i]
                    i += 1
                else:
                    aux[k] = arr[j]
                    j += 1
                k += 1

            while i < mid:
                aux[k] = arr[i]
                i += 1
                k += 1

            while j < right:
                aux[k] = arr[j]
                j += 1
                k += 1

            
            for k in range(left, right):
                arr[k] = aux[k]

        width *= 2

    return arr



def cmp(a, b):
    return (a > b) - (a < b)  

print(stable_sort([4, 1, 3, 9, 7], cmp))

