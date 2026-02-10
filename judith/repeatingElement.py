def repeatingElement(arr):
    repeated = {}
    for element in arr:
        if element in repeated:
            return element
        repeated[element] = True
    return -1