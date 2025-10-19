
# 字符串的功能

# count(): 计数,统计某子串出现的次数
# s = "hello hello hello"
# print(s.count('l'))  # 6
# print(s.count('ll'))  # 3
# print(s.count('ll', 1, 10))  # 2  在[1,10)之间查找"ll"出现的次数

# 大小写判断 (掌握)
print('ABC'.isupper())  # 字母是否为大写
print('abc'.islower())  # 字母是否为小写
print('123'.isdigit())  # 是否为数字
print('abcABC'.isalpha())  # 是否为字母
print('abcABC123'.isalnum())  # 是否字母或数字
# print('   '.isspace())  # 是否为空格字符串
# print('Hello World'.istitle())  # 是否每个单词首字母大写,其他小写

# 大小写转换
print('abc123'.upper())  # "ABC123" 转成大写
print('ABC123'.lower())  # 'abc123' 转成小写
print(int('123'))  # 转成整数 123
print(float('3.14'))  # 转成小数 3.14
# print(int('3.14'))  # 报错， 不能将小数字符串直接转换成整数
# print('heLLO woRLd'.title())  # "Hello World" 转换成:每个单词首字母大写,其他小写
# print('heLLO woRLd'.swapcase())  # 大小写切换: 大写变成小写,小写变成大写  'HEllo WOrlD'



# 查找
#   find(): 查找指定子串第一次出现的下标位置,如果不存在则返回-1
#  rfind(): 从右往左查找指定子串第一次出现的下标位置,如果不存在则返回-1
#   index(): 不用
#   rindex(): 不用
s = "ikun is very very very handsome"
print(s.find('very'))  # 8
print(s.find('luhan'))  # -1
print(s.rfind('very'))  # 18
print(s.rfind('luhan'))  # -1


# 练习:
# 1.已知字符串：“this is a test of Python”
s = 'this is a test of Python'

# a.统计该字符串中字母s出现的次数: count()
print(s.count('s'))  # 3

# b.取出子字符串“test”, 用切片,不能数: 使用find(),len()
print(s[ s.find('test') :  s.find('test') + len('test')])

# c.采用不同的方式将字符串倒序输出: 切片，循环
print(s[::-1])

print(list(range(len(s)-1, -1, -1)))
s2 = ''
for i in range(len(s)-1, -1, -1):
    # print(s[i], end='')
    s2 += s[i]
print(s2)




# 拆分,合并,替换
# 拆分: 分割
#  split() : 拆分后得到列表
s1 = "ikun    is very very very handsome"
print(s1.split())  # ['ikun', 'is', 'very', 'very', 'very', 'handsome']
# print(s1.split(' '))  # ['ikun', '', '', '', 'is', 'very', 'very', 'very', 'handsome']
print(s1.split('ikun'))  # ['', '    is very very very handsome']


# splitlines(): 按行拆分
s2 = '''床前明月光,
疑是地上霜.
举头望明月,
低头思故乡.'''
print(s2.splitlines())  # ['床前明月光,', '疑是地上霜.', '举头望明月,', '低头思故乡.']
print(s2.split('\n'))  # ['床前明月光,', '疑是地上霜.', '举头望明月,', '低头思故乡.']
# print(s2.splitlines(keepends=True))  # ['床前明月光,\n', '疑是地上霜.\n', '举头望明月,\n', '低头思故乡.']



# 合并: join : 会得到字符串类型
#   将列表中的字符串拼接
n = ['床前明月光,', '疑是地上霜.', '举头望明月,', '低头思故乡.']
print('\n'.join(n))
print('\t'.join(n))
print(''.join(n))


# 替换: replace() : 默认替换所有匹配的
s1 = "ikun    is very very very handsome"
s2 = s1.replace('very', 'not')
print(s2)




# 练习
# 1.已知字符串：“this is a test of Python”
# d.将其中的"test"替换为"exam" : replace()
s = 'this is a test of Python'
print(s.replace('test', 'exam'))


# 2.去掉字符串123@zh@qq.com中的@;
# 提示: replace()  或者 split()+join()
s = '123@zh@qq.com'
print(s.replace('@', ''))
print(''.join(s.split('@')))


