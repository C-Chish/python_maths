# ~DICTIONARIES
# Dictionaries allow us to work w/ key value pairs
# AKA hash maps or associative arrays
# two linked values the key is a unique identifier
# eg: representing a student w/ a dictionary
student = {'name': 'John', 'age': 25, 'courses': ['Python', 'GIT']}
# print(student['name'])
# returns "John"
# keys can be inmutable data types. (inlcude intergers, etc)

# .get() method= does the same as above but if a key is not
# in the dictionary, it returns 'none' instead of an error eg:
# print(student.get('cake'))  #None
# if a keys is not in the dictionary it can also be edited to return chosen txt
# print(student.get('cake', 'not here!'))

# to add to the key ['insert']:
# student['phone'] = '666-555'
# print(student)

# ~UPDATE method
# updates keys faster, can add a whole index
# eg:
# student.update({'name': 'Lina', 'age': 25, 'cake': 'present'})
# print(student)

# ~DEL method
# deletes a key from the dictionary eg:
# del student['age']
# print(student)  # returns {'name': 'Lina', 'courses':
# ['Python', 'GIT'], 'cake': 'present'} (no age)
# OR//
# ~POP method- to see what was deleted
# age = student.pop('age')
# print(age)
# print(student)

# LOOPING
# see the length of our keys
# print(len(student))
# see the keys in the dictionary
# print(student.keys())  # returns dict_keys
# (['name', 'age', 'courses'])
# see the values
# print(student.values())  # returns dict_values
# (['John', 25, ['Python', 'GIT']])
# to see keys and values
# print(student.items())  # shows pairs of names and keys
# dict_keys(['name', 'age', 'courses'])
# dict_values(['John', 25, ['Python', 'GIT']])
# dict_items([('name', 'John'), ('age', 25), ('courses', ['Python', 'GIT'])])
# The loop
#    print(keys, values)

# student = {"name": "leslie", "age": 29, "sex": True}
# for key in student:
#     print("The key is " + str(key) + " and the value is "
#           + str(student[key]))
