''' '''

import math

# 包 package : 是一个有__init__.py文件夹
# 模块 module: 是一个python文件

# 封装思路: 项目 => 包(文件夹) => 模块(python文件) => 类 => 函数 => 代码

# 创建包
# 创建模块

# 导入模块
#   import
#   from - import

# import time, math, random
import time
import math
import random

# 精确导入
from time import sleep
sleep(0.1)

# 模糊导入 : * 表示所有内容
from time import *
print(time())
print()


# 自定义模块: 模块是单例模式(导入多次，
'''
import module1
import module1

print(module1.name)
module1.fn1()
'''

'''
from module1 import name,fn1
print(name)
# print(module1.name)  # 报错
fn1()
'''


# 模块在包中
'''
# from package1 import module2
# print(module2.name)

from package1.module2 import name
print(name)
'''


# 别名: as 改名后只能用别名
import module1 as m1
print(m1.name)

from package1 import module2 as m2
print(m2.name)

