if 4 > 5:
    print('hello')
elif 4 == 5:
    print("world")


print("其他的内容")

# 结论：python 运行一个文件的时候，会查看所有顶格写的代码。（一个 if 表达式只会看某一个满足条件的语句）


# if a: 例子

a = ''



if 1:
    pass

if 2:
    pass

if 3:
    pass

else:
    pass


# dalao = ['yuz', 'xuehua', 'ptim']
# for i in dalao[1]:
#     print(i)

# 字符串也是可以进行 for 循环。（容器对象，序列）
# 可迭代对象 iterable
# 列表，字典，元素，字符串，集合

my = {'a', 'b', 'c'}

# for i in my:
#     print(i)
#     # next()
#     # index + 1


cases = [
    {"url": "http://...", "method": "get"},
    {"url": "http://example", "method": "post"}
]

#
# for case in cases:
#     # {"url": "http://...", "method": "get"},
#     for k,v in case.items():
#         print(k, v)


for i in range(100):
    print("我喜欢你")