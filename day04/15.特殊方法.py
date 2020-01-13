# 特殊方法都是使用__开头和结尾的
class Person(object):
    """
    """

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return 'Person [name=%s,age = %d]' % (self._name, self._age)


p1 = Person('swk', 18)
p2 = Person('ts', 20)
# 打印的是__str__的返回值
print(p1)
