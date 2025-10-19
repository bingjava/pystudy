
# 数学操作 math

#    sum(): 求和
#    max()：最大值
#    min(): 最小值
#    round(): 四舍五入
#    abs(): 绝对值
#    pow(): 次方  (了解)  **次方
print(sum([1, 2, 3, 4]))
print(sum(range(1, 101)))  # 5050

print(max([1, 2, 6, 4]))
# print(max(1, 2, 6, 4))

print(min([1, 3, 7, -3, 4]))

print(round(3.14567))  # 3
print(round(3.14567, 2))  # 3.15  保留2位小数

print(abs(-3))   # 3

print(pow(2, 3),  2 **3)


# math: 数学
import math

# print(math.e)  # 2.718281828459045
print(math.pi)  # π  = 3.141592653589793
print(math.inf)  # 无穷大
# print(-math.inf)  # 负无穷大

print(math.sqrt(81), 81**0.5)  # 开平方根  9
# print(math.factorial(5))  # 5的阶乘 5!=1*2*3*4*5 = 120

print(math.ceil(3.14))  # 向上取整 4
print(math.floor(3.14))  # 向下取整 3

# print(math.log(math.e))  # 自然对数 loge(e) = ln(e) = 1  底数和真数一样，则对数的值为1
# print(math.log10(100))  # 2
# print(math.log2(2))  # 1

# print(math.sin(math.pi))  # 三角函数  cos  tan
