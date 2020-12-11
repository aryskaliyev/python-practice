# Decorators
# https://www.youtube.com/watch?v=FsAPt_9Bf3U&t=27s

# A decorator is a function that takes another function as an argument, adds some kind of functionality and then returns another function, without altering the source code of original function that was passed in.
# Classes as decorators and functions as decorators.
# def outer_function(msg):
#     def inner_function():
#         print(msg)
#     return inner_function

# hi_func = outer_function('Hi')
# bye_func = outer_function('Bye')

# hi_func()
# bye_func()

# Decorator Function
# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print('wrapper executed this before {}'.format(original_function.__name__))
#         return original_function(*args, **kwargs)
#     return wrapper_function # waiting to be executed

# Decorator Class
# class decorator_class(object):

#     def __init__(self, original_function):
#         self.original_function = original_function

#     def __call__(self, *args, **kwargs):
#         print('call method executed this before {}'.format(self.original_function.__name__))
#         return self.original_function(*args, **kwargs)

from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper

def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

# @decorator_function
# def display():
#     print('display function ran')

# decorated_display = decorator_function(display)
# decorated_display()
# display()

import time

@my_logger
@my_timer
def display_info(name, age):
    time.sleep(3)
    print('display_info ran with arguments ({}, {})'.format(name, age))

# display_info = my_logger(my_timer(display_info))

display_info('Jeff', 33)
