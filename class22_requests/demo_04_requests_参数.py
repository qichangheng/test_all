import requests

# 发送 post 请求
url = 'http://api.keyou.site:8000/user/login/'

# 发送参数的方式：
# URL: query string: 查询字符串。GET基本上就是用 query string
# body: form /  json
# header

data = {
    "username": "lemon1",
    "password": "123456"
}

# data 表示 form 表单格式数据
# 本质上来说，content-type 设置成 form-data
# res = requests.post(url, data=data)
#
# # json 数据， json 关键字
# # content-type 设置成 application / json
# res = requests.post(url, json=data)

# 但是，有的接口是只支持 form
# 有的接口只支持 json
# 后端工程师规定对的 ， 看接口文档。

# 如何发送 query string
res = requests.post(url, params=data)

# form 表单格式数据

print(res)
print(res.text)
print(res.content)
print(res.json())