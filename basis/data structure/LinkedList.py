class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.length = 0
        self.tailnode=None

    def __len__(self):
        return self.length

    def append(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception("LinkedList is Full!")
        node=Node(value)
        tailnode=self.tailnode
        if tailnode is None:
            self.root.next=node
        else:
            tailnode.next=node
        self.tailnode=node
        self.length+=1

    def appendlelf(self,value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception("LinkedList is Full!")
        node=Node()
        headnode=self.root.next
        self.root.next=node
        node.next=headnode
        self.length+=1

    def iter_node(self):
        curnode=self.root.next
        while curnode is not self.tailnode:
            yield curnode
            curnode=curnode.next
        yield curnode    #因为到了最后一个为tailnode 在while循环中不能yield

    def __iter__(self):
        for node in self.iter_node():
            yield node

    def remove(self,value):
        prevnode=self.root
        curnode=self.root.next
        while curnode.next is not None:
            if curnode.value==value:
                prevnode.next=curnode.next
                del curnode
                self.length-=1
                return
            else:
                prevnode=prevnode.next

    def find(self,value):
        index=0
        for node in self.iter_node():
            if node.value==value:
                return index
            index+=1
        return -1

    def popleft(self):
        if self.root.next is None:
            raise Exception("POP from empty LinkedList")
        headnode=self.root.next
        self.root.next=headnode.next
        self.length-=1
        value=headnode.value
        del headnode
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next=None
        self.length=0


def test_LinkedList():
    pass