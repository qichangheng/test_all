"""while
主要用的场景没有 for 循环多。

while 循环：我不知道什么时候结束。。不知道运行多少次
"""

# 基本用法：
# while 条件:
#     pass

# 例子1：
# while 4 < 3:
#     print("我喜欢你")


# 例子2：执行流程
# 当吧 while 循环下面的子分支执行完毕以后，
# 程序会返回 while 条件判断语句。
# 其实是一个加强版的 if,,
# while 4 > 3:
#     print("我喜欢你")
#     print("你喜欢我吗？")
#     print("你猜？")

# while 循环是把for循环的机制手动化了。
cases = [
    {"url": "http://...", "method": "get"},
    {"url": "http://example", "method": "post"}
]

# index = 0
# while index < len(cases):
#     print(cases[index])
#     # 自动索引 + 1
#     index += 1

# break 语句
# index = 0
# while True:
#     print(cases[index])
#
#     if index == 1:
#         # 手工终止，强制终止 while 循环或者 for
#         print("索引为{}, 终止 while 循环".format(index))
#         break
#
#     index += 1
#
# print("接下来的代码")


# pass 语法
cases = [
    {"url": "http://...", "method": "get"},
    {"url": "http://example", "method": "post"}
]

# continue 是表示跳过此次子语句，进入下一个循环判断
# if 1:
#     # 当有冒号有子语句的时候，目前还不知道这个语句怎么写
#     pass
#
# elif 2:
#     print("hello world")


# while 嵌套

while True:
    print("第一层")
    while True:
        print("第二层")



