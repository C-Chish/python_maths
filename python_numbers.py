# Numbers, Lists, Tuples, Sets

# numbers that look like strings
# vars that look like numbers

# num_1 = '100'
# num_2 = '200'  # this is a string lol
# print(num_1 + num_2)
# returns: 100200

# ~CASTING
# to turn them into integers

# num_1 = int(num_1)
# num_2 = int(num_2)  # this is a function o create an integer

# print(num_1 + num_2)

# Python Tutorial for Beginners 4: Lists, Tuples, and Sets

# ~LISTS[]
# work with a list of values

# courses = ['Python', 'C#', 'Ruby', 'GIT']
# print(courses[2])

# Negative index- -1 will always be the last item.
# Index error- no item
# print(courses[-1])

# ~SLICING

# we want all the values starting from the beginning
# and up to but not including eg:
# print(courses[0:2])  # should print out python and C#
# you can leave out the 0- it assumes you start from the
# beginning

# if nothing is put next to the : , it assumes it wants to go to
# the end of the list

# ~APPEND
# Adds to the list, puts it at the end
# courses.append('Atom')
# print(courses)
# ['Python', 'C#', 'Ruby', 'GIT', 'Atom']

# ~INSERT
# Insert adds it to a specific location
# Takes two arguments (the index you want to insert it)
# (location : value) eg:
# print(courses)
# courses.insert(1, 'Atom')

# print(courses)
# ['Python', 'C#', 'Ruby', 'GIT']
# ['Python', 'Atom', 'C#', 'Ruby', 'GIT']

# ~EXTEND
# for multiple values we want to add to our list
# courses_2 = ['cooking', 'karate']
# courses.insert(0, courses_2)
# print(courses)
# [['cooking', 'karate'], 'Python', 'C#', 'Ruby', 'GIT']

# INSERT in this case inserts the whole list
# instead of individual values inside the list
# So instead use INSERT
# courses.extend(courses_2)
# print(courses)
# ['Python', 'C#', 'Ruby', 'GIT', 'cooking', 'karate']

# ~REMOVE
# removing values from our list
# courses.remove('C#')
# print(courses)

# courses = ['Python', 'C#', 'Ruby', 'GIT']

# or you can use ~POP
# courses.pop()
# removes the last item on the list
# print(courses)
# ['Python', 'C#', 'Ruby'](removed GIT)
# pop also prints out the value it removed
# deleted = courses.pop()
# print(deleted)  # GIT
# print(courses)  # ['Python', 'C#', 'Ruby']
# courses = ['Python', 'C#', 'Ruby', 'GIT']

# ~REVERSE
# courses.reverse()

# ~SORTING
# Sorts alphabetically
# courses.sort()
# print(courses)
# ['C#', 'GIT', 'Python', 'Ruby']

# Also sorts numbers in ascending order
# nums = [4, 5, 8, 4, 22, 0]  # [0, 4, 4, 5, 8, 22]
# nums.sort()
# print(nums)

# Descending Order
# courses.sort(reverse=True)
# nums.sort(reverse=True)
# print(nums)
# print(courses)
# [22, 8, 5, 4, 4, 0]
# ['Ruby', 'Python', 'GIT', 'C#']
# These alters the originals

# SORTED function (different to the sort method)
# sorted(nums)
# print(nums)
# list is not sorted it's the same
# this is beacause the ~sorted function does not sort list in place
# returns a sorted version of the list
# [4, 5, 8, 4, 22, 0]
# sorted_nums = sorted(nums)
# print(sorted_nums)
# [0, 4, 4, 5, 8, 22] - sorted
# this does not alter the originals

# ~MIN AND MAX/SUM
# print(min(nums))  # 0
# print(max(nums))  # 22
# print(sum(nums))  # 43

# Finding the ~INDEX VALUE in our list
# courses = ['Python', 'C#', 'Ruby', 'GIT']
# print(courses.index('GIT'))  # index 2

# To check if a value is even in our list and to check
# if a value is true or false: "IN FUNCTION"
# print('Art' in courses)  # returns false because 'Art' is not on the list

# ~FOR LOOP
# for item in courses:
# print(item)   # we want to print out that item
# Creating a loop that goes through each value of the list
# Each loop through this item variable will be
# equal to the next item in the list
# The indentation is to say the code is executed from within the for loop
# "item" is just a var, it can be changed

# ~ENUMERATE function
# for index, item in enumerate(courses):
#    print(index, item)  # returns:
# 0 Python
# 1 C#
# 2 Ruby
# 3 GIT
# if we do not want to start from 0
# we can pass in a start value to "enumerate" function

# for index, item in enumerate(courses, start=1):
# print(index, item)  # returns starting value as 1

# ~JOIN
# Turning lists into str's separated by a values
courses = ['Python', 'C#', 'Ruby', 'GIT']
# courses_str = ' - '.join(courses)
# print(courses_str)
# Returns {Python -C# -Ruby -GIT}

# ~SPLIT
# new_list = courses_str.split(' - ')  # split up the values on this space,
# print(new_list)
# Returns ['Python', 'C#', 'Ruby', 'GIT']

# TUPLES() & SETS{}
# similar to lists but can't modify them
# mutable eg: "lists" immutable eg: "turps"

# immutable- not many methods to use, can loop, access values.
# can't be modified
# tuple1 = ('Hugs', 'Food', 'Stuff')
# tuple2 = tuple1
# print(type(tuple1))
# print(tuple1)
# print(tuple2)
# if we were to try modify it:
# tuple1[1] = 'Cake' -it would return
# TypeError: 'tuple' object does not support item assignment
# pro tip- ctrl + / = comment out code fast

# ~SETS
# do not care about order and always change {} eg:
# set_list = {'home', 'food', 'sleep}
# print(set_list)
# results in:{'food', 'home', 'sleep'}
# main uses for a test is to test if a value is part of a set
# and to remove duplicate values eg:
# set_list = {'home', 'food', 'food', 'sleep'}
# print(set_list)
# returns with {'food', 'home', 'sleep'}
# Tests if a value is part of a set "membership test"
# Membership tests can be done with lists + tuples too
# Sets are optimized for this
# print(set_list)
# within print statement- eg
# print('home' in set_list)   # returns True

# ~INTERSECTION
# checks similarities in both sets eg:
# set_list = {'home', 'food', 'food', 'sleep'}
# inter_list = {'dogs', 'food', 'cats', 'sleep'}
# print(set_list.intersection(inter_list))
# returns: {'food', 'sleep'} as these are in the same set

# ~DIFFERENCE
# checks differences in sets eg:
# set_list = {'home', 'food', 'food', 'sleep'}
# inter_list = {'dogs', 'food', 'cats', 'sleep'}
# print(set_list.difference(inter_list))
# # returns: {'home'}

# ~UNION method
# print out all sets, conjoined together eg:
# set_list = {'home', 'food', 'food', 'sleep'}
# inter_list = {'dogs', 'food', 'cats', 'sleep'}
# print(set_list.union(inter_list))
# returns {'food', 'sleep', 'dogs', 'cats', 'home'}

# # Empty Lists
# empty_list = []
# empty_list = list()

# # Empty Tuples
# empty_tuple = ()
# empty_tuple = tuple()

# # Empty Sets
# empty_set = {}  # This isn't right! It's not an empty set its a dictionary
# empty_set = set()  # Right way to do it
