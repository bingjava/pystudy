
'''
1. 写一个初级程序：先输入自己的名字，如输入：张三，则打印"大家好，我是 张三"
'''
def inputTest():
    name=input("请输入用户名：")
    print(f"大家好，我是 {name}")
    print("大家好，我是 %s" % name)
    print("大家好，我是 {name}".format(name=name))

'''
2. 分隔符输出字符串：
在控制台分别输入3个变量a,b,c，然后用print输出这3个变量组成的字符串，中间要求使用分隔符加号（+）连接, 要求使用sep
例如：输入3个字符串“Python”、“is”、“Wonderful”，结果显示为“Python+is+Wonderful”
'''
def strSplit():
    a = input("请输入变量 a=")
    b = input("请输入变量 b=")
    c = input("请输入变量 c=")
    print("方式一："+a+'+'+b+'+'+c)
    print("方式二："+a,b,c,sep='+')


'''
3.使用input在控制台输入半径r，求面积S 和  周长C,   π=3.14
   公式： 面积S = 半径r * 半径r * 3.14
		 周长C = 半径r * 3.14 * 2
'''
def paijis():
    r = input("请输入半径，r=")
    try:
        r=int(r)
        s= r * r * 3.14
        print("面积是：%s" %s)
        c=r*2*3.14
        print(f"周长是：{c}")
    except ValueError:
        print(f"输入错误：{r}，请输入有效数字！")
    except Exception as e:
        print(f"发生未知错误:{e}")
# inputTest()
# strSplit()
paijis()