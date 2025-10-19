
# 作业

# 已知列表 names = ['jeff','rain','jack','lucy','lance','feifei']
# a.往names列表里feifei前面插入一个alex

# ffIdx = names.index('feifei')
# # names[ffIdx] = 'alex'
# names.insert(ffIdx,'alex')
# print(names)
# print(names.reverse())
# print(names)
import random

num = random.choice(range(1,101))
print(num)
# b.把lucy的名字改成中文：路西

# c.往names列表里rain的后面插入一个子列表，[oldboy, oldgirl]

# d.返回lance的索引值

# e.创建新列表["佩奇", "喜羊羊"],合并入names列表

# f.取出names列表中索引4-7的4个元素

# g.取出names列表中索引2-10的5个元素，步长为2

# h.取出names列表中最后3个元素

# I.循环names列表，打印每个元素和索引值，如果索引值为偶数时，把对应的元素改成-1
names = ['jeff','rain','jack','lucy','lance','feifei']
for i,name in enumerate(names):
    print()
    if i % 2 == 0:
        # names[i]=-1
        print(i)


