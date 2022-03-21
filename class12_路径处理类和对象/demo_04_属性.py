
"""
什么是属性？？？
表示的是类/对象的特征。

特征是别人不具备的。

类属性（类变量）：  这个类的特征，这个群体的特征， 别的类（别的群体）可能不具备
实例属性（实例变量） ：  给个个体的特征，类当中的其他成员可能不具备。


类属性的获取：
类名.属性

类属性：可以先天定义也可以  后天学习（手工添加）
"""

class Man:
    # 定义类属性
    gender = '男'
    power = "强"
    handsome = 'very very'


print(Man.power)  # Man类的power属性
print(Man.gender) # Man类的gender属性

# 后天学习（手工添加的）
Man.hello = 'hello world'
print(Man.hello)

# 实例属性的后天学习获取
yuz = Man()
# yuz.handsome = 'very very'
print(yuz.handsome)

kaishi = Man()
kaishi.handsome = '一丢丢'
print(kaishi.handsome)
