class A(object):
    def test(self):
        print("AAA")
class B(object):
    def test(self):
        print('B中的test()方法')
    def test2(self):
        print("BBB")

#在Python中是支持多重继承的
# 可以在类名的()后边添加多个类，来实现多重继承
#前面父类的方法会覆盖后边类的方法
class C(A,B):
    pass

#print(C.__bases__)

c = C()

c.test()