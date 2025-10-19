
# 1. Python内部提供的包或模块（官方）
# 2. 我们自己写的包或模块（自己的）
# 3. 别人写的包或模块： 第三方包或模块


# 安装第三方包
#  1.在pycharm的settings中去安装
#  2.先导入包名,如果报错,鼠标悬停到包名,根据提示安装
#  3.命令安装:(重要，推荐）
#       pip install numpy 安装包
#       pip uninstall numpy 卸载包
#       pip show numpy  查看包详情
#       pip list  查看所有包
#       pip  freeze  查看你自己安装的包(==版本号)

#       pip  freeze  >  requirements.txt  将当前环境中的包导出到文件requirements.txt中
#       pip  install  -r  requirements.txt  安装 requirements.txt 文件中的包

#    如果安装很慢,我们要尝试更换镜像:
#       pip install numpy  -i  https://pypi.tuna.tsinghua.edu.cn/simple

#   设置永久镜像:
#       pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

import requests
import numpy as np
import pandas  as pd

'''
import numpy as np
import pandas  as pd
import matplotlib.pyplot as plt  # matplotlib

import flask
import tornado

'''