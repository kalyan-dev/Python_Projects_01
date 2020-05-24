
# # Method 1
# with open('../Basics/somefile.txt') as f:
#     for line in f:
#          print(line)
#
#
# # method 2
# with open('../Basics/somefile.txt') as f:
#     try:
#         while True:
#             print(next(f), end= ' <>')
#     except  StopIteration:
#         pass

# method 3
with open('../Basics/somefile.txt') as f:
    while True:
        line = next(f, None)
        if line == None:
            break
        print(line, '<>')