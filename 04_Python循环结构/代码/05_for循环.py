
# 使用场景：
#   while循环： ①无限循环， ②未知循环次数
#   for循环：一般使用在已知循环次数


# 打印1~100的每一个数
'''
i = 1
while i<= 100:
    print(i)
    i += 1
'''

# for-in循环：
#  每次循环，i会自动等于右边range中的每一个数
for i in range(1, 101):
    print(i)


# 求1~100的和
s = 0
for i in range(1, 101):
    s += i
print(s)


# for循环使用场景
# 1.和range结合
#   比如：循环1~10，找到能被3整除的数
for i in range(1, 11):
    if i%3 == 0:
        print(i)

print()
# 2.和列表结合
# 列表的基本操作
#  元素：列表中的每一个值
nums = [11, 22, 33]
# 索引：从0开始
print(nums[0])  # 11
print(nums[1])  # 22
print(nums[2])  # 33
# print(nums[3])  # 报错，索引超出范围
print(nums[-1])  # 表示倒数第一个元素

# 元素个数：len()
print(len(nums))  # 3

# 循环遍历列表
nums = [11, 22, 33]
for n in nums:
    print(n)  # 元素

# for i in range(3): # range(3) => [0,1,2]
for i in range( len(nums) ):  # range(3) => [0,1,2]
    print(i, nums[i])  # 索引，元素

# enumerate:枚举，列举，会将索引和元素一起得到
for i,n in enumerate(nums):
    print(i, n)  # 索引，元素

# 还可以使用for的有：
#    range()
#    list: [1,2,3]
#    dict: {'name': 'ikun', 'age': 20}
#    tuple: (1,2,3)
#    set: {1,2,3}
#    str: "hello"



