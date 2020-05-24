
# The mere presence of the yield statement in a function turns it into a generator.


def frange(start, increment, stop):
    x = start
    while x < stop:
        yield x
        x += increment


for i in frange(10,0.5,15):
    print(i)


# Generators are iterators, a kind of iterable you can only iterate over once.
# Generators do not store all the values in memory, they generate the values on the fly:
#
# When you create a list, you can read its items one by one. Reading its items one by one is called iteration:
#
# Iteration is a process implying iterables (implementing the __iter__() method) and iterators (implementing the __next__() method).
# Iterables are any objects you can get an iterator from. Iterators are objects that let you iterate on iterables.
#
# https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
# BUT, you cannot perform for i in mygenerator a second time since generators can only be used once: they calculate 0, then forget about it and calculate 1, and end calculating 4, one by one.