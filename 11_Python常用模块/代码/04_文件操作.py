
# 文件操作:
#  1.打开文件
#  2.操作文件(读取read / 写入write)
#  3.关闭文件

# 1.打开文件
# open(file, mode='r')
#   file: 打开的文件路径
#   mode:
#     r : 只读read, 如果文件不存在则报错
#     rb: 只读二进制, 如果文件不存在则报错
#
#     w : 清空写write, 如果文件不存在会自动创建
#     wb: 清空写二进制, 如果文件不存在会自动创建
#     a : 追加写append, 如果文件不存在会自动创建
#     ab: 追加写二进制, 如果文件不存在会自动创建


# 文件句柄, 文件对象
# 读取
fp = open('a.txt', 'r', encoding='utf-8')  # 不是二进制的都要些encoding
# fp = open('a.txt', 'rb')  # 读取出来是二进制

print(fp.read())  # 读取所有内容
# print(fp.readline())  # 一次读一行，会一直往下读行
# print(fp.readline())
# print(fp.readlines())  # 一次读取所有行  ['hello\n', 'abcdef']
# print(fp.read(3))  # 读取3个字符
# print(fp.read(3))  # 读取3个字符

fp.close()


# 写
# fp = open('b.txt', 'w', encoding='utf-8')  # 清空写
# fp.write('hello 杰克')

# fp = open('b.txt', 'wb')  # 清空写
# fp.write('hello 马克'.encode())

# fp = open('b.txt', 'a', encoding='utf-8')  # 追加写
# fp.write('hello 鲁班七号\n')

fp = open('b.txt', 'ab')  # 追加写
fp.write('hello 诸葛亮\n'.encode())

fp.close()


# with-as : 会自动关闭文件
with open('b.txt', 'a', encoding='utf-8') as fp:
    fp.write('Jeff \n')


