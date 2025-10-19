
# 字典 dict  dictionary字典

# dict特点：
#   1. 字典的key不能重复 （key 唯一性）
#   2. 字典的key不可以是 可变类型(list,dict,set)，但是建议使用字符串
#   3. key无序性

# 1.创建
#  key:value ：键值对
d = {'name': "张三丰", 'age': 100}
print(d)

# 2.索引 : 没有数字索引，但是可以使用key
d = {'name': "张三丰", 'age': 100}
# print(d[0])  # KeyError: 0
print(d['name'])  # '张三丰'
# print(d['name2'])  # 报错，key不存在
print(d.get('name'), d.get('name2'))  # 张三丰 None  找不到的话，不会报错，会返回None
print(d.get('sex', '男'))  # 如果找不到sex，则使用默认值"男"


# 3.长度
d = {'name': "张三丰", 'age': 100}
print(len(d))  # 2


# 4.遍历
d = {'name': "张三丰", 'age': 100}

print(list(d.keys()))  # 所有的key  ['name', 'age']
print(list(d.values()))  # 所有的value  ['张三丰', 100]
print(list(d.items()))  # 所有的item   [('name', '张三丰'), ('age', 100)]

# 推荐
for key in d:
    print(key, d[key])  # key

# for key in d.keys():
#     print(key)

# for val in d.values():
#     print(val)

# 推荐
for key,val in d.items():
    print(key, val)  # key  value


# 5.修改元素
d = {'name': "张三丰", 'age': 100}
d['name'] = '聂风'
print(d)  # {'name': '聂风', 'age': 100}


# 6.切片: 不可以
#    dict没有数字索引，而且dict是无序的，所以没有切片

# 7.合并
d1 = {'a': 100}
d2 = {'b': 200}
# print(d1 + d2)  # 不可以，会报错
d1.update(d2)  # 将d2合并到d1里
print(d1)  # {'a': 100, 'b': 200}
print(d2)  # {'b': 200}



# 8.重复： 不可以
# print(d1 * 3)

# 9.成员 (掌握)
d = {'name': "张三丰", 'age': 100}
if 'name' in d:
    print("name 是字典d的key")



# 字典的功能
# 增删改查
#  增，改
d = {'name': "张三丰", 'age': 100}
d['name'] = '聂风'  # 修改：key存在
d['sex'] = '男'  # 新增：key不存在
print(d)  # {'name': '聂风', 'age': 100, 'sex': '男'}


# 删：
#  pop(key): 删除key对应的元素 (掌握 )
#  clear() : 清空字典 （了解）
#  popitem() : 删除一个元素 （了解）

d = {'name': '聂风', 'age': 100, 'sex': '男'}
d.pop('name')  # 删除name
print(d)  # {'age': 100, 'sex': '男'}

# d.clear()
# print(d)  # {}
#
# d = {'a': 1, 'b': 2, 'c': 3}
# d.popitem()
# print(d)

