# Context Managers
# https://www.youtube.com/watch?v=-aKFBoZpiqA

# Regular way of working with files:
# f = open('sample.txt', 'w')
# f.write('This is just random text.\n')
# f.close()

# Using context managers:
# Can be used with class or function decorators.
# with open('sample.txt', 'w') as f:
#     f.write('This is just random text, using context managers.\n')

# Context manager using a class:
# class Open_File():
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode

#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file

#     def __exit__(self, exc_type, exc_val, traceback):
#         self.file.close()

# with Open_File('sample.txt', 'w') as f:
#     f.write('Testing\n')

# print(f.closed)

# Context manager using a function:
# Need to use contextlib module
# to import contextmanager decorator
# to decorate generator function.
# from contextlib import contextmanager

# @contextmanager
# def open_file(file, mode):
#     try:
#         f = open(file, mode)
#         yield f
#     finally:
#         f.close()

# with open_file('sample.txt', 'w')  as f:
#     f.write('Testing with decorator function.\n')

# print(f.closed)

# CD Example:
import os
from contextlib import contextmanager

# cwd = os.getcwd()
# os.chdir('Sample-Dir-One')
# print(os.listdir())
# os.chdir(cwd)

# cwd = os.getcwd()
# os.chdir('Sample-Dir-Two')
# print(os.listdir())
# os.chdir(cwd)

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with change_dir('Sample-Dir-One'):
    print(os.listdir())

with change_dir('Sample-Dir-Two'):
    print(os.listdir())
