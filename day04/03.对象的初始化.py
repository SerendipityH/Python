class Person:
    # 在类中可以定义一些特殊方法（魔术方法）
    # 特殊方法都是以__开始
    # 特殊方法不需要我们自己调用
    # 特殊方法将会在特殊的时刻自动调用
    def __init__(self, name):
       # print("init 方法执行了--")
        self.name = name

    def say_hello(self):
        print('大家好 ， 我是 %s' % self.name)


# p1 = Person()
# p1.name = '孙悟空'
# p1.say_hello()

p1 = Person('swk')
p2 = Person('zbj')
p3 = Person('shs')
# print(p1.name)
# print(p2.name)
# print(p3.name)

p1.say_hello()