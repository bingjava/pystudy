

# 对列表进行降序排序(不修改原列表) :
def sort1(l) -> list:
    return sorted(l, reverse=True)

# 对列表进行升序排序(不修改原列表):
def sort2(l) -> list:
    return sorted(l)

# 获取列表中所有与指定元素重复的元素下标，并返回这些下标所组成的列表
def find_index(l, n) -> list:

    # index_list = []
    # for i,num in enumerate(l):
    #     if n == num:
    #         index_list.append(i)
    # return index_list

    return [i for i,num in enumerate(l) if n==num]



# 模块名称
#   1. 如果在当前文件执行，则__name__的值是"__main__"
#   2. 在其他地方导入当前模块后，在其他地方执行，则__name__是当前模块名 test.sort
print('__name__:', __name__)  # "__main__"


# 1.作为文件入口: 代码开始执行的地方
# 2.在当前模块的测试代码
if __name__ == '__main__':
    ret = sort1([1,2, 3, 4, 5])
    print(ret)

