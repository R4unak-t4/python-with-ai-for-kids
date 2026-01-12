'''
Write a Python function called count_word_frequency(sentence) that:
Takes a string sentence as input. Ignores case sensitivity (treat "Python" and "python" as the same word). Removes punctuation (.,!?). Returns a dictionary where: Keys are unique words in the sentence
Values are the number of times each word appears
sentence = "Python is great, and Python is fun!"
print(count_word_frequency(sentence))
result : {'python': 2, 'is': 2, 'great': 1, 'and': 1, 'fun': 1}
'''

# def count_word_frequency(sentence):
#     sentence = sentence.replace(',','')
#     sentence = sentence.replace('.','')
#     sentence = sentence.replace('!','')
#     sentence = sentence.replace('?','')
#     arr = sentence.split(' ')
#     word_freq = {}
#     for word in arr:
#         if word in word_freq:
#             word_freq[word] +=1
#         else:
#             word_freq[word] = 1
#     return word_freq
#
# sentence = "Python is great, and Python is fun!"
# print(count_word_frequency(sentence))

'''
Write a Python function called is_balanced(s) that:
Takes a string s containing only parentheses ( and ).
Returns True if the parentheses are balanced, otherwise returns False.
A string is considered balanced if:
Every opening parenthesis has a corresponding closing one.
No closing parenthesis appears before a matching opening one.

Example :
print(is_balanced("(()())"))   # True
print(is_balanced("(()"))      # False
print(is_balanced("())("))     # False
'''

def is_balanced(word):
    count = 0
    for char in word:
        if char == '(':
            count +=1
        elif char == ')':
            count -=1
        if count < 0:
            return False
    return count == 0

print(is_balanced("(()())"))   # True
print(is_balanced("(()"))      # False
print(is_balanced("())("))     # False