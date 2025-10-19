
# Python数据类型:
#  int, float, str, bool, NoneType,
#  list, tuple, dict, set(了解), bytes

# list列表 : Array数组
# 为什么要使用列表：
# 举例：如果我们表示汽车品牌用变量保存单个值
a = "BYD"
b = "五菱宏光"
c = "小米"
d = "蔚来"
e = "法拉利"
f = "兰博基尼"
g = "路虎"

# 如果要你表示300个品牌, 变量就太多了，这时我们可以使用列表来表示：
cars = ["BYD", "五菱宏光", "小米", "蔚来", "蔚来", "法拉利", "兰博基尼", "路虎"]



# 列表的基本功能
# 1.列表定义
# nums = [10, 20, 30, 40, 50, "hello"]  # 不推荐 元素类型不统一
nums = [10, 20, 30, 40, 50]

# 2.索引,下标
#   从0开始
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(nums[4])
# print(nums[5])  # IndexError: list index out of range
print(nums[-1])  # 倒数第一个


# 3.长度,元素个数
print(len(nums))  # 5

# 4.遍历,循环
nums = [10, 20, 30]
for n in nums:
    print(n)  # 元素

for i in range(len(nums)):
    print(i, nums[i])  # 索引

for i,n in enumerate(nums):
    print(i, n)  # 索引，元素


# 5.修改列表
nums = [1, 2, 3]
nums[0] = 666
print(nums)  # [666, 2, 3]


# 6.切片 (很重要) : 不会修改原列表
#    list[start : stop : step] : [start, stop)
#  和range(start, stop, step)类似  [start, stop)
ages = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(ages[:5])  # 索引[0,5)  [10, 20, 30, 40, 50]
print(ages[5:])  # 从索引5开始到最后   [60, 70, 80, 90]
print(ages[2:5])  # 索引[2,5)  [30, 40, 50]
print(ages[2:8:2])  # [30, 50, 70]
# print(ages[7:1:-1])  # [80, 70, 60, 50, 40, 30]
print(ages[::-1])  # 倒序，[90, 80, 70, 60, 50, 40, 30, 20, 10]


# 7. 合并 +  (了解)
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)  # [1, 2, 3, 4, 5, 6]

# 8. 重复 * (了解)
print(a * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 9. 成员 in (掌握)
if 3 in a:
    print('3 在列表a中')


# 需求: 列表去重 (掌握)
nums = [1, 2, 2, 2, 2, 3, 3, 3, 3, 1, 1, 5, 5, 4, 3, 3]
nums2 = []
for n in nums:
    if n not in nums2:
        nums2.append(n)  # 把n添加到nums2列表中
print(nums2)  # [1, 2, 3, 5, 4]


# 10.删除元素 del (了解)
nums = [10, 20, 30, 40, 50]
# del nums[0]
del nums[:2]
print(nums)
