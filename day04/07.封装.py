class Person:
    def __init__(self, name,age):
        self._name = name
        self._age = age

    # property装饰器，用来将一个get方法，转化为对象的属性 ，可以使用get方法
    # 使用property装饰的方法，必须和属性名是一样的
    @property
    def name(self):
        print('get 方法执行了')
        return self._name

    # 使用setter方法的装饰器:@属性名.setter
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        self._age = age

p = Person('猪八戒',20)
p.name = '孙悟空'
p.age = 30
print(p.name,p.age)
