"""打开文件，有什么用？？
数据是写在文件当中的。
读取数据。
写入数据。
复制一张图片。
"""

# 打开文件
file = open("new_file.txt", 'r', encoding='utf-8')
# 读取数据
data = file.read()
print(data)
# 关闭文件
file.close()
