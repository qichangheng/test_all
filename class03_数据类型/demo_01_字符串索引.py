# # step 可以省略, step 默认为 1
# name = "课代表 多喝热水"
# print(name[2: 3])
#
# # start 可以省略吗？？
# # start 省略， 0或 -1，最开始的地方
# print(name[:3])
#
# # end 可以省略吗？？
# # end 省略， 一直到最后
# print(name[1:])
# # vs name[1:-1]
# print(name[1:-1])
#
# # start 和 end 都可以省略吗？？
# # 全部取完，从开始到最后
# # name[:] 复制原来的文本
# print(name[:])
# print(name)

# 开始位置 > 结束位置
name = "课代表 多喝热水"
print("打印结果{}".format(name[3: 0]))