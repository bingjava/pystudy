
# 1.变量 : 可变的量
#   1. 作用是用来存储数据, 为了方便以后使用它做别的运算
#   2. 定义变量时,不需要固定类型(弱类型: 动态数据类型)

# 定义一个变量:
#   将10这个值 赋值 给变量a (a是我们自己取的变量名)
a = 10
print(a)

# 其他定义变量的方式:
a, b = 3, 4
print(a, b)  # 3 4

# 了解即可
c, *d, e = 1, 2, 3, 4, 5
print(c, d, e)  # c=1 d=[2, 3, 4] e=5


# 2. 交换2个变量的值[掌握]
h = 6
y = 8
# h = y  # h=8, y=8
# y = h  # h=8, y=8
h, y = y, h
print(h, y)  # 8 6


# 3. 变量命名规范(标识符): [掌握]
#   1.由数字,字母,下划线组成,且不能以数字开头
#   2.不能使用关键字
#   3.区分大小写
#   4.建议: 如果变量名是由多个单词组成,
#           则使用下划线连接 my_teacher 或 使用小驼峰 myTeacher
#   5.建议: 变量名称 尽量见名知义, 一般使用英文 或 英语单词简写 或 拼音

# 3abc = 100
a_bc = 100
_abc123 = 300

# if = 666

age = 55
Age = 66
print(age, Age)

my_teacher = 'jeff'

age = 30

# 4. 关键字
# import keyword
# print(keyword.kwlist)
# [
#  'False', 'None', 'True', 'and', 'as',
#  'assert', 'async', 'await', 'break',
#  'class', 'continue', 'def', 'del',
#  'elif', 'else', 'except', 'finally',
#  'for', 'from', 'global', 'if', 'import',
#  'in', 'is', 'lambda', 'nonlocal', 'not',
#  'or', 'pass', 'raise', 'return', 'try',
#  'while', 'with', 'yield'
#  ]

import keyword
print(keyword.kwlist)


# 能不能使用中文做变量名，虽然可以用，但是不建议
# 国家 = "中国"
# print(国家)

# α = 3
# β = 4
# print(α, β)

'''
练习：判断下面变量命名是否合法,并说明不合法的原因:
_jielun   合法
12world   不合法  不能以数字开头
int       合法，但是不建议
boy_girl  合法
input     合法，但不建议
if        不合法，是关键字
hello&world   不合法，不能使用特殊符号
abc@163    不合法，不能使用特殊符号
'''

int = 2
print(int)


# 补充变量
x = y = z = 1  # 不建议
print(x, y, z)

# 删除变量，不建议使用，Python中有内存回收机制
del  x
print(x)  # 变量删除后不可以再使用 NameError: name 'x' is not defined

