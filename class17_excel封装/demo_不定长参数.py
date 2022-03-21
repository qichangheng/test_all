def add(*args):
    print(args)

# 不定长参数传参
add(3,4,5,6)

# 解包
actual_param = [3,4,5,6]
add(*actual_param)
# 函数调用的时候，实际参数前加*号，解包==》 脱衣服。