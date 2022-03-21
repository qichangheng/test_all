"""
什么是初始化？？
要通过定义的类得到一个具体的对象。  生出来，造出来。

对象个体，初始化过程保证生出来是不一样的。
我们自己给东西进行出厂设置。

特定的方法中去控制：
__init__

实例属性的定义2：
1， 类外面：  对象名.属性
2， 类里面：  self.属性


__init__ 定义的形式参数 和  对象的实例化 a = Man() 的实际参数，是一一对应的。
1. 必须 return None
2. 传入的参数必须要设置成实例属性，才能被被对象访问到。


self: 在 **类里面** ，表示一个 **对象**   他自己。自我， this
cls, ： 在 **类里面** ，表示一个 **类**   他自己。自我， this


实例方法当中，可不可以去定义实例属性。？？

"""

# def run():
#     pass

class Man:
    # 定义类属性
    gender = '男'
    power = "强"
    handsome = 'very very'

    def __init__(self,  name, face_shape='圆脸'):
        """对象的初始化过程。 让对象之间长得不太一样。"""
        # 定义, 在类里面，定义实例属性使用 self.属性 = ...
        self.face = face_shape
        self.name = name


    @staticmethod
    def tianqiyubao():
        print("天气预报：今天是晴天。")

    @classmethod
    def eat(cls):
        print("正在吃饭")
        print(cls.power)
        return "hello world"

    def drink(self, brand):
        """喝。。。"""
        print("{} 正在喝 {} 酒".format(self.name, brand))
        # self.play_game()
        self.eat()
        # 定义实例属性
        self.single = False

    def play_game(self):
        """玩游戏"""
        print("玩游戏")



yuz = Man('yuz', '方脸')

# print(yuz.face)
# print(yuz.name)
# yuz.drink('茅台')

# 整容的权利，可以后天改变属性
# yuz.face = "帅脸"
# print(yuz.face)


# 初始化以后 。 single 属性是后天定义的，
yuz.drink('五粮液')
print(yuz.single)
yuz.single = True
print(yuz.single)


# a
# print(a)
