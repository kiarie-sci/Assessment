def repeating_element(lst):

    seen = {}

    for index, value in enumerate(lst):
        # check if the value is in the dict
        if value in seen:
            return value
        seen[index] = value
    return -1

print(repeating_element([1,2,3,4,5,6,7,8,1]))