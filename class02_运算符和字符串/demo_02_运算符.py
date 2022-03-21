#  加减乘除

a = 1 + 3
print(a)
b = a - 2
print(b)
c = b * 3
print(c)

# 为什么除法得到不是整数？？
# 除法会遇到除不尽，
# 使用了除法数据类型会转化成浮点数。

d = c / 2
print(d)

# 除法注意事项2：
# e = 7 / 0
# print(e)


# 幂运算
f = 5 ** 3
print(f)

# 整除
g = 15 // 2
print(g)

# 取余数:  模运算
h = 15 % 2
print(h)


# 经常用来进行 奇数和偶数判断。
a = input("请输入你的数字：")
print( int(a) % 2)