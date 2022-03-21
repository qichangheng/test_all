# 字符串索引，表示获取字符串当中的某 1 个元素

name = "课代表 多喝热水"

# 索引的表示方法： name[索引号]
# 在 python 当中，索引不是从 1 开始的，是从 0 开始。000000000000000
print(name[0])
# 多
print(name[4])
# 水
print(name[7])
print(name[-1])
# 获取字符串的长度 len()
name_len = len(name)
print(name[name_len - 1])

# 超出索引范围，报错！！！ IndexError
print(name[name_len])