
# 成员运算符（掌握）
#   in,  not in
print(3 in [3, 4, 5])  # True
print(3 not in [3, 4, 5])  # False


# 身份运算符（了解）
#   is,  is not
#   作用：比较内存地址
a = 10
b = 20
print(id(a))
print(id(b))
print(a is b)  # False
print(a is not b)  # True

# id(): 查看内存地址



# 区别： ==， is区别
#  == 比较的是值是否相等
#  is 比较的是内存地址

