

# 列表推导式: (掌握)
#    使用for循环用一行来生成列表

# 创建一个列表
print(list(range(1, 6)))
nums = [1, 2, 3, 4, 5]

nums2 = []
for i in range(1, 6):
    nums2.append(i)
print(nums2)

# 列表推导式：用一行代码快速生成新列表
nums3 = [i  for i in range(1, 6)]
nums3 = [i*2  for i in range(1, 6)]
nums3 = [i  for i in range(1, 10) if i%2]  # 奇数列表 [1, 3, 5, 7, 9]
nums3 = [i  for i in range(1, 10) if i%2 and i%3==0]  # [3, 9]
nums3 = [i  for i in range(1, 10) if i%2 if i%3==0]  # [3, 9]

nums3 = [i+j  for i in "ABC" for j in "123"]  # 循环嵌套
# ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
print(nums3)



# 字典推导式(了解)
d = {f'name{i}': i for i in range(1, 6)}
print(d)  # {'name1': 1, 'name2': 2, 'name3': 3, 'name4': 4, 'name5': 5}


# 集合推导式（了解）
s = {i for i in range(1, 6)}
print(s)  # {1, 2, 3, 4, 5}
