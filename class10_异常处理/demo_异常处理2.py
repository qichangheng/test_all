
# 最基础的异常捕获
# 好程序员：会知道哪一行代码是需要加异常处理的。
# 会知道什么代码需要放到 try
# 异常是好的还是坏的？？
# 出现异常是好事还是坏事？


# lst = ['yuz']
# print(lst[3])
# print("hello")

# lst = ['yuz']
# try:
#     print(lst[0])
# except:
#     print("我错了，女装大佬")

# a = 'a'
# b = 'b'
# try:
#     print(a * b)
# except:
#     print("参数错误，记录日志")

# a = 4
# b = 0
# print( a / b)

a = 4
b = 0
lst = ['yuz']
# try:
#     print( lst[3] )
#     print(a / b)
# # with open() as f:
# # 讲捕获的异常赋值给 err 变量
# except Exception as err:
#     print("程序出现错误 {}".format(err))


try:
    print( lst[3] )
# with open() as f:
# 讲捕获的异常赋值给 err 变量
except Exception as err:
    print("程序出现错误 {}".format(err))

try:
    print(a /b)
except Exception as err:
    print("程序出现错误 {}".format(err))


