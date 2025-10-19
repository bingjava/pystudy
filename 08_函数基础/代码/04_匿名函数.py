
# 匿名函数： lambda
#   特点：
#       没有名字的函数
#       自带return
#       只表示一些简单的，有返回值的函数
def fn(x):
    return x**2

# => 匿名函数
f2 = lambda x: x**2
print(f2(5))  # 25

f3 = lambda x,y: x+y
print(f3(3, 4))  # 7



# 高阶函数 (了解)
#  map: 映射，对列表做批量处理
n = map(lambda x: x**3, [1, 2, 3])
print(list(n))  # [1, 8, 27]

n = map(lambda x,y: x*y, [1, 2, 3], [4, 5, 6])
print(list(n))  # [4, 10, 18]

# filter: 过滤,找到符合要求的数据
n = filter(lambda x: x>0,  [1, -2, 3, -4, -5, 7, 6, -9])
print(list(n))  # [1, 3, 7, 6]

