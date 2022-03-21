#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""
使用其他模块里面的函数，变量，类，模块导入，

务必要记住的模块导入方式
import ____：
    import 路径.路径.模块名 路径从你的项目根目录开始。
    使用：class11_模块.demo_02_什么是模块.visit()
    import 包名称

from ____ import _________
    可以简化其他模块的调用。  模块.visit()

扩展：
from ____ import *      从模块当中导入所有的代码， 就是可能会和这个模块里的函数重名。
from ____ import sth  as   other    as 重命名，取别名。  避免重复。

模块分类：
内置模块： python 自带的。 import os,
第三库模块: 别人写好的模块， 需要安装， pip install requests，import...  from ..import.
自定义模块: 自己写的模块，通常放在包， from 包 import 模块

"""


# print("demo_03", __name__)

#
# def visit(url):
#     print("自己的visit")
#
# import class11_模块.demo_02_什么是模块
# # from .. import
#
# class11_模块.demo_02_什么是模块.visit('')
#
#
# from class11_模块 import demo_02_什么是模块
# demo_02_什么是模块.visit('')
# demo_02_什么是模块.respose()
#
# # from ++++ import ++++
# from class11_模块.demo_02_什么是模块 import visit, respose
# visit('')
#
# # 导入所有的
# from class11_模块.demo_02_什么是模块 import *
# visit('')
# respose()
#
#
# # as 重命名
# # from class11_模块.demo_02_什么是模块 import visit as visit_another
# # visit_another()
#
#
# # import sys
# # print(sys.path)



if __name__ == '__main__':
    print("正在运行 demo03")