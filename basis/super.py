class first(object):
    def __init__(self, value):
        self.value = value


class second(first):
    def __init__(self, value):
        super(__class__, self).__init__(value)
        print(self.value,"vv")
        self.value += 8


class third(first):
    def __init__(self, value):
        super(__class__, self).__init__(value)
        print(self.value,"aa")
        self.value += 7


class four(second, third):
    def __init__(self, value):
        # second.__init__(self, value)
        # third.__init__(self, value)
        # super(second, self).__init__(value)
        super(__class__, self).__init__(value)

test=four(5)
print(test.value)