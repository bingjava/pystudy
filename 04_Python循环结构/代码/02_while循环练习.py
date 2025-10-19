''' '''
# 练习：
# 1. 打印1-100之间的所有偶数
i = 1
while i <= 100:
    if i%2 == 0:
        print(i)
    i += 1

# 2.求 1-100之间可以被6整除的数的个数
count = 0
i = 1
while i <= 100:
    if i%6 == 0:
        count += 1
    i += 1
print(count)

# 3. 打印1-100之间的所有奇数
i = 1
while i <= 100:
    if i%2 == 1:
        print(i)
    i += 1

# 4.计算1到100以内所有偶数的和。
s = 0
i = 1
while i <= 100:
    if i%2 == 0:
        s += i
    i += 1
print(s)

# 5.计算1到100以内所有能被3或者7整除的数的和。
s = 0
i = 1
while i <= 100:
    if i%3 == 0 or i % 7 == 0:
        s += i
    i += 1
print(s)

# 6.计算1到100以内能同时被7和3整除的数的个数。
count = 0
i = 1
while i <= 100:
    if i%3 == 0 and i % 7 == 0:
        count += 1
    i += 1
print(count)

