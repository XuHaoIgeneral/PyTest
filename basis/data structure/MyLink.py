
class Node():
    def __init__(self, next=None, prev=None, key=None, value=None):
        self.next = next
        self.prev = prev
        self.key = key
        self.value = value

class LinkList():
    def __init__(self):
        node = Node()
        node.next, node.prev = node, node
        self.node = node   #链表的node节点
        self.count = 0     #链表中技术

    def headlink(self):
        return self.node.next

    def taillink(self):
        return self.node.prev

    def getbyindex(self,index):
        pass

    def push(self,**kwargs):
        print(kwargs["key"])
        nextnode=Node(key=kwargs["key"],value=kwargs['value'])
        nextnode.prev=self.node
        self.node.next=nextnode
        print(self.node,next())


a=LinkList()
print(a.push(key="a",value="va"))



