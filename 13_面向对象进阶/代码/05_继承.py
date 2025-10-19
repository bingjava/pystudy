
# 面向对象的4大特征：
#   1. 封装：属性和方法
#   2. 继承：子类可以继承父类的属性和方法
#   3. 多态
#   4. 抽象


# 继承：子类继承父类的属性和方法
#    方便后期维护代码

# 单继承 ： 只有1个父类

# 父类：基类
class IPad:
    def __init__(self, color, price):
        self.color = color
        self.price = price

    def movie(self):
        print('看电影')


# 子类
class IPhone(IPad):
    def __init__(self, color, price, size):
        super().__init__(color, price)  # 调用父类的init方法，来初始化color和price
        # IPad.__init__(self, color, price)  # 借用父类的构造函数init
        self.size = size

    def call(self):
        print('可以打电话')

phone16 = IPhone('红色', 8000, 6)
print(phone16.color, phone16.price, phone16.size)
phone16.call()
phone16.movie()


# 继承的使用场景
#   1. 子类在父类的基础上，额外扩展功能
#   2. 将 不同子类的公共属性和方法 提取出来，成为一个父类
#    比如： Dog, Cat
#        Dog类： name,age   sleep   和Dog额外的功能
#        Cat类： name,age   sleep   和Cat额外的功能
#     我们可以把Dog类和Cat类的公共属性和方法提取出来，用Animal类来封装，作为父类，
#     再让Dog和Cat继承 Animal
#
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print('爱睡觉')

#子类Dog
class Dog(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age)
        self.sex = sex

    def eat(self):
        print('狗爱吃骨头')

# 子类Cat
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def catch_mouse(self):
        print('猫会抓老鼠')

# 对象
dog = Dog('旺财', 3, '公')
print(dog.name, dog.age, dog.sex)
dog.sleep()
dog.eat()

cat = Cat('加菲猫', 10, '黄色')
print(cat.name, cat.age, cat.color)
cat.sleep()
cat.catch_mouse()
