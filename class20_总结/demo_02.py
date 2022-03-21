#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

lst = [
    ['name', 'age', 'gender'],
    ["yuz", 16, "男"],
    ['tt', 18, '女'],
    ["wuming", 19, "不知道"]
]


# 列表转化成字典
def list_to_dict(lst):
    """嵌套的列表转化成字典。
    lst = [
    ['name', 'age', 'gender'],
    ["yuz", 16, "男"],
    ['tt', 18, '女'],
    ["wuming", 19, "不知道"]
    ]

    ===》 [
    {},
    {},
    {}
    ]
    """

    new_lst = []
    title = lst[0]
    for column in lst[1:]:
        dic = {}
        for idx, e in enumerate(column):
            key = title[idx]
            dic[key] = e
        new_lst.append(dic)
    return new_lst

# 列表
antoher= [
    (),
    (),
    ()
]


# 任何一个类，都是父亲，继承下来
class Demo:
    pass

class Demo1():
    pass

class Demo2(object):
    pass