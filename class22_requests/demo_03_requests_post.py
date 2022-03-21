import requests

# 发送 post 请求
url = 'http://api.keyou.site:8000/user/login/'

res = requests.post(url)

print(res)
print(res.text)
print(res.content)
print(res.json())