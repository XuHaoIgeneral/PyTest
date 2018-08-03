class Test(object):

    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day
        print("初始化", self.year, self.month, self.day)

    def out_date(self):
        self.is_year()
        print("year:", self.year)
        print("month:", self.month)
        print("day:", self.day)

    @classmethod
    def get_data(cls, string_date):
        # 这里第一个参数是cls， 表示调用当前的类名
        year, month, day = map(int, string_date.split('-'))
        print(year, month, day)
        date1 = cls(year, month, day)
        # 返回的是一个初始化后的类
        return date1

    @staticmethod
    def is_year():
        print("这是一次测试")

# t = Test(2017, 4, 24)
# t.out_date()


# 提升class的可扩展性
r = Test.get_data("2018-4-25")
r.out_date()
r.is_year()


# Test.is_year()
# Test.get_data("2018-4-25")
