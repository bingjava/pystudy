

# 重写: 方法重写，在继承的基础上，子类和父类有一样的方法名称。

class Person:
    def run(self):
        print('Person父类中的run')

class Boy(Person):
    pass
    # 重写：方法重写，在子类中写一个和父类一样方法名的方法
    #     会优先调用子类的run
    def run(self):
        print('Boy子类中的run')


boy = Boy()
boy.run()

# p = Person()
# p.run()
