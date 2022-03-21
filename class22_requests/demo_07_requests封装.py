import logging

import requests

def visit(
        url,
        params=None,
        data=None,
        json=None,
        method='get',
        **kwargs
):
    """访问接口。

    返回字典 。 res.json()
    """

    if method.lower() == 'get':
        res = requests.get(url, params = params, **kwargs)
    elif method.lower() == 'post':
        res = requests.post(url, params=params, data=data, json=json)
    else:
        res = None

    try:
        return res.json()
    except Exception as e:
        logging.error("返回数据不是 json 格式：{}".format(e))
        return None



def visit_simple(
        url,
        params=None,
        data=None,
        json=None,
        method='get',
        **kwargs
):
    """访问接口。

    返回字典 。 res.json()
    """
    res = requests.request(
        method,
        url,
        params=params,
        data=data,
        json=json,
        **kwargs
    )

    try:
        return res.json()
    except Exception as e:
        logging.error("返回数据不是 json 格式：{}".format(e))
        return None


if __name__ == '__main__':
    # url = "http://api.keyou.site:8000/interfaces/"
    #
    # # 传递token
    # headers = {
    #     "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImxlbW9uMSIsImV4cCI6MTU5MTUwMDE0OSwiZW1haWwiOiJsZW1vbjEwMEBxcS5jb20ifQ.X33NEAsLQnP66myl7CQbsCoTiUozQ43GPn6izWOKM80"
    # }
    #
    # data = visit(url, method='get', headers=headers)
    # print(data)

    # 登录
    url = "http://api.keyou.site:8000/user/login/"
    info = {
        "username": "lemon1",
        "password": "123456"
    }
    user_info = visit(url, method='post', json=info)
    # 获取 token
    token = user_info["token"]

    url = "http://api.keyou.site:8000/interfaces/"

    # 传递token
    headers = {
        "Authorization": "JWT {}".format(token)
    }

    data = visit(url, method='get', headers=headers)
    print(data)


# class 类




