

# 构造方法：初始化方法，在创建对象时自动被调用
#    __init__
# 析构方法：在对象销毁时自动被调用 (了解)
#    __del__

# 魔法方法：双下划线的方法

class Animal:
    # 构造方法
    def __init__(self, name):
        self.name = name
        print('构造方法：在对象创建时会自动调用!')

    # 析构方法
    def __del__(self):
        # 在这里可以写手动是否内存的代码，关闭文件
        print('析构方法：在对象销毁时会自动调用!')


cat = Animal('米米')


import time
time.sleep(3)

del cat

time.sleep(3)
print('end')
