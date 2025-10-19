
# 作用是让 函数可以变成属性的方法来调用
#   1.必须有返回值， 2.没有参数
# @property  # (掌握)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # getter：用来获取值
    @property
    def age(self):
        return self.__age

    # setter： 用来修改值
    # @age.setter   # 了解
    # def age(self, new_age):
    #     if new_age > 0:
    #         self.__age = new_age


# 对象
p = Person('张三', 33)
print(p.age)

# p.age = 18  # setter功能
# print(p.age)


