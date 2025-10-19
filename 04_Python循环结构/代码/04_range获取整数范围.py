
# range(start, stop, step=1): 整数范围
#   start: 起始值, 包含
#   stop: 结束值，不包含  [start, stop)前闭后开，左闭右开
#   step: 步长


print(range(5))
print(list(range(5)))  # [0, 1, 2, 3, 4]
print(list(range(0, 5)))  # [0, 1, 2, 3, 4]
print(list(range(2, 5)))  # [2, 3, 4]
print(list(range(6, 2)))  # []
print(list(range(2, 9, 2)))  # [2, 4, 6, 8]
print(list(range(6, 1, -1)))  # [6, 5, 4, 3, 2]



