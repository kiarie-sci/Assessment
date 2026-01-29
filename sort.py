
def cmp(a, b):
    if a < b:
        return -1
    if a == b:
        return 0
    if a > b:
        return 1


def merge(list1, list2):
    merged_list = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if cmp(list1[i], list2[j]) <= 0:  # use comparator
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list


def merger_sort(lst):
    if len(lst) <= 1:
        return lst

    midpoint = len(lst) // 2
    left_array = merger_sort(lst[:midpoint])
    right_array = merger_sort(lst[midpoint:])

    return merge(left_array, right_array)


print(merger_sort([3, 4, 567, 12, 1, 9, 0]))

