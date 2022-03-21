
# 第一步打开文件
# f = open("demo.txt")
# data = f.read()
# print(data)
#
# # 换行符分割 `\n`
# new_data = data.split("\n")
# print(new_data)

# 读取文件是根据光标的移动读取，读取一个字符， 就把光标移动一个字符。
# 写入也是一样的。没写一个字符，就移动字符的光标

f = open('demo.txt', 'r')
f.write('new line')
f.close()


f = open('demo.txt', 'r')
print(f.read())
# 打印空的。
