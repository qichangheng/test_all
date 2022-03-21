# 进阶版异常捕获
# 指明出现的异常类型
# 先不要加异常，让他报错（开发主动试错）
# IndexError
# 对每一种不同类型的异常
# 分开处理，进行不同的处理。


# raise 手动抛出异常。让程序报错

# lst = ['yuz']
# try:
#     print(4 / 0)
#     lst[3]
# except IndexError as e:
#     print("出现异常：{}".format(e))
# except ZeroDivisionError as e:
#     print("出现除法错误：{}".format(e))
# finally:
#     # 不管有没有报错，fianally 都会执行的。
#     print("hello world")
#     # raise


#
def join_girl_team(age, gender):
    if age > 22:
        raise ValueError("age must be 小于 22 ")
    print("可以加入女子足球队")


join_girl_team(22, '女')


# 语法错误是不能被捕获的

# wofjo'asdf'


