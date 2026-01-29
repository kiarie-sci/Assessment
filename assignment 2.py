#function to give letter combination of phone number
def letter_combinations(values):
    if not values:
        return []#output an empty list
# a dictionary of the phone mapping.
    phone_map = {
        '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
        '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
    }
    # start with an empty combination
    result = [""]
    for value in values:
        result = [prefix + letter for prefix in result for letter in phone_map[value]]

    return result
#Output the combination of the given digits:
print(letter_combinations("67"))

