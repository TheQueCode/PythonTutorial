# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

from validator import validate_email
import validator
import datetime
from datetime import date
import time
from time import time

# today = datetime.date.today()
today = date.today()
timestamp = time()

print(today)
print(timestamp)


# import custom mod


email = 'test#test.com'

if validate_email(email):
    print('Email is valid')
else:
    print('Email is not valid')
