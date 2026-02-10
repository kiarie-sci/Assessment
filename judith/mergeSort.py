def stableSort(arr, cmp):
    n = len(arr)
    if n <= 1:
        return arr

    temp = [] * n

    subarray_size = 1
    while subarray_size < n:
        start = 0

        while start < n:
            mid = min(start + subarray_size, n)
            end = min(start + 2 * subarray_size, n)

            i = start
            j = mid
            k = start

            while i < mid and j < end:
                if cmp(arr[i], arr[j]) <= 0:
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


            while j < end:
                temp[k] = arr[j]
                j += 1
                k += 1

            start += 2 * subarray_size

      
        for i in range(n):
            arr[i] = temp[i]

        subarray_size *= 2

    return arr