class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
          return 'Node({!r})'.format(self._value)

    def addchild(self,node):
        self._children.append(node)


    def __iter__(self):
        return iter(self._children)


# example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.addchild(child1)
    root.addchild(child2)
    for c in root:
        print(c)
