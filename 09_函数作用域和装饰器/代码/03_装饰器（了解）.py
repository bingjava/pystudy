

# 装饰器：
#     作用是在其他函数的前面或后面添加功能，但是不修改原函数

def swim():
    print('我爱游泳')

def swim2():
    print('先跳个舞')
    swim()
    print('再唱个歌')


# 上面的方式有缺陷：只能给swim添加功能

def run():
    print('我爱跑步')


def run2(fn):
    print('先跳个舞')
    fn()
    print('再唱个歌')

run2(run)
run2(swim)
print('*' * 100)


# 上面还有缺点：调用的方式会发生变化
#    不使用装饰器就调用 run()
#      使用装饰器就调用 run2()


# 标准装饰器
# 定义装饰器

def outer(fn):  # fn=sleep

    def inner():
        print('先跳个舞')
        fn()  # 其实调用的是sleep()
        print('再唱个歌')
    return inner

# def sleep():
#     print('我爱睡觉')
#
# sleep = outer(sleep)  # 装饰器的原理
# print(sleep.__name__)  # sleep=inner, inner函数，sleep指向inner函数
# sleep()  # 相当于调用inner()

@outer  # 添加装饰器的语法, 相当于添加了sleep2 = outer(sleep2)
def sleep2():
    print('我爱睡觉2')

sleep2()
print(sleep2.__name__)

print()


# 练习：写一个装饰器，计算函数运行的时间
import time
print(time.time())  # 获取当前时间

# 装饰器(了解)
def dec(fn):
    def inner(*args, **kwargs):  # 通用装饰器，通用参数，可以接受任意参数
        start = time.time()
        fn(*args, **kwargs)
        end = time.time()
        print(end - start)  # 时间差
    return inner


@dec
def mysum(n):
    s = 0
    for i in range(n):
        s += i
    # print(s)


mysum(10**8)




