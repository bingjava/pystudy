
# 私有属性不能继承：
#     私有属性只能在当前类内部使用

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有属性

    def eat(self):
        print('eat')


class Boy(Person):
    def __init__(self, name, age, sex):
        super().__init__(name, age)
        self.sex = sex

    def sleep(self):
        print('sleep')
        # print(self.__age)  # 在子类中不可以直接访问父类的私有属性
        self.eat()

boy = Boy('小明', 20, '男')
print(boy.name)
# print(boy.__age)  # 类外部不可以直接使用私有属性
boy.sleep()

