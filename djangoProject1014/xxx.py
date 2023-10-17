class Foo(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


obj = Foo('111')

# 输出对象是，想要定制现实的内容，需要重写__str__ 方法
print(obj)


