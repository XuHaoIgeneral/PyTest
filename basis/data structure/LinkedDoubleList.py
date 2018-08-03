class Node(object):
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class LinkedDoubleList(object):
    def __init__(self, maxsize=None):
        node = Node()
        node.prev, node.next = node, node
        self.root = node
        self.maxsize = maxsize
        self.length = 0

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception("LinkedDoubleList is Full")

        node = Node(value=value)
        tailnode = self.tailnode()

        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception("LinkedDoubleList is Full")
        node = Node(value=value)
        if self.root.next == self.tailnode():
            node.next = self.root
            node.prev = self.root
            self.root.next = node
            self.root.prev = node
        else:
            headnode = self.headnode()
            node.next = headnode
            node.prev = self.root
            self.root.next = node
        self.length += 1

    def remove(self, value):
        if value == None:
            raise Exception("layed")
        for node in self.iter_node():
            if node.value == value:
                prevnode = node.prev
                nextnode = node.next
                prevnode.next, nextnode.prev = nextnode, prevnode
                del node
                self.length -= 1

    def iter_node(self):
        curnode = self.root.next
        tailnode = self.root.prev
        while curnode is not tailnode:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def __len__(self):
        return self.length


def test_LinkDouble():
    a = LinkedDoubleList()
    a.append(1)
    a.append(2)
    a.append(3)
    assert list(a) == [1, 2, 3]
    a.appendleft(0)
    assert list(a) == [0, 1, 2, 3]
    a.remove(0)
    a.remove(3)
    assert list(a) == [1, 2]
    a.append(4)
    assert list(a) == [1, 2, 4]
