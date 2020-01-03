#定义一个简单的类
#使用class关键字来定义类
#class 类名（[父类]）：
# 代码块
class MyClass() :
    def say_hello(self):
        print('你好 ！ 我是 %s' %self.name)

#print(MyClass)
#使用MyClass 创建一个对象
mc = MyClass() #使用类来创建对象，就像调用一个函数一样 ，mc是Nyclass 的实例

#print(mc , type(mc))

#result = isinstance(mc ,MyClass)
#print(result)

#mc.name = 'swk'

#print(mc.name)

p1 = MyClass()
p1.name = "tom"
p1.say_hello()