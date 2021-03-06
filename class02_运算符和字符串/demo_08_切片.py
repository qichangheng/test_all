# 字符串切片
# 切片：是获取字符串的多个元素
# 如何表示：name[切的起始点 : 切的终点]
# 切片： 顾头不顾腚， 取左不取右， 右边的要 + 1
#
name = "课代表 多喝热水"
print(name[1: 3 : 2])

print(name[4: 6])

# name[切的起始点 : 切的终点 : 步长]
# 步长 step: 获取第一次以后， 加多少个索引去获取第二次
num = "010101010101010101"
print(num[1: 5 : 2])  # 1 + 2 + 2

print(num[2: 8 : 3])

print(name[1: 7 : 3])

# 范围超出
# 在切片当中，超出范围，是不报错的。是表示取完的意思
print(name[1: 1000000000])

# 下一节课字符串 step 可以是负数
# 倒序
name = "课代表 多喝热水"
print(name[::-1])
