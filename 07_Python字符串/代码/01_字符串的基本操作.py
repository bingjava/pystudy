
# 字符串的基本操作
#  str : 引号包裹的就是字符串 'abc'  "abc" """abc"""

# 1.创建字符串
s = '宝，买房吗'
print(s)

# 2.索引
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[-1])

# 3.长度
print(len(s))

# 4. 循环
s = 'abc'
for c in s:
    print(c)  # 字符char

for i in range(len(s)):
    print(i, s[i])  # 索引

for i,c in enumerate(s):
    print(i, c)  # 索引，字符


# 5.修改字符串: 字符串str是不可变类型
# s = "abcdef"
# s[0] = "A"  # 报错

s = 'ABC'
s = s + "DEF"
print(s)

# 6.切片
s = 'ABCDEFGHI'
print(s[:4])  # 'ABCD'
print(s[4:])  # 'EFGHI'
print(s[2:4])  # 'CD'
print(s[2:7:2])  # 'CEG'
print(s[::-1])  # 倒序  'IHGFEDCBA'


# 7.加法
print("abc" + 'def')

# 8.乘法
print('abc' * 3)

# 9.成员
print('a' in 'abc')
print('abc' in '123abcdef')

