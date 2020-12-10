# Closures
# https://www.youtube.com/watch?v=swU3c34d2NQ

# A Closure - is an inner function that remembers and has access to variables in the local scope in which it was created, even after the outer function has finished executing.

# Pass functions as an argument.
# Assign functions to a variable.
# Return functions as a result.
def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func

hi_func = outer_func('Hi')
hello_func = outer_func('Hello')

hi_func()
hello_func()
