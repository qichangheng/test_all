"""
return :
1, 函数遇到 return 就终止
2， 函数的返回值 return， 函数调用以后可以通过 变脸接收 return 值，
函数的输出数据是由 return 决定的

"""

def add(a, b):
    """添加"""
    c = a + b
    print("hello world")
    return c
    

# # 直接打印
# print(add(5, 6))
# # 第二种方式：通过变量接收
# c = add(6, 8)
# print(c)

# 函数里面 return 表示函数的返回值，可以在调用函数之后通过变量进行接收
# return 知识点2： 函数体遇到 return 就终止运行, 相当于 for/ while 的 break,


# 例子二：

# def add(a, b):
#     if a > 100:
#         return a + b
#     elif a == 100:
#         return a + 2*b
#     else:
#         return a + 3 * b

# print(add(3, 6))

# 例子 3：
# def add(a, b):
#     if a > 100:
#         return a + b
#     else:
#         return a + 3 * b
# print(add(111, 2))


# 例子4

def add( a, b):
    c = a + b
    print(c)
    # return 
    

# 函数调用以后得到的数据是由 return 决定的。
# 函数没有 return , 得到的数据就是 None
# result = add( 3,  2)   # None
# print(result + 4)


# append 之前
# my_list = ['yuz', 'a']
# a = my_list.append('开始')  # 方法
# print(a)

# 自己实现一个 append
def append(origin_list,  element):
    """对列表进行数据添加"""
    origin_list.append(element)
    return origin_list

# print(append(['yuz'], '阿七'))

# orgin_list = ['yuz']
# element = '阿七'
# 形式参数： 函数在定义的时候写的参数。变量名  origin_list      ,  element
# 实际参数： 函数在调用的时候写的参数。他是值       = ['yuz']       ='阿七'
# 位置参数 positional argument： 形式参数和实际参数要一一按照顺序对应。不多不少， 位置一样。
# a  = 'hello'

# print(append(['yuz'] ))   # 报错，缺少位置参数 element

# print(append(['yuz'] , '阿七', '阿七'))   # 报错， 需要 2 个位置参数，但是你给了 3 个

# print(append('阿七', ['yuz']))  # 顺序要保持一致

# 默认参数： 在函数定义的时候，给形式参数一个默认值
# 如果有默认值，在函数调用是如果位置参数一一对应，掺入了实际参数，默认参数不会生效。
# 如果没有传入实际参数，默认值会生效。

def append(origin_list,  element=None):
    """对列表进行数据添加"""
    origin_list.append(element)
    return origin_list

print(append(['yuz']))



# 关键字参数
# 位置参数，默认参数和关键字参数的组合使用
# 不定长参数（ *args,  **kwargs）
# 函数的相互调用
# 函数的作用域。







