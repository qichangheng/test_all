import requests

# 发送 post 请求
url = 'http://api.keyou.site:8000/user/login/'

data = {
    "username": "lemon1",
    "password": "123456"
}

res = requests.post(url, json=data)

print(res)
print(res.text)
print(res.content)
res_data = res.json()

# 获取 token
token = res_data["token"]
print(token)


# 访问 interface 接口

url = "http://api.keyou.site:8000/interfaces/"

headers = {
    "Authorization": "JWT {}".format(token)
}

res = requests.get(url, headers=headers)

print(res.json())