"""
关键字参数。

作用：还是相对于位置参数讲的。
可以提高函数调用时候的可读性，更加容易理解实际参数的意义。
关键字的名字==> 形式参数

关键字参数区别位置参数： 可以不按照顺序进行调用，可以交换顺序。

TODO: 关键字参数也要放到位置参数的后面。


函数：一定要掌握的知识：
return
函数的形式参数
函数的实际参数
函数的位置参数
默认参数：简化调用过程
关键字参数：可以交换参数的顺序，并且提高可读性

"""

def get_name(firstname, middle,  lastname=""):
    """获取名字"""
    return firstname + middle + lastname

a = get_name('王', lastname='雨泽',  middle='高颜值')
print(a)