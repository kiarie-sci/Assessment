def letter_combinations(string):
    if string is int():
        return "Only Strings in "" can be inputted and must be a phone number"
    phone_combination = {
        "0":" ",
        "1": "",
        "2":"abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl" ,
        "6": "mno" ,
        "7": "pqrs" ,
        "8": "tuv",
        "9": "wxyz"
    }

    seen = list()

    for i, value in enumerate(string):
        if value in phone_combination:
            seen.append(phone_combination[value])
    return seen


my_number = "0115720771"

print(letter_combinations(my_number))

