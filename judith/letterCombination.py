def letterCombo(digits:str):
    if not digits:
        return []
    digit_mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
        '0': ' ',
        '1': '',
    }
    results = []
    def backtrack(combo,digit):
        if not digit:
            results.append(combo)
        else:
            for letter in digit_mapping[digit[0]] :
                backtrack(combo+letter,digit[1:])
    backtrack('',digits)
    return results