import math


# 利用面向对象的思想写下面的程序：直接赋值

# 1.小明穿着白色的特步运动鞋在奥林匹克公园跑步
#   Person类
#      属性：name
#      方法：run(self, place, shoes)
class Person:
    def __init__(self, name):
        self.name = name

    def run(self, place, shoes):
        print(f'{self.name}穿着{place}在{shoes}跑步')

p = Person('小明')
p.run('奥林匹克公园', '白色的特步运动鞋')


# 2.王梅家的荷兰宠物猪【笨笨】跑丢了，她哭着贴寻猪启示。
#   Person2类
#      属性：name
#      方法：find_pig(self, pig)

class Person2:
    def __init__(self, name):
        self.name = name

    def find_pig(self, pig):
        print(f'{self.name}家的{pig.place}宠物猪【{pig.name}】跑丢了，她哭着贴寻猪启示')

class Pig:
    def __init__(self, name, place):
        self.name = name
        self.place = place

pig = Pig('笨笨', '荷兰')
p2 = Person2('王梅')
p2.find_pig(pig)



# 3. 定义一“圆”（Circle）类，圆心为“点”Point类，构造一圆，求圆的周长和面积，并判断某点与圆的关系
# 圆类Circle:
#     属性: 半径r,圆心(Point对象)
#     方法: 周长,面积
#
# 点类Point:
#   属性: x,y
#   方法: 与圆的关系(在圆内/在圆外/在圆上)

class Circle:
    def __init__(self, r, point):
        self.r = r
        self.point = point
    def C(self):
        print(2 * self.r * 3.14)
    def S(self):
        print(3.14 * self.r ** 2)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def ralation(self, circle):
        # 勾股定理： c = math.sqrt(a**2 + b**2)
        distance = math.sqrt((self.x - circle.point.x) **2 + (self.y - circle.point.y) **2)
        if distance == circle.r:
            print('在圆上')
        elif distance > circle.r:
            print('在圆外')
        else:
            print('在圆内')

circle = Circle(5, Point(0, 0))
circle.C()
circle.S()

point = Point(3, 4)
point.ralation(circle)



# 4. 使用面向对象的思想，创建下面的类，对象
#
#  有一个银行账户类 Account,
#     属性包括: 名字name , 余额balance属性
#    方法有：存钱 save_money(self,money)、
#           取钱 get_money(self,money)、
#           查询余额 show_balance(self)。
#    要求：取钱时，要判断余额是否充足，余额不够的时候要提示余额不足

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def save_money(self, money):
        self.balance += money

    def get_money(self, money):
        if self.balance < money:
            print('余额不足!')
            return 0
        else:
            self.balance -= money
            return money

    def show_balance(self):
        return self.balance

account = Account('马云', 10000)
account.save_money(1000)
print(account.show_balance())


m = account.get_money(10000)
print(m)
print(account.show_balance())
