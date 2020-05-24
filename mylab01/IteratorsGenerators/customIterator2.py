
# Python’s iterator protocol requires __iter__() to return a special iterator object that
# implements a __next__() operation and uses a StopIteration exception to signal
# completion.
#
# Define  your iterator as a generator and be done with it.
#     the     depth_first()     method is simple    to    read and describe.It    first    yields    itself and then    iterates    over    each    child    yielding
#     the    items    produced    by    the    child’s    depth_first()    method(using    yield from).


class Node:
    def __init__(self,value):
        self._value = value
        self._children = []


    def __repr__(self):
        return 'Node({!r})'.format(self._value)


    def __iter__(self):
        return iter(self._children)

    def addchild(self,node):
        self._children.append(node)


    def depthfirst(self):
        yield self
        for c in self._children:
            yield from c.depthfirst()


# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.addchild(child1)
    root.addchild(child2)
    child1.addchild(Node(3))
    child1.addchild(Node(4))
    child2.addchild(Node(5))
    for ch in root.depthfirst():
        print(ch)
# Outputs Node(0),