
# def code(func):
#     data={}
#
#     def wrapper(n):
#         if n in data:
#             return  data[n]
#         else:
#             res=func(n)
#             data[n]=res
#             return res
#     return wrapper
#
# @code
# def fib(n):
#     if n<=2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
#
#
# for i in range(1,20):
#     print(fib(i))

class Fib(object):
    def __init__(self):
        pass

    def __call__(self, num):
        a, b = 0, 1;
        self.l = []

        for i in range(num):
            self.l.append(a)
            a, b = b, a + b
        return self.l

    def __str__(self):
        return str(self.l)

    __rept__ = __str__


f = Fib()
print(f(10))

