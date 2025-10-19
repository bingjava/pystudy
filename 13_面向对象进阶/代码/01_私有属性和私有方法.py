
# 私有属性和私有方法： 在属性名或方法名前面添加2个下划线
# 公有属性和公有方法


class Girl:
    def __init__(self, name, age):
        # 公有属性
        self.name = name
        # 私有属性：
        #   1. 只能在当前类内部使用
        #   2. 属性名前面需要添加2个下划线
        self.__age = age

    # 公有方法
    def dance(self):
        print(f'{self.name}今年{self.__age}岁了，会跳舞了!')
        self.__sing()  # 在当前类内部可以使用

    # 私有方法
    def __sing(self):
        print(f'{self.name} 会唱歌')


# 对象
g1 = Girl('刘亦菲', 18)
print(g1.name)
# print(g1.__age)  # 私有属性，不可以在类外部调用
g1.dance()
# g1.__sing()  # 私有方法，不可以在类外部调用

# 扩展: 不建议使用，把私有属性当做私有，不建议使用下面的方式调用
# 特殊: 可以通过内部的属性调用：_类名__age
# print(g1._Girl__age)
# g1._Girl__sing()
