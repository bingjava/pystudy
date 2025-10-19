
# 作用域：变量起作用的范围
#   函数有作用域

# 全局变量：全局作用域，不会释放内存
a = 10

def fn():
    # 局部变量：局部作用域，退出作用域(函数)时会自动将变量占的内存释放掉
    b = 20
    print('b:', b)
    print('a:', a)

fn()
# print(b)  # 不能使用函数内部定义的局部变量
a = 30
fn()

# if语句,while,for循环： 没有作用域
# if True:
#     c = 100
# print('c:', c)
#
# i = 1
# while i:
#     d = 100
#     i -= 1
# print('d:', d)


# 函数嵌套
# 内建作用域 B： Built-in , 整个Python环境都可以使用
# 全局作用域 G： Global
# 函数作用域 E： EnClosing
# 局部作用域 L： Local


x = 3  # 全局作用域
def fn1():
    y = 4  # 函数作用域 E： EnClosing 闭包

    def fn2():
        z = 5  # 局部作用域 L： Local


print()
# 关键字： global，nonlocal

# global : 全局
m = 10
def f1():
    global m   # 声明使用的是全局变量m
    m += 4
    print('m:', m)

f1()
print('函数外的m:', m)


print()
# nonlocal : 在函数嵌套时才会使用
A = 3  # 全局作用域
def f2():
    A = 4  # 函数作用域

    def f3():
        # global A  # 声明使用的是全局作用域下的变量 A=3
        nonlocal A  # 声明使用的是函数作用域下的变量 A=4
        A = 5  # 局部作用域
        print('f3 的 A:', A)
    f3()

    print('f2 的 A:', A)


f2()
print('函数外的 A:', A)


