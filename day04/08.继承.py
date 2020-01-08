class Animal:
    def run(self):
        print('动物会跑')

    def sleep(self):
        print('动物睡觉~~~')


class Dog(Animal):
    def bark(self):
        print("wangwangwang~~~~")
d = Dog()

d.run()
d.bark()

