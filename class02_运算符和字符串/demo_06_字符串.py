
# 字符串
# 引号括起来的数据类型就是字符串
# 引号可以是单引号，也可以是双引号，还可以是三引号

# a = "jwfoewfjowfjssaf89932!!@@#$%%#%"
# print(a)
# print(type(a))
#
a = 'jwfoewfjowfjssaf89932!!@@#$%%#%'

# 三引号，可以多多行字符串,
# 三引号，也可以是双引和单引
a = """sklfweof
sfwofewfe
fsdfoowef

fw2fw2feo"""
print(a)

# 三引号什么时候是注释，什么时候又是字符串呢？
# 后面需要用到的就是字符串
print("""hello world""")

# 光不溜秋的就是注释
"""这是一波注释"""



# 成员运算 in     not in
names = "yuze duohereshiu kedaibiao"
print("yuzeduohereshiu" in names)


# + , 字符串可以用 + 号，表示字符串拼接起来
family_name = "wang"
last_name = "yuze"
print(family_name + " " + last_name)

# *, 字符串 * 数字， 表示重复多少遍
print(last_name * 5)

print("###" * 20)
print("#")
print("###" * 20)

# 字符串 * 字符串
print("##"  * "##")
