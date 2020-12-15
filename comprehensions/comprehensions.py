# Comprehensions: lists, dicts, sets, generator expressions
# https://www.youtube.com/watch?v=3dt4OGnU5sM&t=302s

# List Comprehensions
# nums = [1,2,3,4,5,6,7,8,9,10]

# I want 'n' for each 'n' in nums
# Regular for loop:
# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

# List comprehension:
# my_list = [n for n in nums]
# print(my_list)

# I want 'n*n' for each 'n' in nums
# Regular for loop:
# my_list = []
# for n in nums:
#     my_list.append(n*n)
# print(my_list)

# List comprehension:
# my_list = [n*n for n in nums]
# print(my_list)

# Using map + lambda:
# returns iterator.
# my_list = map(lambda n: n*n, nums)
# for i in my_list:
#     print(i)

# I want 'n' for each 'n' in nums if 'n' is even
# Regular for loop:
# my_list = []
# for n in nums:
#     if n%2 == 0:
#         my_list.append(n)
# print(my_list)

# List comprehension:
# my_list = [n for n in nums if n%2 == 0]
# print(my_list)

# Using map + filter:
# returns iterator.
# my_list = filter(lambda n: n%2 == 0, nums)
# for i in my_list:
#     print(i)

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
# Regular for loop:
# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter, num))
# print(my_list)

# List comprehension:
# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(my_list)

# Dictionary Comprehensions
# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# zip() returns iterator. Run print(help(zip)) for more info.
# print(list(zip(names, heros)))

# I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
# Regular for loop:
# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print(my_dict)

# Dict comprehesion:
# my_dict = {name: hero for name, hero in zip(names, heros)}
# print(my_dict)

# If name not equal to Peter
# my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
# print(my_dict)

# Set Comprehensions (unique values)
# nums = [10,9,1,1,2,3,3,3,4,5,5,6,6,6,7,7,8,9,9,10]

# Regular for loop:
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)

# Set comprehension:
# my_set = {n for n in nums}
# print(my_set)

# Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

# Using generator function
# def gen_func(nums):
#     for n in nums:
#         yield n*n

# my_gen = gen_func(nums)

# Using generator expression
my_gen = (n*n for n in nums)

for i in my_gen:
    print(i)
