
# 1. 利用封装和继承的特性完成如下操作：
# 小学生：
#   属性： 姓名 学号 年龄 性别
#   行为： 学习 打架
#
# 中学生：
#   属性： 姓名 学号 年龄 性别
#   行为： 学习 谈恋爱
#
# 大学生：
#   属性： 姓名 学号 年龄 性别
#   行为： 学习 打游戏

# 调用：
# 创建小学生对象
#    调用学习的方法
#    打印内容为： xx 学习的内容为：语文 数学 英语
#
# 创建中学生对象
#    调用学习的方法
#    打印内容为： xx 学习的内容为：语数外 生物化 史地政
#
# 创建大学生对象
#    调用学习的方法：
#    打印内容为： 逃课中..


class Student:
    def __init__(self, name, num, age, score):
        self.name = name
        self.num = num
        self.age = age
        self.score = score

    def study(self):
        print('学习')

# 小学生
class Pupil(Student):
    def study(self):
        print(f'{self.name} 学习的内容为：语数外 生物化 史地政')

    def fight(self):
        print('打架')

# 中学生
class Middle(Student):
    def study(self):
        print(f'{self.name} 学习的内容为：语文 数学 英语')
    def love(self):
        print('谈恋爱')

# 大学生
class College(Student):
    def study(self):
        print(f'逃课中...')
    def game(self):
        print('玩游戏')



