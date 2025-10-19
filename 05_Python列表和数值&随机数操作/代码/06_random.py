
# random: 随机数

# import keyword
# import math
# import time
import random

# random.choice(): 从列表/str中随机取一个元素
girl_friends = ["刘亦菲", '迪丽热巴', '如花', '凤姐', '欧阳娜娜']
print(random.choice(girl_friends))
print(random.choice("abc"))
print(random.choice(range(1, 7)))  # 筛子

# random.randint(a, b): 从一个范围随机取一个整数，闭区间
print(random.randint(3, 5))  # 从[3,5]之间去一个随机值

# random.randrange(a, b, step): 随机获取一个奇数，和range类似
# print(random.randrange(3, 5))  # 在[3,5)范围取一个随机值
# print(random.randrange(2, 9, 2))  # 在2,4,6,8中取一个随机值


# random.random() : 在0~1之间[0,1)随机获取一个小数
print(random.random())  # 在0~1之间[0,1)随机获取一个小数
# print(1 + random.random() * 9)  # 得到一个1-10之间的小数


# random.uniform(3, 5) ： 3~5之间的小数 （了解）
print(random.uniform(3, 5))  #  [3, 5)
print(random.uniform(3, 3))  # [3, 3]
'''
def uniform(self, a, b):
    "Get a random number in the range [a, b) or [a, b] depending on rounding."
    return a + (b - a) * self.random()
'''


# random.shuffle(list) : 随机打乱顺序  （了解）
# nums = [1, 2, 3, 4, 5]
# random.shuffle(nums)  # 把列表nums打乱顺序
# print(nums)


