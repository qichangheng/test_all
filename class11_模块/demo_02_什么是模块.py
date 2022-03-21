#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""
模块：.py 文件就是模块。【实际上 .pyc  .pyo pyd  so  dll, 】动态库
什么是包：包含了 __init__.py 的模块的文件夹（目录）

模块和包的作用：
就是为了组织代码。
"""

# print("demo_02", __name__)

def visit(url):
    print("正在访问网站：{}".format(url))

def respose():
    print("response")


if __name__ == '__main__':
    # __name__ == demo_02_什么模块
    # 写这个模块的测试代码。
    print("正在运行demo02")