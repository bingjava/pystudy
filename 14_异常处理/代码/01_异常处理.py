
# 异常处理

# 错误：代码还没运行就已经出错了， 这种情况要先解决
# 异常：代码写的时候不报错，运行报错


# 异常处理：针对有一定概率(小概率)出现异常的，我们需要做异常处理
# try-except:
#   尝试执行try中的代码，如果出错则进入except，否则不进入
#   作用是：防止报错导致程序结束，出现的错误可以被except捕获

# a = 0
# n = 3 / a
# print('前面报错了，程序已经终止了，我不会执行')

try:
    a = 2
    n = 3 / a
    print(n)
except:
    print('报错了')

print('前面代码虽然报错，但是我依然会执行')


# 这种方式建议使用 （掌握）
try:
    a = 0
    n = 3 / a
    print(n)
except Exception as e:
    print(e)  # division by zero
    print(type(e))  # <class 'ZeroDivisionError'>
    print('出错了')

try:
    a = 2
    n = 3 / a
    print(n)
    l = []
    print(l[0])
except ZeroDivisionError as e:
    print(e)  # division by zero
    print(type(e))  # <class 'ZeroDivisionError'>
    print('出错了')
except IndexError as e:
    print(e)
    print('出错了 IndexError')


print()
# try-except-else  （了解）
#   try尝试执行代码，如果出错了就进入except,否则进入else
try:
    a = 3
    n = 3 / a
    print(n)
except Exception as e:
    print("error：", e)
else:
    print('没问题')


# try-except-finally （了解）
#    try尝试执行代码，如果出错了就进入except, 最终进入finally(不管有没有错)
try:
    a = 0
    n = 3 / a
    print(n)
except Exception as e:
    print("error：", e)
finally:
    print('不管有没有错误，我都会在最后执行')


# Python自带的异常类型:
#     AttributeError : 属性错误
#     NameError: 变量没定义
#     IndexError : 索引越界
#     ZeroDivisionError : 除以0的错误
#     KeyError : 字典的key错误
#     FileExistsError : 文件已经存在
#     FileNotFoundError : 文件不存在
#     ImportError : 导包错误
#     IndentationError : 缩进错误
#     SyntaxError : 语法错误

# 主动抛出异常 raise  （了解）
# raise NameError("sorry！我错了")
# raise IndexError('索引不对')

# 断言 assert  （了解）
def fn(n):
    # 判定n!=0,如果我的判定不对，则抛出异常
    assert n != 0, "报错了，n不能为0"
    # AssertionError: 报错了，n不能为0

    print(5/n)

fn(0)