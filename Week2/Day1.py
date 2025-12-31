# Dictionary
# word : meaning
# Key     value

# Dictionary is enclosed in curly braces : { }
# Data is stored in key value pairs

# key_name = 'key'
# value_name = 'value'
#
# my_dictionary = {
#                   'key' : 'value',
#                   'key1' : 'value1',
#                   'key2': True
#                   }
#
# print(my_dictionary[key_name])

# For in Loop on Dictionary
# info = {
#     'first name' : 'Raunak',
#     'last name' : 'Thapa',
#     'age' : 20
# }

# key_name ---> key, value_name ---> value
# for key_name, value_name in info.items():
#     print(key_name)

# Task
# my_dictionary = {
#                 'firstname': 'Devansh',
#                 'lastname':'Taparia',
#                 'age': '13'
#                 }
# for key in my_dictionary:
#     if key == 'firstname':
#         print(key,my_dictionary['firstname'])
#
#     elif key == 'lastname':
#         print(key,my_dictionary['lastname'])
#
#     else:
#         print(key,my_dictionary['age'])
#

# replacing values
# info = {
#     'first name' : 'Raunak',
#     'last name' : 'Thapa',
#     'age' : 20
# }
# info['age'] = 30
# print(info['age'])

# del
# del info['age']
# print(info)

# .pop()
# info = {
#     'first name' : 'Raunak',
#     'last name' : 'Thapa',
#     'age' : 20
# }
#
# print(info.pop('last name'))
# print(info)
#
# print(info.items())