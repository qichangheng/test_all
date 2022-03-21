"""
可变长参数：
*names, 在函数内部的表现形式：names 是元组。
可以接收从函数调用的时候，多余的位置参数.
*names 加在其他的位置参数的后面。

可不可以只有一个 *names, 可以的。

**kwargs, keyword args

"""

# def get_name(firstname, *names ):
#     """获取名字"""
#     print(firstname)
#     print(names)
#     return firstname
#
# get_name('yuz', 'wang', '高颜值')


# # 可不可以只有一个 *names, 可以的。
# def get_name(*names ):
#     """获取名字"""
#     print(names)
#
# get_name('yuz', 'wang', '高颜值')



# 可不可以只有一个 *names, 可以的。
def get_name(*names, **kwargs ):
    """获取名字"""
    print(names)
    print(kwargs)

get_name('yuz', 'wang' , middle='hello', yit='world')