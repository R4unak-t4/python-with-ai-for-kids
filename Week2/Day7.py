'''
Write a function validate_password(password) that:
Minimum length 8
Must contain at least one digit
Must contain at least one uppercase letter
Return True or False
'''

def password_validate(password) :
    count_digits = 0
    count_upper = 0
    if len(password)<8:
        return False
    for char in password:
        if char.isdigit():
            count_digits +=1
        if char.isupper():
            count_upper +=1
        if count_digits > 0 and count_upper > 0:
            return True
    return count_digits >0 and count_upper >0


print(password_validate('Myww2game'))

'''
Write a function common_elements(list1, list2) that:
Returns a list of common elements (no duplicates)
Input: [1,2,3,4], [3,4,5,6]
Output: [3,4]
'''

'''
Write a function rotate_list(lst, k) that:
Rotates list right by k positions
Example :
    Input: [1,2,3,4,5], k=2
    Output: [4,5,1,2,3]
'''

def rotate_list(lst, k):
    for i in range(k):
        last = lst.pop()
        lst.insert(0,last)
    return lst

print(rotate_list([1,2,3,4,5], k=3))