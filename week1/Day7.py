# collection data types

# primitive data-types
# int
# str
# float
# boolean

# (non-primitive data types)
# collection data types include the collection the primitive data types in different structures.
# Holds multiple primitive data types

# list

# list is enclosed in big-square brackets : []
# indexed datatype

# info = [20,63.5,"raunak"]

# 20 --> 0
# 63.5 --> 1
# "raunak" --> 2

# accessing by index
# print(info[1])

# [20,63.5,"raunak"]

# for-in loop in list
# for var in info:
#     print(var)

# task
# i = 0
# while i < len(info):
#     print(info[i])
#     i+=1
#

info = [20,63.5,"raunak"]

# List operations

# .append()
# [20,63.5,"raunak"] --> info.append(True) --> [20,63.5,"raunak",True]
# info.append(True)
# print(info)

# .pop()
# [20,63.5,"raunak"] --> info.pop() --> [20,63.5]
# print(info.pop())
# print(info)

# replacing element in list
# info[1] = 65.7
# print(info)

# .insert()
# [20,63.5,"raunak"] --> info.insert(index,element) --> [20,172,63.5,"raunak"]
#                                       1     172
# info.insert(1,172)
# print(info)

# .clear()
# info.clear()
# print(info)

# Task

# 1. Take 5 items' price as input from user

# 2. Store those items' price in a list

# 3. Run a for in loop on the list to calculate the total

# 4. Print the total with 13% V.A.T

# list1 = []
# for i in range(1,6):
#     price_individual = int(input(f'Enter price for item {i} : '))
#     list1.append(price_individual)
# total = 0
# for price in list1 :
#     total+=price
#
# print(f'Total with V.A.T is {total + (total*0.13)}')

list1 = []
leng = len(list1)
while leng < 5:
    leng += 1
    price_individual = int(input(f'Enter price for item {leng}: '))
    list1.append(price_individual)
total = 0
index = 0
while index < leng :
    total += list1[index]
    index += 1
print(f"Total cost is {total}")
print(f'Total with V.A.T is {total + (total*0.13)}')








