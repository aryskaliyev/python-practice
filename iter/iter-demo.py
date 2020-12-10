# Iterators and Iterables
# https://www.youtube.com/watch?v=jTYiNjvnHZY

# Iterable - something that can be looped over.
# Tuples, lists, dictionaries, files, strings, generators etc.
# Something is an iterable if it has __iter__() special method.

# Iterator - an object with a state, so it remembers where it is during iteration.
# Generators are iterators as well, but __iter__() and __next__() are created automatically.
nums = [1, 2, 3]

# i_nums = nums.__iter__()
i_nums = iter(nums)

while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break

# print(i_nums)
# print(dir(i_nums))

# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# StopIteration exception
# print(next(i_nums))

# for num in nums:
#     print(num)

# print(dir(nums))
# print(next(nums))
