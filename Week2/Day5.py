'''
Write a Python function merge_dicts that takes two dictionaries as input and returns a new dictionary that merges the two. If there are overlapping keys, the values in the second dictionary should overwrite the values in the first dictionary.

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'd': 5}

result = merge_dicts(dict1, dict2)
print(result)
result = {'a': 1, 'b': 4, 'c': 3, 'd': 5}
'''
# def merge_dicts(dict1, dict2):
#     merged_dict = {}
#     for key, item in dict1.items():
#         merged_dict[key] = item
#     for key, item in dict2.items():
#         merged_dict[key] = item
#     return merged_dict
#
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'f': 4, 'd': 5}
#
# result = merge_dicts(dict1, dict2)
# print(result)

# P Y T H O N
# 0 1 2 3 4 5
#  P  Y  T  H  O  N
# -6 -5 -4 -3 -2 -1

# non --> is palindrome
# noun ---> not a palindrome

'''
Write a Python function count_vowels that takes a string as input and returns a dictionary containing the count of each vowel (a, e, i, o, u) present in the string.

The function should:

Be case-insensitive

Only include vowels that appear at least once

text = "Programming is Awesome"
print(count_vowels(text))

{'a': 2, 'i': 1, 'o': 2, 'e': 2}
'''

vowels = ['a','e','i','o','u']

def count_vowels(word):
    vowels_count = {}
    for char in word:
        if char.lower() in vowels:
            if char in vowels_count:
                vowels_count[char.lower()] +=1
            else:
                vowels_count[char.lower()] = 1
    return vowels_count

text = "Programming is Awesome"
print(count_vowels(text))

'''
Write a Python function find_second_largest that takes a list of integers and returns the second largest unique number in the list.

If the list has fewer than two unique numbers, return None.

Example:
nums = [10, 20, 4, 20, 5]
print(find_second_largest(nums))


Expected Output:
10

Hint:
Think about removing duplicates before finding the largest values.
'''