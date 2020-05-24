# You want to take a slice of data produced by an iterator, but the normal slicing operator
# doesn’t work.
# The itertools.islice() function is perfectly suited for taking slices of iterators and
# generators.

# It’s important to emphasize that islice() will consume data on the supplied iterator.
# Since iterators can’t be rewound, that is something to consider. If it’s important to go
# back, you should probably just turn the data into a list first.

def count(n):
    while True:
        yield n
        n += 1


c = count(10)

#gives error
# for i in c[25:40]:
#     print(i)
#

import itertools as itt

for i in itt.islice(c, 10, 55,5):
    print(i)

