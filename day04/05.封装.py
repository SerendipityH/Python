class Dog:
    """
    表示狗的类
    """

    def __init__(self, name, age):
        self.hidden_name = name
        self.hidden_age = age

    def say_hello(self):
        print('大家好，我是 %s' % self.hidden_name)

    def get_name(self):
        """
         get_name()用来获取对象的name属性
        :return:
        """
        return self.hidden_name

    def set_name(self, name):
        self.hidden_name = name

    def get_age(self):
        return self.hidden_age

    def set_age(self, age):
        if age > 0:
            self.hidden_age = age


# d = Dog('旺财')
#
# d.name = '小黑'
#
# d.say_hello()
#
# d.set_name('小黑')
# d.say_hello()
# print(d.get_name())

d = Dog('小黑', 6)

d.set_age(7);

print(d.get_age())
