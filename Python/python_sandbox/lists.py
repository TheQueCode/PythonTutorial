# A List is a collection which is ordered and changeable. Allows duplicate members.

# List

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))

# print(numbers, numbers2)

# Get a value
print(fruits[1])  # Oranges

# Get length of list
print(len(fruits))  # 4

# Append to list
fruits.append('Mangos')

# Remove from list
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'Strawberries')

# Remove from position
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort
fruits.sort()

# Reverse Sort
fruits.sort(reverse=True)

# Change value
fruits[0] = 'Blueberries'


print(fruits)
