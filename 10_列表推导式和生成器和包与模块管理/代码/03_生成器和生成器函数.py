

# 生成器 generator (掌握)
#  需要使用next或者for循环来调用

# nums = [i for i in range(1, 6)]   # 列表推导式

g = (i for i in range(1, 4))   # 生成器
print(g)  # generator 生成器对象
# print(list(g))  # [1, 2, 3]

# 1.next
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
# print(next(g))  # StopIteration 报错，已经没有数据了

# 2.for
g = (i for i in range(1, 4))
for i in g:
    print('i =', i)


print()

# 生成器函数:
#   1. 函数内部要有 yield
#   2. 需要用next来调用
#   3. 每个next都会在yield处暂停
#   4. yield 会暂停, 可以返回值

def fn():
    print('hello,我是fn，你看我会执行吗')
    yield  666    # 类似return的返回值，但是不会结束函数
    print('BBBB')
    yield 888

g = fn()
print(g)  # generator object
print( next(g) )  # 666
print( next(g) )  # 888




print()
# 示例:
def gen():
    g = (i for i in range(1, 10**100))

    for i in g:
        # 一个个返回值, 不会退出函数
        yield i


g = gen()
print(next(g))
print(next(g))
print(next(g))
print()



# 练习
# 1.请写一个生成器函数, 得到前20个斐波那契数 (难度:*****)
# 斐波那契数列如下：0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
#                a  b
#                   a  b
#                      a  b
#    提示:使用while True, 通过调用n次next来获取前20个数
import time

def fun():
    a = 0  # 第一个数
    b = 1  # 第二个数
    while True:
        a, b = b, a+b
        yield a

g1 = fun()
for i in g1:
    print(i, end=' ')
    time.sleep(0.1)  # 每隔0.1秒获取下一个斐波那契数



