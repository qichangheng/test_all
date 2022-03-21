# 列表的表示, [] 表示列表
# 列表：是存储多个数据的数据类型
# list()

my_list = ['yuz', 'nocturne', "热水"]
print(my_list)

# 列表可以存储多种数据类型
# 列表就是百宝箱，你什么数据都可以往里面丢。
# Java, c, 不可以
my_list = ['yuz', 18, [45, '23', "num"] ]
print(my_list)

# 列表的长度？？
print(len(my_list))

# 获取某一个元素，索引
# 字符串索引操作，可以直接使用到 列表当中
# 列表索引得到的结果：该元素是什么数据类型，得到的结果就是什么类型~！
print(my_list[-2])

# 切片
print(my_list[0: 2])


# 增加元素， 增加一个元素
# 列表的最后添加一个元素
my_list.append("存储一百万")
print(my_list)
# 指定的索引位置添加一个元素
my_list.insert(1, "周杰伦")
print(my_list)

# 同时加多个元素, 列表合并
my_list.extend(['燕子', "hs", "周杰伦"])
print(my_list)

# 删除元素
# 删除指定的内容位置
# 如果找不到，会报错。
# my_list.remove('周杰')
# print(my_list)

# 删除指定的索引位置
# my_list.pop(0)
# print(my_list)

# 修改某个元素
my_list[0] = '无名之辈'
print(my_list)


