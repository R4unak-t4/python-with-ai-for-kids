# tuple
# The tuple is enclosed in small brackets : ()
# Tuple is immutable
# Tuple is indexed data type
#
# my_tuple = ('raunak',20,63.3)
#

# Slicing
# my_list = [1,2,3,4,5,6,7,8,9]

# arr[   a     :   b               ], here a and b are the indexes
#      start      end but exclusive --> b-1
# print(my_list[1:5:2])



# Task
# use while loop for students.
# info = {
#     'class name' : 'AI room',
#     'class no' : 12,
#     'class area' : 44.4,
#     'is class available' : True,
#     'students' : ['raunak','devansh','ram'],
# }
info = {
    'class name' : None,
    'class no' : None,
    'class area' : None,
    'is class available' : None,
    'students' : None,
}
class_name = input('Enter class name : ')
class_no = int(input('Enter class no : '))
class_area = float(input('Enter class area : '))
class_availability = bool(input('Entr class availability status : '))
students_ = []

while True:
    student_ = input('Enter student name : ')
    students_.append(student_)
    des = input('Do you ant to add more? (no to discontinue) : ')
    if des.strip().lower() == 'no':
        break

info['class name'] = class_name
info['class no'] = class_no
info['class area'] = class_area
info['is class available'] = class_availability
info['students'] = students_

print(f'Class name : {info['class name']}')
print(f'Class no : {info['class no']}')
print(f'Class area : {info['class area']}')
if info['is class available']:
    print('Class available : Yes')
else:
    print('Class available : No')
print(f'Students in the class {info['class name']} : ')
for student in info['students']:
    print(student)

students = [
    {
    'id' : 1,
        'name' : 'Raunak'
},
    {
    'id' : 2,
        'name' : 'Raunak'
}
]