# # with 语句可以让我们节省关闭文件的操作
#
# f = open("demo.txt")
# f.read()
# f.close()
#
# # 打开文件，用 f 去接受。
# # 上下文表达式
# with open("demo.txt") as f:
#     f.read()

# 不要这样写
# f = open('demo.txt')
# f.read()
# f = open("demo.txt", 'w')
# f.write('new_line')
#
# f = open('demo.txt')
# f.read()