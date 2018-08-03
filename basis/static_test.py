class TestStatic(object):
    def __init__(self,name=0,passwd=0):
        print("init")
        self.name=name
        self.passwd=passwd

    def get_init(self):
        return self.name,self.passwd

    @classmethod
    def set_init(cls,text):
        print("classmethod")
        name,passwd=text.split('-')
        a=cls(name,passwd)
        return a

    def func(self):
        print(self.name,self.passwd)


t=TestStatic.set_init("11-10")
t.func()



