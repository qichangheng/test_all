file = open('new_file.txt', mode='r+', encoding='utf-8')
# 写入数据

file.write('新内容')
print(file.read())
# 关闭文件
file.close()