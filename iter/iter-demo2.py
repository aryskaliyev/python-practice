# Iterators and Iterables
# https://www.youtube.com/watch?v=jTYiNjvnHZY

class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

# Generator function
def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


# nums = MyRange(1, 10)
nums = my_range(1, 10)

# print(dir(nums))

for num in nums:
    print(num)
