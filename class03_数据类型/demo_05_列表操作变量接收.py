my_list = ['yuz', 'linghao', 'wuming']

new_elem = my_list.append("hello")
# new_elem = my_list

print(my_list)

# None 是一种特殊数据类型， 表示什么都没有。
# append 在原来的列表中添加一个元素到末尾
# append 得到的结果是为 None ,由python设计者决定的。
# 讲函数的时候
print(new_elem)

# remove
elem = my_list.remove('yuz')
print(elem)
print(my_list)

# pop函数 得到的结果是我们删除的元素
elem = my_list.pop(0)
print(my_list)
print(elem)

# 以后我们自己定义，我们可以控制结果 return


d = my_list.append('tt')
print(d)  # None