
# 类和对象
#   类是对象的抽象，class, 同一类事物的统称
#   对象是类的具体，object, 需要通过类来创建
#
#   类：不占内存
#   对象：占内存，不同对象占不同内存

#   类         对象
#   人          我
#  电脑       你的那台华为电脑
#  华为电脑    你的那台华为电脑
#  男朋友      你的这个男朋友

# 一个类可以创建任意多个对象
# 比如：工厂生产华为手机的模型就是类
#      生产的每一部具体的手机就是一个对象


# 自定义类
#   所有的类都会默认继承object
class Person(object):
    # 属性：变量，静态的，表示一些特征，比如：名字，年龄，身高，
    # 类属性：一般用类名来调用
    # name = "Jack"  # 值固定
    # age = 30

    # 方法：初始化方法，构造方法
    #   1.作用是用来初始化属性值
    #   2.会在创建对象时自动被调用
    def __init__(self, name, sex):
        # 对象属性：成员属性，对象来调用
        self.name2 = name
        self.sex2 = sex

    # 方法：函数，动态的，表示功能，比如：打篮球，跑步，看电影，游戏
    def run(self):
        print(self.name2, "在跑步")


# 创建对象
p = Person("杰伦", '男')
print(p.name2, p.sex2)
p.run()

p2 = Person('昆凌', '女')
print(p2.name2, p2.sex2)
p2.run()


# 练习
# 1.创建Phone类
#      属性：color, size, price
#      方法：call, play_game, chat

class Phone:
    def __init__(self, color, size, price):
        self.color = color
        self.size = size
        self.price = price

    def call(self):
        print('call')
    def play_game(self):
        print('play game')
    def chat(self):
        print('chat')

iphone16 = Phone('黑色', 6, 8000)
print(iphone16.color, iphone16.size, iphone16.price)



# 2.小美在朝阳公园溜旺财【注：旺财是狗】
#   类People：
#       属性：姓名 name
#       方法：溜旺财 walk_dog
#            def walk_dog(self, place, dog_name):
#                   小美 在 朝阳公园 溜 旺财

class People:
    def __init__(self, name):
        self.name = name

    def walk_dog(self, place, dog_name):
        print(f'{self.name}在{place}溜{dog_name}')


xiaomei = People('小美')
xiaomei.walk_dog('朝阳公园', '旺财')

