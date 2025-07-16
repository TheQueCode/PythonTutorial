# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# Single assignment
'''
x = 1          #int 
y = 2.5        #float
name = 'Que'   #str
is_cool = True #bool
'''

# Multiple assignment

x, y, name, is_cool = (1, 2.5, 'Que', True)

print(x, y, name, is_cool)

# Basic mah
a = x + y

print(a)

# Casting

x = str(x)  # <class 'str'>
y = int(y)
z = float(y)

print(type(x))  # <class 'int'>
print(type(y), y)
print(type(z), z)
