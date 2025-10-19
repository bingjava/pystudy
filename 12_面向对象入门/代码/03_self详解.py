

# self:
#   1.不是关键字, 只是一个形参，但是建议写self, 不需要给self传值
#   2.self是指向当前类的对象（哪个对象调用函数，则该函数中的self就是这个对象）
#   3.作用是让你可以在函数中调用类中的其他属性或方法


class Dog:
    def __init__(self, name):
        self.name = name
        print('__init__函数中的self:', id(self))

    def eat(self):
        print(self.name, '喜欢吃骨头！')
        print('eat函数中的self:', id(self))

# 创建对象
dog = Dog('旺财')
# print(dog.name)
dog.eat()
print('id(dog):', id(dog))  # id():内存地址
print('*' * 100)

dog2 = Dog('大黄')
dog2.eat()
print('id(dog2):', id(dog2))

