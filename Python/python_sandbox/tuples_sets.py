# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create a uple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma to be seen as a tuple
fruits2 = ('Apples',)
# print(fruits2, type(fruits2))

# Delete

del fruits2

print(fruits[1])

# Get length of tuple
print(len(fruits))  # 3

print('*' * 10)

# A Set is a collection which is unordered and unindexed. No duplicate members.

fruits_set = {'Apples', 'Oranges', 'Mangos'}

# Check if in set
print('Apples' in fruits_set)  # True

# Add to set
fruits_set.add('Grapes')

# Remove from set
fruits_set.remove('Grapes')

# Clear set
fruits_set.clear()  # set()

# Delete
del fruits_set  # not defined

print(fruits_set)
