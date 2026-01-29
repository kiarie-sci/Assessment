'''You are given a string containing digits from 0–9.​
Return all possible letter combinations that the number could represent, in any order.
Each digit maps to letters as on a traditional phone keypad.​
Note that 1 does not map to any letters.'''

    
def letter_comb(nums):
    if not nums:
        return []

    mapping = {
        "0": " ","1": "",
        "2": "abc","3": "def",
        "4": "ghi","5": "jkl",
        "6": "mno","7": "pqrs",
        "8": "tuv","9": "wxyz"
    }

    #empty combination
    comb = [""]

    for d in nums:
        letters = mapping.get(d, "")
        if not letters:  
            continue

        new_comb = []
        for prefix in comb:
            for ch in letters:
                new_comb.append(prefix + ch)
        comb = new_comb

    return comb

print(letter_comb("23"))