# ----------------
# readlines() 读取每一行， 会存放到列表当中，每一个行的内容就一个列表的一个元素。
# read() 得到的是整个一个字符串
# --------------------
f = open('demo.txt')
lines = f.readlines()
print(lines)

# 分行打印
for line, data in enumerate(lines):
    if line == len(lines) - 1:
        # 最后一行
        print(data)
    else:
        # 其他行。
        print(data[:-1])




