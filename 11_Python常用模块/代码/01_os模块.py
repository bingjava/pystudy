import os

# os  用于获取系统的功能，主要用于操作文件或者文件夹

# print(os.name)  # nt 表示window操作系统
# print(os.getcwd())  # 当前目录


# 创建目录: mkdir()  如果文件存在会报错
# 创建多层目录: makedirs('a/b/c')
if not os.path.exists('hello'):
    os.mkdir('hello')

# os.makedirs('a/b/c')


# 删除空目录: rmdir  (了解)
# os.rmdir('hello')

# 删除文件: remove  （了解）
# os.remove('aa.txt')

# 重命名: rename（了解）
# os.rename('hello', 'hello2')



# listdir() : 返回指定目录下的所有文件或文件夹名组成的列表
dir_list = os.listdir(r'C:\Users\EDY\Desktop\Python\pythonProject\11_Python常用模块\代码')
print(dir_list)


# os.path
#  os.path.exists : 文件或文件夹是否存在
#  os.path.isfile() : 是否为文件
#  os.path.isdir() : 是否为目录
print(os.path.exists(r'C:\Users\EDY\Desktop\Python'))  # True
print(os.path.isfile(r'C:\Users\EDY\Desktop\Python'))  # False
print(os.path.isdir(r'C:\Users\EDY\Desktop\Python'))  # True


# 合并路径
print(os.path.join(r'C:\Users\EDY\Desktop\Python', 'a.py'))
# C:\Users\EDY\Desktop\Python\a.py


# 需求: 将指定目录下的子目录的绝对路径打印
path = r'C:\Users\EDY\Desktop\Python\pythonProject\11_Python常用模块\代码'
dir_list = os.listdir(path)
# print(dir_list)
for dir in dir_list:
    # 拼接路径
    path2 = os.path.join(path, dir)
    # print(path2)

    if os.path.isfile(path2):
        print("文件:", path2)
    else:
        print('目录:', path2)


# 绝对路径: 从盘符开始的路径
# 相对路径: 从当前文件所在目录开始的路径

# os.path.split : 拆分 (了解)
# print(os.path.split(r'C:\Users\01_os模块.py'))
# ('C:\\Users', '01_os模块.py')

# os.path.splitext() : 拆分文件的扩展名  (了解)
# print(os.path.splitext(r'01_os模块.py'))
# ('01_os模块', '.py')

# 文件大小:字节  (了解)
# print(os.path.getsize('hello.json'))  # 204字节

# 绝对路径  (了解)
# print(os.path.abspath('hello.json'))
# C:\Users\EDY\Desktop\Python\pythonProject\11_Python常用模块\代码\hello.json




