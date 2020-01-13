class A(object):
    count = 0

    def __init__(self):
        self.name = 'swk'

    # @classmethod修饰的方法属于类方法
    # 类方法第一个参数是cls,也会被自动传递
    @classmethod
    def test_2(cls):
        print('类方法')
    #静态方法
    @staticmethod
    def test_3():
        print("")


a = A()
print(a.count)
print(A.count)
