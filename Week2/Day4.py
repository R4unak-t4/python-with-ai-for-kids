# function
# write a function to give count of vowels in a word
vowels = ('a','e','i','o','u')
def vowel_count(word):
    count = 0
    for char in word:
        if char in vowels:
            count+=1
    return count

print(vowel_count('raunak'))


'''
Write a Python function called find_max_min that takes a list of integers as a parameter and returns both the maximum and minimum values in the list without using the built-in max() or min() functions.
[1,6,2,7,5,9]
'''
def min_max(arr):
    min = arr[0]
    max = arr[0]

    for i in arr:
        if i < min:
            min = i
        if i > max:
            max = i
    return (min,max)

print(min_max([1,6,2,7,5,9]))

'''
Write a Python function called remove_duplicates that takes a list of numbers as a parameter and returns a new list with all duplicate values removed, while keeping the original order.

Example:
Input: [1, 2, 2, 3, 4, 3, 5]
Output: [1, 2, 3, 4, 5]
'''

def dups(arr):
    non_dups = []
    for i in arr:
        if i not in non_dups:
            non_dups.append(i)
    return non_dups

print(dups([1, 2, 2, 3, 4, 3, 5]))
