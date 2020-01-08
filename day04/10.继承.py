class Animal:
    def __init__(self, name):
        self._name = name;

    def run(self):
        print('动物会跑')

    def sleep(self):
        print('动物睡觉~~~')

    @property
    def name(self):
        return self._name;

    @name.setter
    def name(self, name):
        self._name = name;


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self._age = age

    def bark(self):
        print("wangwangwang~~~~")

    def run(self):
        print('狗跑!!!!!!!')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


d = Dog('旺财',18)
print(d.name)
print(d.age)
