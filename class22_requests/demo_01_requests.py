#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

# 导入 requests
# 客户端是什么？？ 浏览器，postman，python, user-agent
import requests

# 发送 GET 请求， 需要传递参数， URL
url = "http://www.baidu.com"
res = requests.get(url)

# 响应对象
print(res)

# 响应状态码
print(res.status_code)

# 获取返回的数据
# print(res.text)
# HTML 页面

print(res.json())




# print(res.content)



