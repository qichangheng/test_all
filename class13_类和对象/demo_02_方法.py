"""
方法：表示类 、 对象的行为。
方法本质上是函数。

属性名称：名词。
方法：动词，


方法 vS  函数：
1, self
2, 放在类里面，缩进的。
3， 调用过程不一样。 方法需要加前缀，类名或者对象名。
函数前面要么不加，要么加的模块名。

# 对象.方法()
Man().drink()

# 实例方法，对象方法：
1， 第一个参数名称，规定是 self,
2,  实例方法在调用的时候，前缀是对象，不能是类

# 类方法：
1, 在方法的上面添加 @classmethod
2, 把实例方法当中的 self 改成 cls,

# 静态方法
静态方法表示： 方法的上面加上一个 @staticmethod
不需要用 self， cls 作为固定参数

是刚刚好放在一个类当中的普通函数而已。
除了放在类当中，和普通函数没什么区别。

没有实际作用，和类或者对象没有关系（联系），
为什么要用静态方法、为什么要把普通的函数放到类当中去？？
方便管理

调用静态方法。
静态方法，（普通函数） 只需要在调用静态方法，前面加上类名或者对象名

类外面的普通函数：普通函数不需要加类，模块



实际使用当中：
实例方法： 98% ， 实例方法占大多数情况。
不知道用什么方法，就用实例方法。

类方法：后面会有特殊情况

静态方法： 可以用普通函数代替，不是必须的。（管理方便。）
 """



class Man:
    # 定义类属性
    gender = '男'
    power = "强"
    handsome = 'very very'

    @staticmethod
    def tianqiyubao():
        print("天气预报：今天是晴天。")

    @classmethod
    def eat(cls):
        print("正在吃饭")
        return "hello world"

    def drink(self):
        """喝。。。"""
        pass

    def play_game(self):
        """玩游戏"""
        pass

# # 对象.方法()
# Man().drink()
#
# yuz = Man()
# yuz.drink()

# 行为是属于某一个人的。不能被类调用的
#  不 OK,  Man.drink()

# 打印函数的调用打印出来的是函数的返回值。
# def run():
#     pass
#
# print(run())


# print(Man.eat())
# print(Man().eat())


# 静态方法的使用
Man.tianqiyubao()
Man().tianqiyubao()