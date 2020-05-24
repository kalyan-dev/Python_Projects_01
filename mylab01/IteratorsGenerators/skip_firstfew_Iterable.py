# You want to iterate over items in an iterable, but the first few items aren’t of interest and
# you just want to discard them.


# skip the first few/the commnetd lines and read the other lines from a file

from itertools import dropwhile

# with open("./sample2.txt") as f:
#     for line in dropwhile(lambda line: line.startswith('#'), f):
#         print(line, end = ' ')


#lambda in for
with open('./sample2.txt') as f:
    lines = (line for line in f if not line.startswith('#'))
    for l in lines:
        print(l)


# if we know the exact number of items/lines to be skipped,

from itertools import islice

items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items[2:], 3, None):
    print(x)

