# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create Dictionary

person = {
    'first_name': 'Que',
    'last_name': 'Code',
    'age': 50
}

# print(person, type(person))

# User constructor
# person2 = dict(first_name='Henry', last_name='Mine')
# print(person2, type(person2))

# Get a value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

# Get dictionary keys
print(person.keys())

# Get dictionary items
print(person.items())

# Copy dict
person_copy = person.copy()
person_copy['city'] = 'Chicago'

# Remove an item
del (person['age'])
person.pop('phone')

# CLear
person.clear()

# Length
print(len(person_copy))  # 5

# list of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])  # Kevin
