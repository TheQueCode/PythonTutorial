# This is a comment
print('Hello World!')
print('I like pizza!')
print('It is really good!')

# variables - (string, integer, float, boolean)

# Strings
first_name = 'Que'
food = 'pizza'
email = 'quecode@gmail.com'

print(first_name)

# fstring
print(f'Hello, my name is {first_name}')
print(f'I like {food}')
print(f'My email is: {email}')

# Integer - whole numbers

age = 25
quantity = 3
num_of_students = 30

print(f"I'm {age} years old.")
print(f'I am buying {quantity} items.')
print(f'My class has {num_of_students} students.')

# floats - floating point number

price = 10.99
gpa = 3.8
distance = 5.5

print(f'The price is ${price}')
print(f'My GPA is: {gpa}')
print(f'I ran {distance} km.')

# Boolean - true or false

is_student = True
has_kids = False

print(f'I am a student: {is_student}')
print(f'I have kids: {has_kids}')

if is_student:
    print('You are a student')
else:
    print('You are not a student')


for_sale = False

if for_sale:
    print('This item is for sale')
else:
    print('This item is not for sale')

is_online = True

if is_online:
    print('Is online')
else:
    print('Is offline')


# Typecasting = converting variable from one data type to another

name = 'Que Code'
age = 50
gpa = 3.8
is_student = True

print(type(name))  # <class 'str'>
print(type(age))  # <class 'int'>
print(type(gpa))  # <class 'float>
print(type(is_student))  # <class 'bool'>

gpa = int(gpa)
print(type(gpa))  # <class 'int'>
print(gpa)  # 3

age = float(age)
print(type(age))  # <class 'float>
print(age)  # 50.0

print(name, age)

# Lists

names: list = ['Que', 'Henry', 'Chris']  # mutable
coordinates: tuple = (1.5, 2.3)  # immutable - once set,can't change
unique: set = {1, 4, 2, 9}  # lists that cannot have duplicates
data: dict = {'name': 'Que', 'age': 50}  # key, value pairs

print('*' * 10)

# PEP 8 Formatting Python Code

x = 1
y = 2
unit_price = 3
