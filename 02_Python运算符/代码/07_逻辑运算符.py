
# 逻辑运算符
#   and与(且)  or或者  not非（取反）


# and: 并且
#   2边都为True则为True，只要有一个是False 则为False
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# or：或者
#   2边都为False则为False, 只要有一个是True则为True
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# not 非，取反
print(not True)  # False
print(not False)  # True
print(not 0)  # True
print(not '0')  # False

# 不同数据类型 隐式bool值 判断
#   数字类型： 0是假，其他为真
#   字符串类型： 空字符串''为假，其他为真
#   bool类型： False为假，True为真
#   NoneType类型: None是假
#   list类型：空列表[]是假，其他为真
#   tuple元组： 空元组()为假,其他为真
#   dict字典：空字典{}为假，其他为真
# print()
# print(bool(0))
# print(bool(''))
# print(bool(None))
# print(bool([]))
# print(bool(()))
# print(bool({}))




print()
# 扩展: and和or的短路运算

# and:
#  从左往右依次判断每一个数，只要有一个是False（bool值隐式判断） 则返回该数
print(3 and 5)  # 5
print(3 and 0 and 5)  # 0
print(3 and 0 and print(50))  # 0 到0的时候就短路了(不会往右继续判断)
print(3 and print(50) and 6)  # 打印50，然后输出None

# print(print(100))


# or:
#  从左往右依次判断每一个数，只要有一个是True（bool值隐式判断） 则返回该数
print(0 or 666)  # 666
print(0 or print(80) or 888)  # 先打印80，然后再输出888
print(0 or 999 or print(90))  # 999



# 练习：请直接写出答案（先不要运行）
x = True and 9  # x=9
y = False or True or 8  # y=True
z = x * 3 + y * 2  # 9*3 + 1*2
print(x, y, z)  # z=29





