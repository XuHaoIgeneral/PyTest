class Array(object):

    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, value):
        return self._items[value]

    def __setitem__(self, key, value):
        self._items[key] = value

    def __len__(self):
        return self._size

    def clear(self,value=None):
        for item in range(self._size):
            self._items[item]=value

    def __iter__(self):
        for item in self._items:
            yield item


def test_Array():
    size=20
    a=Array(size)
    a[0]=1
    assert a[0]==1
    a.clear()
    assert a[0]==None