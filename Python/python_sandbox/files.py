# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myfile.txt', 'w')

# Get info on file
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Writing to a file
myFile.write('I love pizza')
myFile.write(' and JavaScript')
myFile.write(' and Python')
myFile.close

# Append to a closed file

myFile = open('myfile.txt', 'a')  # a for append
myFile.write(' I also like spaghetti')
myFile.close

# Read from a file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)
