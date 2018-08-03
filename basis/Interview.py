# def singleton(cls):
#     instances = {}
#     a=[]
#     def getinstance(*args, **kw):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kw)
#         return instances[cls]
#     return getinstance
#
# @singleton
# class MyClass:
#     def __init__(self,a):
#         self.a=a
#
#     def run(self):
#         print(self.a)
#
#
# test=MyClass("aaa")
# test.run()

# x=1
# def external():
#     x = 10
#     def internal():
#         nonlocal x
#         x += 1
#         print(x)
#     internal()
#
# external()

