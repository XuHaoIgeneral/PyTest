"""

"""

class Bag(object):
    def __init__(self, maxsize=10):
        self.maxsize = maxsize
        self._items = list()

    def add(self, value):
        print(len(self))
        print(len(self._items))
        if len(self) > self.maxsize:
            raise Exception("Bag is full")
        self._items.append(value)

    def remove(self, value):
        if value not in self._items:
            raise Exception("value not in Bag")
        return self._items.remove(value)

    def __len__(self):
        print("a")
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item

def test_bag():
    bag = Bag()

    bag.add(1)
    bag.add(2)
    bag.add(3)
    assert len(bag) == 3

    bag.remove(3)
    assert len(bag) == 2



