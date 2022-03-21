# 局部变量：函数体这个局部， 函数是一个盒子。
# 全局变量:

# 全局能获取局部变量吗？？？ 不能！！！！
# 局部作用域能获取全局变量吗？？  能！！！！


# def add(a, b):
#     c = a + b
#     c += 5
#     return c
#
# c = 4
# add(5,7)
# print(c)



# 局部作用域能获取全局变量吗？？  能！！！！
# c = 10
# def add(a, b):
#     return c + a + b
#
# print(add(2,3))



# 全局能修改局部变量吗？？  不能！！！！
# 不能获取，更不用说修改

# def add(a, b):
#     return a + b
#
# a = a + 1


# 局部变量能修改全局变量吗？？？
# 不加 global 表明是全局变量，是不能修改全局变量的。
# 如果想在局部去修改全局变量，加 global 表明这是一个全局变量
# global 关键字声明全局变量的关键字， 不要轻易使用。


c = 3

def add(a, b):
    global c
    c = c + 3
    print(c)
    return a + b + c

add(3, 4)
print("最后的c:", c)
