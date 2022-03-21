a = "hello worlD"
print(a.upper())
print(a.lower())
print(a.title())
print(a.capitalize())
print(a.swapcase())

# get / post 进行规范

# replace() 替换某个字符
a = "燕子真是666"
b = a.replace("燕子", "小低调")
print(b)

# find 查找指定字符 ==> 得到的找到该字符串的索引位置
index = a.find("真是")
print(index)

# find 查找指定字符 ==> 不能找到，返回 -1
index = a.find("是真")
print(index)

# index == find
result = a.index("真是")
print(result)

# index 方法如果找不到就会报错 ValueError
# ValueError, 值错误
# result = a.index("是真")
# print(result)


# count() 查找字符的次数
song = "爱情是一种病，你爱他爱， 爱情不知道是什么鬼， 爱情买卖，"
print(song.count("爱情"))

"""
join()  字符串拼接的高级用法

split()

strip()
"""

# yuz,xiaojin,kaishi,ptim  ==>   CSV
a = "#".join(['http://ss.com/login', 'GET', 'lucky', '123456'])
print(a)

# 拆开
b = a.split('#')
print(b)

# strip 字符串去掉空格
word = '            sfowofwf           '
c = word.strip()
print(c)


# isdigital() 是否是正整数
print(c.isdigit())

# islower()



