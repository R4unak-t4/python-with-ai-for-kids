# function

# vowels = ('a','e','i','o','u')

# def vowels_count(word):
#     count = 0
#     for char in word:
#         if char.lower() not in vowels:
#             count+=1
#     return count
#
# print(vowels_count("rAunak"))

'''
Write a Python function called find_max_min that takes a list of integers as a parameter and returns both the maximum and minimum values in the list without using the built-in max() or min() functions.

Example:
Input: [4, 7, 1, 9, 2]
Output: (9, 1)
'''

# def min_max(arr):
#     min = arr[0]
#     max = arr[0]
#     for i in arr:
#         if i < min :
#             min = i
#         if i > max:
#             max = i
#     return (max,min)
#
# print(min_max([4, 7, 1, 9, 2]))

'''
Write a Python function called remove_duplicates that takes a list of numbers as a parameter and returns a new list with all duplicate values removed, while keeping the original order.

Example:
Input: [1, 2, 2, 3, 4, 3, 5]
Output: [1, 2, 3, 4, 5]
'''

# def el_dup(arr):
#     li = []
#     for i in arr:
#         if i not in li:
#             li.append(i)
#     return li
#
# print(el_dup([1, 2, 2, 3, 4, 3, 5]))

