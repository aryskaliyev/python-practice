# Generators
# https://www.youtube.com/watch?v=bD05uGo_sVI

# Regular function
# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result

# Generator function.
# Generators do not hold entire result in memory.
# It yields one result at a time.
# def square_numbers(nums):
#     for i in nums:
#         yield (i*i)

# my_nums = square_numbers([1,2,3,4,5])

# List comprehension example: returns list.
# my_nums = [x*x for x in [1,2,3,4,5]]

# List comprehension: returns generator object.
my_nums = (x*x for x in [1,2,3,4,5])

print(list(my_nums))
# print(my_nums)
# print(next(my_nums))

# for num in my_nums:
#     print(num)
