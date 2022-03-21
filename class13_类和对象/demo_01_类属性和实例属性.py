#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽


"""

# 类属性和实例属性：

# 类属性：所有的成员都是一样的。
# 实例属性：不是每个成员都一样



# 第二个区别：
#类属性，可以被实例、对象访问
# 实例属性， 不可以被类获取
"""

class Man:
    # 定义类属性
    gender = '男'
    power = "强"
    handsome = 'very very'


yuz = Man()
kaishi = Man()

print(yuz.gender)
print(kaishi.gender)

yuz.eye = '蓝色'
# AttributeError, 属性错误。
# print(kaishi.eye)


# 第二个区别：
#类属性，可以被实例、对象访问
# 实例属性， 不可以被类获取
print(Man.eye)
