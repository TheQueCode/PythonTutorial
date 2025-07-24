'''
# Core Data Types: Int, Float, String, Bool

# Int - any whole number without a decimal

-2394849583
2090293
1
-1
5743

# Float

-9.72
27272.0
897.987

# String

'Hello'
"Hello"
'4.6'

# Bool

True - 1
False - 0


# Output and Printing
print('Hello World!')
print(4.5)
print(1110.0111, 'hello', True, 'Now', -88)

# Variables
hello = 'que'
world = 'world'
world = hello
hello = 'no'

print(hello, world)

# User Input
# name = input('Name: ')
# age = input('Age: ')

# print('Hello', name, 'you are', age, 'years old')
# print(f'Hello, {name}')

# Arithmetic Operators
x = 10
y = 3
result = x + y
result = x - y
result = x * y
result = int(x / y)
result = x ** y
# Floor division - removes repeating decimal point. Answer isn't 3.3333333, it's 3
result = x // y
result = x % y

# Order of operation - BEDMAS - Brackets, Exponents, Division, Multiplication, Addition, Subtraction
print(result)

# num = input('Number: ')
# print(int(num)-5)

# String Methods

hello = 'hello'.upper()  # HELLO
hello = 'heLLO'.lower()  # hello
hello = 'heLLO'.capitalize()  # Hello
hello = 'hello'.count('l')  # 2

print(hello)
x = 'hello'
y = 3
z = 'yes'
print(x * y)  # hellohellohello
print(x + y) # helloyes

# Conditional Operators

x = 'hello'
y = 'hello'

print(x == y)  # True

print('a' > 'Z')  # True
print(ord('a'))  # ord = ordinal a = 97
print(ord('Z'))  # Z = 90
print(ord('b'))  # b = 98

print(7.5 > 7)  # True
print(7.0 == 7)  # True

# Chained Conditionals - not, and, or

x = 7
y = 8
z = 0

result1 = x == y
result2 = y > x
result3 = z < x + 2

result4 = result1 or result2 or result3
print(result4)

print(not True)  # False
print(not False)  # True
print(not (False or True))  # False

# If/Else/Elif
x = input('Name: ')

if x == 'Tim':
    print('You are great')
elif x == 'Que':
    print('You are Betta')
else:
    print('Who the hell are you?')

print('Always do this')

# Collections - list and tuples

x = [4, True, 'hello']  # list
x[0] = 'hello'
x.append('hi')
print(x.pop(0))
print(x)  # 3 - len = length
print(x[1])

square_nums = []
for num in range(1, 22):
    square = num**2
    square_nums.append(square)

print(square_nums)

# Looping through slices

fruits = ['dragon fruit', 'jackfruit',
          'strawberry', 'banana', 'peach', 'guava']

for fruit in fruits[:5]:
    print(f'The {fruit.title()} is ripe for the taking.')
    print(f'I will start picking {fruit.title()} next Monday.')

# Copying Lists
books = ['great expectations', 'god of flies', 'tempest',
         'middle march', 'bleak house', 'hard times']

favorite_books = books[:]

print('These are the books I have in my library:')
print(books)

print('These are my favorite books:')
print(favorite_books)
'''
# Python Conditionals
bikes = ('toyota', 'bmw', 'suzuki', 'yamaha', 'harley davidson', 'honda')

for bike in bikes:
    if bike == 'bmw':
        print(bike.upper())
    else:
        print(bike.title())
