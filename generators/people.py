# Generators
# https://www.youtube.com/watch?v=bD05uGo_sVI

import resource
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

# in kilobytes converted to megabytes
print ('Memory (Before): {}Mb'.format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person

# in seconds
# t1 = time.process_time()
# people = people_list(1000000)
# t2 = time.process_time()

t1 = time.process_time()
people = people_generator(1000000)
t2 = time.process_time()

print ('Memory (After) : {}Mb'.format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024))
print ('Took {} Seconds'.format(t2-t1))
