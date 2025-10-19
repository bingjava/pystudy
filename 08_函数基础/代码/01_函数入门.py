''''''

# 封装思路:
#    项目 => 文件夹(包) => 文件(模块) => 类 => 函数 => 代码



'''
问题: 代码重复
     后期维护成本太高
	 代码可读性不高

解决问题：函数
	在一个完整的项目中，某些功能会被反复使用，那么将这部分功能对应的代码提取出来，
	当需要使用功能的时候直接使用
	
本质：对一些特殊功能的封装

优点：
	a.简化代码结构，提高应用的效率
	b.提高代码复用性
	c.提高代码的可读性和可维护性

建议：但凡涉及到功能，都尽量使用函数实现
'''

# 数学中的函数
#  f(x) = 3x + 1
#  f(x) = 4x + 5


# 函数定义 : def
def fn():
    print('我是函数')


# 函数必须调用才会执行
fn()
fn()
fn()


# 一.函数的参数(必须要掌握)
#  形参: 形式参数, 比如：a, b
#  实参: 实际参数, 比如：5，6
def sum(a, b):
    print(f'a:{a}, b:{b}')
    # 返回a+b的值
    return a + b

# 调用时会将 5赋值给a，6赋值给b
n = sum(5, 6)
print(n)  # 11
print()

# 细分参数种类:
#  1. 必需的位置参数, a, b
#  2. 默认参数, c=7
#  3. 关键字参数, 一般和默认参数结合,

def fn1(a, b,  c=7, d=8):
    print(f'a:{a}, b:{b}, c:{c}, d:{d}')

fn1(5, 6)
fn1(5, 6,  c=77, d=88)
fn1(5, 6,  d=88)
fn1(5, 6,  88)


# 4. 不定长参数
#  *args: 接收任意多个位置参数, 元组
#  **kwargs: 接收任意多个关键字参数, 字典
# args: arguments 参数的意思
# kwargs: keyword arguments 关键字参数的意思

#  *args: 接收任意多个位置参数, 元组
#  **kwargs: 接收任意多个关键字参数, 字典
def fn2(*args, **kwargs):
    print(args)  # (4, 5)
    print(kwargs)  # {'c': 77, 'd': 88}

fn2(4)
fn2(4, 5,  c=77, d=88)
print()

# 二.返回值: return
#  1. return要写在函数内部, 返回 值
#  2. 如果不写return则默认会返回None
#  3. return会立刻结束函数,并返回值

def fn3(a, b):
    s = a + b
    # return   # 写return，不写值，表示立刻结束函数，返回None
    return s
    print('我在return后面，我永远不会执行')

n = fn3(1, 2)
print(n)
print()


# 函数参数顺序
#   形参顺序: 位置参数，*args,     默认参数，**kwargs
#   实参顺序: 位置参数，           关键字参数
def fn(a, b, *args,     d=7, e=8, **kwargs):
    print(a, b, args)  # 2 3 (4, 5)
    print(d, e, kwargs)  # 77 88 {'f': 99, 'g': 100}

fn(2, 3, 4, 5,    d=77, e=88, f=99, g=100)


# 通用参数
def fun(*args, **kwargs):
    print(args, kwargs)

fun(2, 3, 4, 5,    d=77, e=88, f=99, g=100)


