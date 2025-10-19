
# 单继承： 只有1个父类
# 多继承： 多个父类 （了解）

# 2个父类： 父亲，母亲
# 1个子类： 儿子

class Father:
    def __init__(self, name):
        self.name = name
    def smoke(self):
        print('会抽烟')

class Mother:
    def __init__(self, age):
        self.age = age
    def cook(self):
        print('会做饭')

# 子类
class Son(Father, Mother):
    def __init__(self, name, age, sex):
        # Father.__init__(self, name)  # 显式调用
        # Mother.__init__(self, age)
        
        # super(Son, self).__init__(name)
        super().__init__(name)  # 隐式调用
        super(Father, self).__init__(age)

        self.sex = sex

    def play_game(self):
        print('会玩游戏')

son = Son('小红', 20, '男')
print(son.name, son.age, son.sex)
son.smoke()
son.cook()
son.play_game()

# 继承链
print(Son.__mro__)
# (<class '__main__.Son'>,
#  <class '__main__.Father'>,
#  <class '__main__.Mother'>,
#  <class 'object'>
#  )
