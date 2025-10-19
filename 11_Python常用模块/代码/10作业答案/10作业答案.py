
# 1.实现万年历效果图，使用函数封装:
#   A:先输出提示语句，并接受用户输入的年、月。
#   B:根据用户输入的年，先判断是否是闰年。
#   C:根据用户输入的月来判断月的天数。
#   D:用循环计算用户输入的年份距1900年1月1日的总天数。
#   E:用循环计算用户输入的月份距输入的年份的1月1日共有多少天,
#   F:相加D与E的天数，得到总天数。
#   G:用总天数来计算输入月的第一天的星期数
#   H:根据G的值，格式化输出这个月的日历!

# a:先输出提示语句，并接受用户输入的年、月。
def fa():
    year = int(input('请输入年：'))
    month = int(input('请输入月：'))
    fh(year, month)


# b:根据用户输入的年，先判断是否是闰年。
def fb(year):
    return (year%4==0 and year%100!=0) or year%400==0

# C:根据用户输入的月来判断月的天数。
def fc(year, month):
    if month == 2:
        return 29 if fb(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    return 0

# D:用循环计算用户输入的年份距1900年1月1日的总天数。
def fd(year):
    s = 0
    for i in range(1900, year):
        s += 366 if fb(i) else 365
    return s

# 2026年8月
# E:用循环计算用户输入的月份距输入的年份的1月1日共有多少天,
def fe(year, month):
    s = 0
    for i in range(1, month):
        s += fc(year, i)
    return s

# F:相加D与E的天数，得到总天数。
def ff(year, month):
    return fe(year, month) + fd(year)

# G:用总天数来计算输入月的第一天的星期数
def fg(year, month):
    return ff(year, month) % 7


# H:根据G的值，格式化输出这个月的日历!
def fh(year, month):
    week = fg(year, month)
    # print(week)

    print('一', '二', '三', '四', '五', '六', '日', sep='\t')

    # 1.打印空格
    for i in range(week):
        print(' ', end='\t')

    # 2.打印当前月的日期
    for i in range(1, fc(year,month)+1):
        print(i, end='\t')
        if (i + week) % 7 == 0:  # 换行
            print()

fa()

print('\n')


# 2.请写一个生成器函数,生成一个无限序列,从1开始可以不断往后取值,每次+1
#    提示:使用while True, 通过调用n次next来获取前n个数

def fn2():
    i = 1
    while True:
        yield i
        i += 1

g2 = fn2()

import time
while True:
    print( next(g2) )
    time.sleep(1)




