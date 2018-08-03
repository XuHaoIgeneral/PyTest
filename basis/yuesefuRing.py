class MyClass(object):

    data = "This is class data"
    
    def instance_method(self):
        print("实例方法，只能被实例对象调用，可以访问实例属性%s" % self.data)

    @staticmethod
    def static_method():
        print("是静态方法,不能访问类属性或者实例属性")

    @classmethod
    def class_method(cls):
        print("是类方法，可以访问类属性%s" % cls.data)

m = MyClass()
m.data = "this is m"
m.instance_method()
m.static_method()
m.class_method()

MyClass.static_method()
#
#
MyClass.class_method()
#
#
# MyClass.instance_method()