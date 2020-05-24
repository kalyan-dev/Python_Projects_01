
from collections import deque


def search(lines, pattern, history=2):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
            previous_lines.append(line)


# Example use on a file
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'Python', 2):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)


q1 = deque(maxlen=3)
q2 = deque()

q1.append(4)
q1.append(5)
q1.append(6)
q1.append(7)
print(q1)

q2.append(4)
q2.append(5)
q2.append(6)
q2.append(7)
print(q2)
