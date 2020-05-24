# Reversed iteration only works if the object in question has a size that can be determined
# or if the object implements a __reversed__() special method. If neither of these can
# be satisfied, you’ll have to convert the object into a list first


# with open('..\Basics\somefile.txt') as f:
#     for line in reversed(list(f)):
#         print (line)
#
# simple version, for default things
# l = [3,4,5,324,342,54]
# for n in reversed(l):
#     print(n)
# print(l)


class countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        i = self.start
        while i > 0:
            yield i
            i -= 1

    def __reversed__(self):
        i = 1
        while i <= self.start:
            yield i
            i += 1

    def __repr__(self):
        return self.start


n = countdown(12)
# for x in n:
#     print(x)

for x in reversed(n):
    print(x)
