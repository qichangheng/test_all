
"""
__name__ 是表示当前文件的模块名。


运行文件 、 脚本。 1， 是模块， 特殊的模块
我们是通过这个文件运行程序的

通过模块导入形式运行的， __name__ 就是文件名、模块名称
直接运行的文件，脚本， __name__ 就不是文件名，模块名称，是固定的：__main__
"""

from class11_模块 import demo_02_什么是模块
from class11_模块 import demo_03_模块导入

# print("demo_04", __name__)


# if __name__ == '__main__':
#     print("正在运行 demo_04")


import requests

resp = requests.get('http://www.baidu.com')
print(resp)