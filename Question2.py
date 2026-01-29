"""
Question 2: Letter Combinations of a Phone Number
Approach
I am going to be using backtracking which means mapping the digits to the letters.
Then build the combinations character by character while skipping the digits that map to empty strings(1)

Time & Space
Time: O(4^n) (maximum for digit 7 or 9)
Space: O(n) since there is a recursion stack
"""
def letterCombinations(digits):
    if not digits:
        return []

    phone = {
        "0": " ",
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    result = []

    def backtrack(index, path):
        if index == len(digits):
            result.append(path)
            return

        letters = phone[digits[index]]
        if letters == "":
            backtrack(index + 1, path)
        else:
            for ch in letters:
                backtrack(index + 1, path + ch)

    backtrack(0, "")
    return result


print(letterCombinations("23"))













