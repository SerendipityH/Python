class Rectangle:
    """
    表示矩形的类
    """

    def __init__(self, width, height):
        self.hidden_width = width
        self.hidden_height = height

    def get_width(self):
        return self.hidden_width

    def get_height(self):
        return self.hidden_height

    def set_width(self, width):
        self.hidden_width = width

    def set_height(self, height):
        self.hidden_height = height

    def get_area(self):
        return self.hidden_width * self.hidden_height


# r = Rectangle(2,5)
# r.set_height(3)
# print(r.get_area())

#可以为对象的属性使用双下划线开头，__xxx
#双下划线开头的属性，是对象的隐藏属性
#其实隐藏属性只不过Python自动为属性改了一个名字
# 实际上是将名字修改为了，_类名__属性名
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         self.__name = name
#
#
# p = Person('孙悟空', 90)
#
# #print(p.__name) __双下划线开头的属性是隐藏属性，无法通过对象访问
# #print(p._Person__name)
# print(p.get_name())


class Person:
    def __init__(self, name, age):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

p = Person('孙悟空', 90)

print(p._name)