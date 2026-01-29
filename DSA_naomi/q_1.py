'''
You are given an array of integers.​
Write a function that returns the first repeating element in the array.
'''

def first_rep(arr):
    seen = set()
    result = []

    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
        else:
            
            return num

        
    return -1

array = [4, 4, 2, 5, 1,5]
print(first_rep(array))

test = [1,2,3]
print(first_rep(test))


    
