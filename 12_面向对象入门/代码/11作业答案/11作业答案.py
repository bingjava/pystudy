
# 1. 自定义模块:
#   a.建立一个包：test
#   b.在包的下创建一个排序的模块 sort.py
#        模块下的功能
#        对列表进行降序排序(不修改原列表) :
#            def sort1(l) -> list:
#
#        对列表进行升序排序(不修改原列表):
#            def sort2(l) -> list:
#
#        获取列表中所有与指定元素重复的元素下标，并返回这些下标所组成的列表
#             def find_index(l, n) -> list:
#
#   c.在另外一个文件中 aa.py导入上述包中的模块sort.py，完成模块中功能的调用
from test import sort
print(sort.find_index([3, 4, 4, 5, 4, 6, 4], 4))



# 2. 开房查询
# 	创建函数，传入一个名字，查找到这哥们的开房记录，
#       然后把身份证号码和地址取出来，写入到以这哥们名字为名的txt文件中 如：张三.txt

def fn(name='鲍晨飞'):

    fp2 = open(f'{name}.txt', 'a', encoding='utf-8')

    with open('kaifanglist.txt', 'r', encoding='utf-8') as fp:
        list1 = fp.readlines()
        # print(list1)
        for row in list1:
            # print(row)
            list2 = row.split(',')

            if list2[0] == name:
                print(list2[1], list2[4])
                fp2.write(f'{list2[1]}, {list2[4]}')


    fp2.close()

fn()
