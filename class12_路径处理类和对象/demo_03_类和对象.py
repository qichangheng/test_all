"""

一： 概念
什么是类？？
俗话说：人以群分，物以类聚。 种类/ 分类
英文单词： class

什么样的东西可以形成一个类？？
人类 、 禽类 、 兽类
因为他们有相似点。共同之处。

我：男
寒霜： 男   ===》》》》 Man  男人类
Girl

类：群体


什么是对象 object ？？又被称为 实例 instance
object: 东西
是一个群里当中的成员 / 个体

Man 类里面的 对象： 我，寒霜，开始


二：：：：：
类和对象在python 当中的表示

类的定义：
class 类名：
    类的组成部分

类的调用：
print(类名)
变量 = 类名
<class '__main__.Man'>
<__main__.Man object at 0x0000022ABEE74670>
看到有尖括号的，一般来说就是一个类 / 对象。

对象的表示方法：
类名()   ==> 对象的表示


类的命名：大驼峰命名： 两个单词的首字母大写。
class PerfectManHelp

函数的命名：下划线命名：perfect_man_help

变量命名：下划线命名.

"""
class Man:
    pass

# class Man(object):
#     pass

new_man = Man
print(new_man)
print(Man)
print(Man())
a = Man()
# 不要求掌握，
b = Man()
print(Man())
# is 判断另个变量两个值 是不是同一个对象。
print(a is b)
# 经典的面试题
print(Man() is Man())
# 如何去进一步确定是不是同一个对象
print(id(a))
print(id(b))


class Cat:
    pass


jiafei = Cat()
tom = Cat()
blue = Cat()
black = Cat()
dragon = Cat()

print(jiafei)
print(tom)
print(blue)

