class Dog:
    """
    表示狗的类
    """

    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def bark(self):
        """
         狗叫的方法
        """
        print('汪汪汪 。。。')

    def run(self):
        """
        跑的方法
        :return:
        """
        print('%s 在快乐的奔跑' % self.name)


d = Dog('旺财', 1, 'male', 30)
d.run()
