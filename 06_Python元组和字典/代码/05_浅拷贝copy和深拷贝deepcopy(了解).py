
# Python
#   不可变类型: int,float,str,tuple,bool,NoneType
#    可变类型: list, set, dict

# 赋值
# 不可变类型 (没有关联)
a = 10
b = a
b = 20
print(a, b)  # a=10, b=20


# 可变类型 (有关联)
a = [1, 2, 3]
b = a
b[0] = 666
print(a)  # [666, 2, 3]
print(b)  # [666, 2, 3]



# 深浅拷贝的可视化视图
#  http://pythontutor.com/live.html#mode=edit

# copy: 浅拷贝/浅复制
a = [1, 2, 3]
b = a.copy()
b[0] = 666
print(a)  # [1, 2, 3]
print(b)  # [666, 2, 3]


# deepcopy 深拷贝(针对二维或多维数组)

a = [1, 2, [3, 4]]
b = a.copy()  # 浅拷贝
b[-1][-1] = 888
print(a)  # [1, 2, [3, 888]]
print(b)  # [1, 2, [3, 888]]

import copy
a = [1, 2, [3, 4]]
b = copy.deepcopy(a)  # 深拷贝
b[-1][-1] = 888
print(a)  # [1, 2, [3, 4]]
print(b)  # [1, 2, [3, 888]]

