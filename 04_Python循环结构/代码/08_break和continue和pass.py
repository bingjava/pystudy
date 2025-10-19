
# break: 主动结束循环
#   1.要写在循环中, 作用是主动结束循环,break之后的语句不会再执行
#   2.break只会跳出当前这一层循环(在循环嵌套的情况下)
#   3.break 和 for-else(while-else) 结合使用

# 需求: 找到1~10之间的第一个能被3整除的数 （break）
'''
for i in range(1, 11):
    print(i)
    if i%3 == 0:
        break
'''

for p in range(1, 6):
    print(f'------- p={p} --------')
    for i in range(1, 11):
        print(i)
        if i%3 == 0:
            break



# for-else (了解)
# while-else

# 给一个数n, 判断该数是不是 素数(质数) : 除了1和自身以外,中间不能被其他数整除
# 比如: 2, 3, 5, 7, 11, 13, 17, 19, 23, ...
n = 23
for i in range(2, n):
    if n%i == 0:
        print(n, '不是素数，是合数！')
        break
else:
    print(n, '是素数')

print('end')

# for-else:
#   1. 需要和break结合使用
#   2. break和else只会执行其中一个
#   3. else执行:是在for正常循环结束后才执行(没有break)






# continue: 跳过当次循环,继续执行下一次循环
for i in range(1, 10):
    if i % 3 == 0:
        continue
    print(i)


# pass:
#    没有任何语义, 占位语句, 作用是防止报错

if 1:
    pass


