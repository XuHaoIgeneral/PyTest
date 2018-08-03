MINI14 = '1.4GHz Mac mini'
# class AppleFactory:
#     class MacMini14:
#         def __init__(self):
#             self.memory = 4  # in gigabytes
#             self.hdd = 500  # in gigabytes
#             self.gpu = 'Intel HD Graphics 5000'
#
#         def __str__(self):
#             info = ('Model: {}'.format(MINI14),
#                     'Memory: {}GB'.format(self.memory),
#                     'Hard Disk: {}GB'.format(self.hdd),
#                     'Graphics Card: {}'.format(self.gpu))
#             return '\n'.join(info)
#
#     def build_computer(self, model):
#         if model == MINI14:
#             return self.MacMini14()
#         else:
#             print("I don't know how to build {}".format(model))
#
#
# # 使用工厂
# afac = AppleFactory()
# mac_mini = afac.build_computer(MINI14)
# print(mac_mini)

# class Computer:
#     def __init__(self, serial_number):
#         self.serial = serial_number
#         self.memory = None      # in gigabytes
#         self.hdd = None         # in gigabytes
#         self.gpu = None
#
#     def __str__(self):
#         info = ('Memory: {}GB'.format(self.memory),
#                 'Hard Disk: {}GB'.format(self.hdd),
#                 'Graphics Card: {}'.format(self.gpu))
#         return '\n'.join(info)
#
#
# class ComputerBuilder:
#     def __init__(self):
#         self.computer = Computer('AG23385193')
#
#     def configure_memory(self, amount):
#         self.computer.memory = amount
#
#     def configure_hdd(self, amount):
#         self.computer.hdd = amount
#
#     def configure_gpu(self, gpu_model):
#         self.computer.gpu = gpu_model
#
#
# class HardwareEngineer:
#     def __init__(self):
#         self.builder = None
#
#     def construct_computer(self, memory, hdd, gpu):
#         self.builder = ComputerBuilder()
#         [step for step in (self.builder.configure_memory(memory),
#                         self.builder.configure_hdd(hdd),
#                         self.builder.configure_gpu(gpu))]
#
#     @property
#     def computer(self):
#         return self.builder.computer
#
# # 使用buidler，可以创建多个builder类实现不同的组装方式
# engineer = HardwareEngineer()
# engineer.construct_computer(hdd=500, memory=8, gpu='GeForce GTX 650 Ti')
# computer = engineer.computer
# print(computer)




# import copy
# from collections import OrderedDict
#
# class Book:
#     def __init__(self, name, authors, price, **rest):
#         '''Examples of rest: publisher, length, tags, publication
#         date'''
#         print("Name======",name)
#         print("Authors======",authors)
#         print("Price======",price)
#         print("Rest======",rest)
#         self.name = name
#         self.authors = authors
#         self.price = price      # in US dollars
#         self.__dict__.update(rest)
#
#     def __str__(self):
#         mylist = []
#         ordered = OrderedDict(sorted(self.__dict__.items()))
#         for i in ordered.keys():
#             mylist.append('{}: {}'.format(i, ordered[i]))
#             if i == 'price':
#                 mylist.append('$')
#             mylist.append('\n')
#         return ''.join(mylist)
#
#
# class Prototype:
#     def __init__(self):
#         self.objects = {}
#
#     def register(self, identifier, obj):
#         self.objects[identifier] = obj
#
#     def unregister(self, identifier):
#         del self.objects[identifier]
#
#     def clone(self, identifier, **attr):
#         """ 实现对象拷贝 """
#         found = self.objects.get(identifier)
#         if not found:
#             raise ValueError('Incorrect object identifier: {}'.format(identifier))
#         obj = copy.deepcopy(found)
#         obj.__dict__.update(attr)    # 实现拷贝时自定义更新
#         return obj
#
#
# def main():
#     b1 = Book('The C Programming Language', ('Brian W. Kernighan', 'Dennis M.Ritchie'),
#             price=118, publisher='Prentice Hall', length=228, publication_date='1978-02-22',
#             tags=('C', 'programming', 'algorithms', 'data structures'))
#
#     prototype = Prototype()
#     cid = 'k&r-first'
#     prototype.register(cid, b1)
#     b2 = prototype.clone(cid, name='The C Programming Language (ANSI)', price=48.99, length=274,
#                         publication_date='1988-04-01', edition=2)
#     for i in (b1, b2):
#         print(i)
#         print("ID b1 : {} != ID b2 : {}".format(id(b1), id(b2)))


class Computer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        """ call by client code """
        return 'execute a program'


class Synthesizer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} synthesizer'.format(self.name)

    def play(self):
        return 'is playing an electroinc song'


class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} human'.format(self.name)

    def speak(self):
        return 'says hello'


class Adapter:
    def __init__(self, obj, adapted_methods):
        """ 不使用继承，使用__dict__属性实现适配器模式 """
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


# 适配器使用示例
def main():
    objs = [Computer('Asus')]
    synth = Synthesizer('moog')
    objs.append(Adapter(synth, dict(execute=synth.play)))
    human = Human('Wnn')
    objs.append(Adapter(human, dict(execute=human.speak)))

    for o in objs:
        # 用统一的execute适配不同对象的方法，这样在无需修改源对象的情况下就实现了不同对象方法的适配
        print('{} {}'.format(str(o), o.execute()))


if __name__ == "__main__":
    main()


