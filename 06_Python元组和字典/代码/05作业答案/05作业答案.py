
# 作业

# 已知列表 names = ['jeff','rain','jack','lucy','lance','feifei']
# a.往names列表里feifei前面插入一个alex
names = ['jeff','rain','jack','lucy','lance','feifei']
# names.insert(-1, 'alex')
names.insert(5, 'alex')
print(names)

# b.把lucy的名字改成中文：路西
# names[3] = '路西'
names[names.index('lucy')] = '路西'
print(names)

# c.往names列表里rain的后面插入一个子列表，[oldboy, oldgirl]
names.insert(2, ['oldboy', "oldgirl"])
print(names)

# d.返回lance的索引值
print(names.index('lance'))

# e.创建新列表["佩奇", "喜羊羊"],合并入names列表
new_names = ["佩奇", "喜羊羊"]
# print(names + new_names)
names.extend(new_names)
print(names)

# f.取出names列表中索引4-7的4个元素
print(names[4:8])

# g.取出names列表中索引2-10的元素，步长为2
print(names[2:11:2])

# h.取出names列表中最后3个元素
print(names[-3:])

# I.循环names列表，打印每个元素和索引值，如果索引值为偶数时，把对应的元素改成-1
for i,n in enumerate(names):
    print(i, n)
    if i%2 == 0:
        names[i] = -1

print(names)
