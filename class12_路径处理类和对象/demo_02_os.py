#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

# 第一种
import os.path
# 第二种方式
from os import path
# os.path 主要处理系统路径相关的操作。
#

# 获取文件的绝对路径
# 什么是绝对路径？？  从系统的盘符或者是系统根目录开始，
# 相对路径。  一个路径相对于另一个路径的说法。
# D:  D:\班级管理

# 用得最多的是 os.path.abspath(__file__)
# 因为绝对路径不会变

print(os.path.abspath(__file__))   #demo_02_os,   class12_路径处理类和对象\demo_02_os.py

# __file__
# __name__
print(__file__)     # 文件路径(相对）
print(__name__)   #模块名，没有路径


# 获取现在的文件绝对路径
file_path = os.path.abspath(__file__)
print("filepath", file_path)

# 获取上一级路径
dir_name = os.path.dirname(file_path)


# 路径拼接  文件  /  文件
# 所有获取到的路径，只是一个路径的表示，并不代表这个文件或者路径真的存在。
# 说白了：路径得到的是一个字符串。这个字符串是一个路径格式 `\` ，
txt_path = os.path.join(dir_name,  'demo.txt' )


with open(txt_path, 'w') as f:
    f.write("new txt file")


# 获取当前工作目录
print(os.getcwd())

# 创建一个新的目录（文件夹）
if not os.path.exists("subdir"):
    print(os.mkdir('subdir'))

# 判断一个路径存不存在
# print(os.path.exists("d:\olg"))

# 判断路径是否是一个文件
# 获取到的路径得到是一个字符串。
print(os.path.isfile(os.getcwd()))
print(os.path.isdir(os.getcwd()))

# 判断路径是否是一个目录











