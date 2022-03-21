a = "123"
print(int(a))
print(type(int(a)))

# b = "abc"
# print(int(b))

# c = "abc"
# print(float(c))

# 重点内容：bool()
# 以下情况 bool 转化为 False, 意思为空或者0

print(bool(1))  # True
print(bool(0))  # F
print(bool(-1))

# "yuze wang"  "yuzewang"
print(bool(" "))  # True
print(bool(""))  # False