class Sentence:

    def __init__(self, sentence):
        lst = sentence.split()
        for word in lst:
            if word == '':
                lst.remove(word)
        self.lst = lst
        self.start = 0
        self.end = len(self.lst)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current = self.lst[self.start]
        self.start += 1
        return current

# Generator function
def gen_sent(sentence):
    lst = sentence.split()
    for word in lst:
        if word == '':
            lst.remove(word)
    return (word for word in lst)

def sentence(sentence):
    for word in sentence.split():
        yield word

# my_sentence = Sentence('This is a test')
# my_sentence = gen_sent('This is a test ')
my_sentence = sentence('This is a test ')

# for word in my_sentence:
#     print(word)

print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
