''' '''

# 三大结构
#   1. 顺序结构： 代码自上而下执行
#   2. 分支结构
#   3. 循环结构

# if分支结构
#    Python语言有强制缩进
if True:
    print("hello")
    print("hello")


# 单分支
'''
age = int(input('请输入年龄：'))
if age >= 18:
    print('恭喜你，成年了!')

print('end')
'''

# 双分支
'''
age = int(input('请输入年龄：'))
if age >= 18:
    print('恭喜你，成年了!')
else:
    print('还没成年，老实点')

print('end')
'''

# 多分支
#  age范围
#    age<18 : 未成年
#    18~30 : 年轻人
#    30~60 : 中年人
#    age>60 : 老年人
'''
age = int(input('请输入年龄：'))
if age < 18:
    print('未成年')
elif age <= 30:
    print('年轻人')
elif age <= 60:
    print('中年人')
else:
    print('老年人')

'''


# 练习：
#    输入年龄age，要求输入0~12岁之间
#    0~3 : 婴儿
#    3~6 ： 幼儿
#    6~12 ：儿童
'''
age = int(input('请输入年龄(0~12)：'))
if age <= 3:
    print('婴儿')
elif age <= 6:
    print('幼儿')
else:
    print('儿童')
'''


# 练习2：
#    输入性别sex,判断sex
#    如果sex=='男'：输出王思聪
#    如果sex=='女'：输出刘亦菲
#    否则：输出泰国人
'''
sex = input('输入性别(男/女)：')
if sex == '男':
    print('王思聪')
elif sex == '女':
    print('刘亦菲')
else:
    print('泰国人')
'''

# if嵌套
#   可以在if语句中 再写if
# 比如：有一个女孩，她母亲要给他介绍对象，女孩有几个要求：
#   1.年龄<=30
#   2.身高>=1.75m
#   3.年薪>=20w
'''
age = int(input('这个男的多大了:'))
if age <= 30:
    height = float(input('他多高啊:'))
    if height >= 1.75:
        salary = int(input('他年薪多少啊:'))
        if salary >= 20:
            print('那就见一面吧！')
        else:
            print('薪资太低了！，不考虑了')
    else:
        print('身高不高啊，不见了吧')
else:
    print('年龄太大了，我还小')
'''

# if 条件
# bool值隐式判断
if 10:
    print('if 10')



# 扩展
# 输入2个数，得到较大的数
a = 60
b = 40
if a > b:
    print(a)
else:
    print(b)

# 一行来表示：if-else
c = a if a>b else b
print(c)


# 练习：
#   input("请说出你的心里话(喜欢/不喜欢):")
#   如果喜欢，输出：小女子无以为报,只有以身相许
#   如果不喜欢，输出：小女子无以为报,只有来世做牛做马报答公子大恩
word = input("请说出你的心里话(喜欢/不喜欢):")
if word == "喜欢":
    print('小女子无以为报,只有以身相许')
else:
    print('小女子无以为报,只有来世做牛做马报答公子大恩')

# 练习：
# 输入一个成绩score,判断这个成绩属于哪个等级
#    score >= 90: A
#    70<= score <90: B
#    60<= score <70: C
#    score < 60 : D
score = int(input('score:'))
if score >= 90:
    print('A')
elif score >= 70:
    print('B')
elif score >= 60:
    print('C')
else:
    print('D')

