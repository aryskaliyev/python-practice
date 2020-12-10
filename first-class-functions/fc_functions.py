# First-Class Functions
# https://www.youtube.com/watch?v=kr0mpwqttM0

# Assigning function to a variable. Not same as assigning result to a variable!
# If a function accepts other functions as arguments or returns functions as a result -- higher-order functions.
# def square(x):
#     return x * x

# f = square

# print(square)
# print(f(5))

# def cube(x):
#     return x * x * x
# Passes function as an argument.
# def my_map(func, arg_list):
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#     return result

# squares = my_map(square, [1, 2, 3, 4, 5])
# cubes = my_map(cube, [1, 2, 3, 4, 5])

# print(squares)
# print(cubes)

# Returns function as result of a function.
# def logger(msg):

#     def log_message():
#         print('Log: ', msg)

#     return log_message

# # Closure
# log_hi = logger('Hi!')
# print(log_hi)
# log_hi()

def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test headline!')
print_h1('Another headline!')

print_p = html_tag('p')
print_p('Test paragraph!')
