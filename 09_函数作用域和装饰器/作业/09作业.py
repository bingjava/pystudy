

# 1、使用Python写一个按照下面方式调用都能正常工作的 my_sum() 方法
'''
    print(my_sum(2,3))     输出 5
    print(my_sum(2)(3))    输出 5
'''
# 提示:
#   通过参数数量判断不同的情况
#   1.有1个参数, 嵌套函数
#   2.有2个参数, 返回和



# 2、封装函数，传入不定数量的数值型参数，返回所有数字的乘积,
# 提示: *args


# 3、 封装一个函数random_color，该函数的返回值为随机十六进制颜色。 RGB
# 说明： 十六进制颜色#开头后面接6个十六进制数， 例: #FFFFFF， #000000， #0033CC
# 提示: colors = '0123456789ABCDEF'
#      使用random模块
colors = '0123456789ABCDEF'



# 4、 封装函数，
# 第一个函数create_persons()，
#   创建并返回包含5个字典(例如:{"name":"xx","age":xx, "faceValue":100})的列表
#      其中name的值：从["张三","李四","王五","赵六","钱七"]依次取
#      其中age的值：10-100之间的随机整数 random.randint()
#      其中faceValue的值：0-100之间的随机整数
#
# 第二个函数 get_old(), 传入第一个函数创建的列表, 找出列表中年龄最大的人，并将其所有信息打印
# 第三个函数 sort_facevalue(), 传入第一个函数创建的列表, 根据颜值升序排列，并打印排序后的信息

def create_persons():
    pass


def get_old(persons):
    pass


def sort_facevalue(persons):
    pass



# 调用
persons = create_persons()

get_old(persons)
sort_facevalue(persons)



# 6. 给下面的set_age函数添加一个装饰器，
#    要求：在传入age之前判断age不能小于0，如果小于0则传入0，并打印"提示：年龄不能小于0"

def set_age(age):
    print(f'大家好！我今年{age}岁')


