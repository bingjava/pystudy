
# 转义字符 \ : 让有语义的字符失去语义 (掌握)
# r'' : 让字符串中有语义的字符失去语义 (掌握)
# b'' : 字节
# f'' : f-string

#  \\  表示一个\
s = 'C:\\Users\\EDY\\Desktop\\软件包'
s = r'C:\Users\EDY\Desktop\软件包'
print(s)


# 编码和解码
#  编码: encode() 将 字符串 => 二进制
#  解码: decode() 将 二进制 => 字符串
s = 'hello 中国'
b = s.encode() # utf-8   # b'hello \xe4\xb8\xad\xe5\x9b\xbd'
# b = s.encode('gbk')  # b'hello \xd6\xd0\xb9\xfa'
print(b)

s2 = b.decode()
print(s2)  # hello 中国


# ASCII码(了解)
# print(ord('a'))  # 97
# print(chr(65))  # A


# strip() : 去除两边的指定字符(默认去除空格) (了解)
s = '     hello   world     '
# print(s.strip())  # 'hello   world'
# print(s.lstrip())  # 'hello   world     '
# print(s.rstrip())  # '     hello   world'
# print('-----hello---world----'.strip('-'))  # 'hello---world'


# 对齐方式 : 了解
# print('hello'.center(40))  # 居中
# print('hello'.ljust(40))  # 靠左
# print('hello'.rjust(40))  # 靠右
# print('hello'.zfill(40))  # 靠右


# 前缀和后缀
print('helloworld'.startswith('hel'))  # True
print('helloworld'.endswith('rld'))  # True

