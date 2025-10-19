
# 回调函数： (了解)
#   把函数当作参数传入另一个函数中

def fn(n, cb):  # cb:callback  cb=lambda x: x**2
    print('n:', n)  # n: 3
    n2 = cb(n)
    print('n2:', n2)  # n2: 9

fn(3, lambda x: x**2)


#
def fn(n, cb):
    print('n:', n)  # n: 3
    n2 = cb(n)  # 回调
    print('n2:', n2)  # n2: 9
    return n2 * 2

# callback是回调函数
def callback(x):
    return x**2

n3 = fn(3, callback)
print("n3:", 18)
print()

#  自定义过滤器
# filter: 过滤,找到符合要求的数据
# n = filter(lambda x: x>0,  [1, -2, 3, -4, -5, 7, 6, -9])

def filter2(cb, l):
    l2 = []
    for n in l:
        if cb(n):  # 回调
            l2.append(n)
    return l2

n = filter2(lambda x: x > 0, [1, -2, 3, -4, -5, 7, 6, -9])
print(n)  # [1, 3, 7, 6]




# sort(key=lambda)
list1 = [
    {'name': '张三', 'age': 18, 'score': 50, 'tel': 18866669999, 'sex': '不明'},
    {'name': '李四', 'age': 16, 'score': 88, 'tel': 18866668998, 'sex': '男'},
    {'name': '王五', 'age': 17, 'score': 48, 'tel': 18866667995, 'sex': '女'},
    {'name': '陈一军', 'age': 61, 'score': 59, 'tel': 18866669998, 'sex': '不明'},
    {'name': '陈二军', 'age': 49, 'score': 88, 'tel': 18866669396, 'sex': '男'},
    {'name': '陈三军', 'age': 49, 'score': 61, 'tel': 18866668994, 'sex': '女'}
]
# 需求1：把上面list1按照age升序
list1.sort(key=lambda d: d['age'])
print(list1)

# 需求2：把上面list1按照score降序
list1.sort(key=lambda d: d['score'], reverse=True)
print(list1)


# 按照数字升序
list2 = [
    ('张三', 18),
    ('李四', 16),
    ('王五', 17),
    ('陈一军', 61),
    ('陈二军', 49),
    ('陈三军', 48)
]

list2.sort(key=lambda t: t[1])
print(list2)

