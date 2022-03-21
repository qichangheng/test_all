yuz_age = input("雨泽的年龄：")
xiaowangzi_age = input("小王子的年龄：")

if int(yuz_age) > int(xiaowangzi_age):
    print("29期的人每个给雨泽 10 块钱")
    if 1:
        print("hello")
elif int(yuz_age) < int(xiaowangzi_age):
    print("雨泽给29期总共 10 块钱")

# 2 个条件表达式
if int(yuz_age) >= int(xiaowangzi_age):
    print("没有钱分")
    if True:
        print("world")
else:
    print("不可能")