
# 函数名称：既是函数名，也是指向该函数的变量
#          只要是指向该函数，就可以调用该函数
def f1():
    print('f1函数')

f1()
f2 = f1
f2()
print()


# 函数嵌套
def fn():
    def fn2():
        print('fn2函数')

    return fn2


fn22 = fn()  # fn22=fn2
fn22()  # fn2()
print(fn22.__name__)  # fn2,说明fn22真实指向的是fn2函数



# 闭包：函数嵌套，且返回内部函数 就会形成闭包  (了解即可)
#      函数作用域中的变量x=10不会被释放

def fn3():
    x = 10

    def fn4():
        nonlocal x
        x += 1

        print('fn4函数内的x:', x)

    return fn4

f4 = fn3()  # f4=fn4
f4()  # fn4()  x=11
f4()  # fn4()  x=12
f4()  # fn4()  x=13




