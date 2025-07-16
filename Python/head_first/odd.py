import time
import datetime
import sys
import os

from os import getcwd
where_am_I = getcwd()
print(where_am_I)

sys.platform
print(sys.platform)

os.getcwd()
print(os.getcwd())

print(datetime.date.today())
print(datetime.date.today().day)
print(datetime.date.today().month)
print(datetime.date.today().year)

print(time.strftime("%H:%M"))
print(time.strftime('%A %p'))


'''
from datetime import datetime

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29,
        31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print("This minute seems a little odd.")
else:
    print("Not an odd minute.")
'''
