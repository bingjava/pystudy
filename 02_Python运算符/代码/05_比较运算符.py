
# 比较运算符/关系运算符/条件运算符
#  > >= < <= == !=
#  得到的结果一定是bool类型
print(10 > 4)  # True
print(10 >= 10)  # True
print(10 < 4)  # False
print(10 <= 4)  # False
print(10 == 4)  # False
print(10 != 4)  # True

print(True == 1)  # True
print(False == 0)  # True

print()
# 字符串和字符串比较
# 比较规则：从左往右依次一个一个字符比较，如果能比较出大小则直接返回结果
#  ASCII码：
#  a~z : 97~122
#  A~Z : 65~90
#  0~9 : 48~57
print('a' < 'b')  # True  97 < 98
print('A' < 'a')  # True  65 < 97
print('abcdgsdfg' > 'acb')  # False

n = 10
print(5 < n < 20)


# 练习：
# BMI（身体质量指数）的计算公式为 BMI=体重（千克）/身高的平方（米）
#   请输入您的身高 和 体重，计算BMI值，判断是否在18.5~25之间？
weight = 80
height = 1.8
BMI = weight / (height**2)
print(BMI, 18.5 < BMI < 25)

