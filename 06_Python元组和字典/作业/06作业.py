
# 1.已知字典 dic = {"k1": "v1", "k2": "v2", "k3": "v3"}，实现以下功能
# dic = {"k1": "v1", "k2": "v2", "k3": "v3"}
#
# # a.遍历字典 dic 中所有的key
# for k,v in dic.items():
#     print(f"{k}={v}")
# # b.遍历字典 dic 中所有的value
# for v in dic.values():
#     print(v)
# # c.循环遍历字典 dic 中所有的key和value
# for k in dic.keys():
#     print(f"{k}={dic[k]}")
# # d.添加一个键值对"k4","v4",输出添加后的字典 dic
# dic.setdefault("K4","V4")
# print(dic)
# # e.删除字典 dic 中的键值对"k1","v1",并输出删除后的字典 dic
# dic.pop("k1")
# print(dic)
# dic.popitem()
# print(dic)

# 2. 去除列表中成绩小于70的字典
# dict_list = [{"科目":"政治", "成绩":98},
#              {"科目":"语文", "成绩":77},
#              {"科目":"数学", "成绩":99},
#              {"科目":"历史", "成绩":65}]
#
# for k,v  in dict_list:
#     print(f"{k}={v}")
# for lst in dict_list:
#     print(lst)
#     if lst.get('成绩')<70:
#         print(lst)
#         dict_list.remove(lst)
#
# print(dict_list)
# 3.已知字典 d2 = {'k1':"v1", 'a':"b"}
#   编写程序，使得d2 = {'k1':"v1", 'k2':"v2", 'k3':"v3", 'a':"b"}


# 4.已知我的电话簿里头有以下联系人，现在输入人名，查询他的号码，
#   如果人名存在，则输出电话号码，如果该人不存在，返回"not found"
address_dict = {'mayun': '13309283335',
                'zhaolong': '18989227822',
                'zhangmin': '13382398921',
                'Gorge': '19833824743',
                'Jordan': '18807317878',
                'Curry': '15093488129',
                'Wade': '19282937665'}
'''
name = input('请输入姓名:')
print(address_dict.get(name, 'not found'))
'''
name = input('请输入姓名:')
person = address_dict.get(name, 'not found')
address_dict.setdefault(person, '0')
print(person)

# 5.已知列表 numlist = [23,5,56,7,78,89,12,45,6,8,89,100,99],
# 生成一个字典，将大于66的数字保存在字典的第一个key中，
#            将小于等于66的数字保存在字典的第二个key中
# 结果为： { 'key1': [78, 89, 89, 100, 99],
#          'key2': [23, 5, 56, 7, 12, 45, 6, 8]}

#
# tuple1 = ('a','b','c')
# print(type(tuple1))
# print(len(tuple1))
#
# dict1 = {'k1':'v1', 'k2':'v2', 'k3':'v3'}
# dect2 = {'K4':'V4'}
#
# dict1.setdefault('K1','111')
# dect2.update(dict1)
# val = dect2.get('K12','333')
# print(val)
# print(dict1)
# print(dect2)
# print(dect2)
# print(dict1)
# for k,v in dict1.items():
#     print(k,v)
