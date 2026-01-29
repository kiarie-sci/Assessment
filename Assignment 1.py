
#function to print out first repeating elements in array
def first_repeating_element(arr):
    # Empty dictionary to keep track of my elements
    my_dict = {}
    for num in arr:
        if num in my_dict:
            # First repeating element found
            return num
        else:
            # Mark the number as my dictionary
            my_dict[num] = True

    # There are no repeating elements found
    return -1
#Input of interger elements
arr = [2, 5, 1, 2, 3, 5, 1]
# Outputs the repeating elements
print(first_repeating_element(arr))
