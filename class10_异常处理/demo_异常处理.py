# 异常，是程序出现了意想不到的情况。
# 有异常出现，你要不要解决？？
# 如果异常不解决，程序会奔溃，停止运行。

# 异常捕获，捕获异常
# 如果出现了异常，我们会让他按照事先规定的规则去执行对应的操作：记录错误日志。log
# try 要运行的有可能发生异常的代码 ：
#        代码
# except 异常：
#        出现异常的时候要运行的代码（执行的操作），记录日志

# 一旦 try 当中出现异常，立即调到 except 子句，try 剩下的代码不会再执行。

# 不停的 try:


# 不会出现异常的代码
try:
    lst = ['yuz', 'bt', 'wfe', 'fwo']
except:
    pass



try:
    # 有可能出现异常的代码
    # 会执行
    print(lst[3])
    print(list[10])
    print("try....")
    print("try....")
    # 一旦 try 当中的代码报错，立即调到 except,
    # try 报错代码的下面将不会继续执行。
except:
    # 如果出现异常，会执行 except 分支的代码
    print("记录错误日志")
    # raise()

print("running .....")
print("finish")