#First Repeating Element
"""
Approach
Use a hashMap to track seen elements
As soon as I see an element already in the set return it
Time & Space
Time: O(n)
Space: O(n)

"""
#Solution
def firstRepeatingElement(arr):
    seen = set()

    for num in arr:
        if num in seen:
            return num
        seen.add(num)

    return -1

#Example 1
arr1 = [4, 5, 1, 2, 5, 3]
print(firstRepeatingElement(arr1)) # Should return 5

#Example 2
arr2 = [4, 5, 7, 9, 3]
print (firstRepeatingElement(arr2)) #Should return -1

