#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import logging   # 内置模块


python29 = [
    ['无名之辈', "钉钉"],
    ['阿七', "小胖"],
    ["钩子", "开始"],
    ["小凌", "小罗"]
]

for group in python29:
    # logging.debug
    logging.debug("group = {}".format(group))
    # print(group)
    for name in group:
        logging.debug("name = {}".format(name))

# info
# print(python29)
logging.info(python29)


if type(python29) == list:
    logging.warning('注意：现在我们支持 dict ， 但是之后我们会取消dict支持。')


# 版本真的迭代之后，取消对 dict 支持以后
if type(python29) == list:
    logging.error("不要用 dict 了！！！")
    # raise ValueError()

