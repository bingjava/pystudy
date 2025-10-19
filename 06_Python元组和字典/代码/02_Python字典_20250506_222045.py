
# 数据类型：
#   int: 整数
#   float: 存小数
#   bool： 表示真假
#   str: 存字符串，包括 中文，英文 等
#   list: 列表一般存放相同类型或类似的数据，主要是方便循环批量操作，
#         比如存放人的姓名["张三", "李四", "王五",...]
#   tuple：除了不可以修改，作用和list一样
#   dict: 一般用来存储一个事物的不同属性，
#         比如表示一个人的信息：{"name": "ikun", "age": 18, "sex": "男", "like": ["篮球","RAP","跳舞"]}

# 字典 dict  dictionary字典

# dict特点：
#   1. 字典的key不能重复 （key 唯一性）
#   2. 字典的key不可以是 可变类型(list,dict,set)，但是建议使用字符串
#   3. key无序性

# 可变类型：list, dict, set
# 不可变类型：int,float,bool,str,tuple,NoneType

# 1.创建
#  key:value ：键值对
d = {'name': '张三丰', 'age': 100}
print(d, type(d))


# 2.索引 : 没有数字索引，但是可以使用key
d = {'name': '张三丰', 'age': 100}
# print(d[0])  # KeyError: 0  表示 0不是有效的key
print(d['name'])  # 张三丰
# print(d['name2'])  # 如果key不存在，则报错
print(d.get('name'), d.get('name2'))  # 张三丰 None   找不到的话不会报错会返回None
print(d.get('sex', "男"))  # 如果找不到，则使用默认值“男”


# 3.长度
d = {'name': '张三丰', 'age': 100}
print(len(d))  # 2


# 4.遍历
d = {'name': '张三丰', 'age': 100}

for key in d:  # 遍历key
    print(key, d[key])  # key

print(list(d.keys()))  # 所有的key  ['name', 'age']
print(list(d.values()))  # 所有的value  ['张三丰', 100]
print(list(d.items()))  # 所有的item  [('name', '张三丰'), ('age', 100)]

# for key in d.keys():
#     print(key)

# for val in d.values():  # 遍历value （了解）
#     print(val)

for key,val in d.items():  # key和value
    print(key,val)


# 5.修改元素
d = {'name': '张三丰', 'age': 100}
d['name'] = '聂风'
print(d)  # {'name': '聂风', 'age': 100}


# 6.切片: 不可以
#    dict没有数字索引，而且dict是无序，所以没有切片


# 7.合并
d1 = {'a': 100}
d2 = {'b': 200}
# print(d1 + d2) # 不可以
d1.update(d2)
print(d1)  # {'a': 100, 'b': 200}
print(d2)  # {'b': 200}


# 8.重复： 不可以
# print(d1 * 3)  # 报错

# 9.成员 (掌握)
d3 = {'a': 100, 'b': 200}
if 'a' in d3:
    print('a在d3中')






# 字典的功能
# 增删改查
#  增，改
d = {'name': '张三丰', 'age': 100}
d['name'] = '聂风'  # 修改：key存在
d['sex'] = '男'  # 新增：key不存在
print(d)  # {'name': '聂风', 'age': 100, 'sex': '男'}


# 删：
#  pop(key): 删除key对应的元素 (掌握 )
#  clear() : 清空字典 （了解）
#  popitem() : 删除一个元素 （了解）

d = {'name': '聂风', 'age': 100, 'sex': '男'}
d.pop('name')
print(d)  # {'age': 100, 'sex': '男'}

# d.clear()
# print(d)  # {}

# d = {'a': 1, 'b': 2, 'c': 3}
# d.popitem()
# print(d)
