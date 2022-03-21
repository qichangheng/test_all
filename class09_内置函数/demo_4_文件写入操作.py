#写入文件
# 在 w 模式下，如果之前没有这个文件，将会创建新文件
# 写入中文需要指定编码格式为 utf-8, GBK
# TODO: 坑1：如果之前已经存在同名文件，使用 mode='w' 模式，会覆盖之前的文件内容。

# mode = 'a', 追加模式
# mode = 'x', 原创模式，独创模式
# mode = 'b'， 二进制模式，  't'文本

# file = open('new_file.txt', mode='a', encoding='utf-8')
# # 写入数据
# file.write("英文太多，我记不住")
# # 关闭文件
# file.close()


file = open('new_file.txt', mode='at', encoding='utf-8')
# 写入数据
file.write("英文太多，我记不住")
# 关闭文件
file.close()