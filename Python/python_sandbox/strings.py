# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Que'
age = 50

# Concat
# print('Hello, my name is ' + name + ' and I am ' + age + ' years old')
# Errors - can only concat strings

# String Formatting

# Arguments by position

# print('My name is {name} and I am {age} years old'.format(name=name, age=age))

# F-strings

# print(f'Hello, this is an f-string. I am {name} and I am {age}')

# String Methods

s = 'hello World'

# Capialize string
print(s.capitalize())  # capitalizes the first letter & only the first

print(s.upper())  # makes all capitalized

print(s.lower())  # makes all lower case

print(s.swapcase())  # makes lower upper & upper lower

print(len(s))  # get length

print(s.replace('World', 'everyone'))  # replaces

sub = 'h'
sub2 = 'l'
# 1 - count the number of 'h's inside the string (sub = substring)
print(s.count(sub))
print(s.count(sub2))  # 3 - count the number of 'l's inside the string

print(s.startswith('h'))  # True

print(s.endswith('d'))  # True

print(s.split())  # splits ['hello', 'World']

print(s.find('r'))  # find position - 8

print(s.isalnum())  # false - is alphanumeric?

print(s.isalpha())  # false - is alphabetic?

print(s.isnumeric())  # false - is numeric?
