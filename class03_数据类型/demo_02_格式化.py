name = "雨泽"

###############
# 雨泽
###############

print("###"* 4)
print("#" + " " + name)
print("###" * 4)

name = input('名字：')
age = input("年龄：")
gender = input("性别：")

# print("最帅的是谁: {}".format(name))

#  变量比较多的情况
print("""
最帅的是谁: {username}
他的芳龄：{nianling}
性别是：{username}
""".format(username=name, nianling=age, sexy=gender))


