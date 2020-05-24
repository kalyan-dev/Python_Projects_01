
# If you want a generator to expose extra state to the user, don’t forget that you can easily
# implement it as a class, putting the generator function code in the __iter__() method

from collections import deque

class linehistory:
    def __init__(self, lines, histlen):
        self.lines = lines
        self.history = deque(maxlen = histlen)

    def __iter__(self):
        for lineno,line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()




f = open("..\Basics\somefile.txt")
lh = linehistory(f,3)
for line in lh:
    # print(line)
    if "Python" in line:
        for lineno,line in lh.history:
            print('{}.{}'.format(lineno,line), end='<>')