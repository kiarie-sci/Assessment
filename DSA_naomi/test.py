def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    l_half = merge_sort(arr[:mid])
    r_half = merge_sort(arr[mid:])

    return merge(l_half, r_half)

def merge(l, r):
    sorted_arr = []
    i = j = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            sorted_arr.append(l[i])
            i +=1

        else:
            sorted_arr.append(r[j])
            j +=1

    sorted_arr.extend(l[i:])
    sorted_arr.extend(r[j:])

    return sorted_arr

def cmp(a, b):
    return (a > b) - (a < b)  

print(merge_sort([4, 1, 3, 9, 7]))
