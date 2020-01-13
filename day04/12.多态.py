class A:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class B:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


a = A("sunwukong")
b = B('zhubajie')


def say_hello(obj):
    print('你好 %s' % obj.name)

def say_hellow_2(obj):
    if isinstance(obj,A):
       print('你好 %s' % obj.name)

say_hello(a)
