
'''
1. 写一个初级程序：先输入自己的名字，如输入：张三，则打印"大家好，我是 张三"
'''
# name = input('请输入名字：')
# print("大家好，我是", name, sep='')


'''
2. 分隔符输出字符串：
在控制台分别输入3个变量a,b,c，然后用print输出这3个变量组成的字符串，中间要求使用分隔符加号（+）连接, 要求使用sep
例如：输入3个字符串“Python”、“is”、“Wonderful”，结果显示为“Python+is+Wonderful”
'''
# a = input('a:')
# b = input('b:')
# c = input('c:')
# print(a, b, c, sep='+')


'''
3.使用input在控制台输入半径r，求面积S 和  周长C,   π=3.14
   公式： 面积S = 半径r * 半径r * 3.14
		 周长C = 半径r * 3.14 * 2
'''
r = float(input('r:'))
S = r * r * 3.14
C = r * 3.14 * 2
print(S, C)

