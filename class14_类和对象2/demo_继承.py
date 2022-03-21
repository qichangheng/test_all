"""继承。
父类  子类

继承如何表示：
class 子类名(父类名):
    pass


子类可以实现自己独有的方法。

子类可以覆盖父类的方法。 ==》 重写

super() 超继承： 使用父类当中的方法。

"""

class Phone:
    """手机"""

    def __init__(self, number):
        self.number = number

    def call(self, to, recorded=False):
        """打电话"""
        print(" {} 给 {} 打电话。。".format(self.number, to))

        if recorded:
            self.record()

    def record(self):
        """录音"""
        print("{} 正在录音".format(self.number))


class SmartPhone(Phone):
    """智能手机"""

    def __init__(self, number, brand):
        self.number = number
        self.brand = brand

    def watch_movie(self, name):
        print("正在看电影{}".format(name))


class Iphone(SmartPhone):
    # brand = '苹果'

    def __init__(self, number):
        super().__init__(number, '苹果')
        # self.number = number
        # self.brand = "苹果"

    def face_time(self):
        """录屏，直播"""
        print("{} 正在直播".format(self.number))

    def call(self, to, recorded=False, face=False):
        """打电话既可以录音，也可以facetime"""
        # print(" {} 给 {} 打电话。。".format(self.number, to))
        #
        # if recorded:
        #     self.record()

        super().call(to, recorded=False)

        if face:
            self.face_time()



# normal_phone = Phone('1')
# print(normal_phone.record())
#
# # 父类当中不能调用子类方法。
# # normal_phone.watch_movie("红海行动")
#
# smart_phone = SmartPhone("2")
# print(smart_phone.record())
# print(smart_phone.number)
# smart_phone.watch_movie('小偷家族')


# 当子类和父类具有同样的方法或者属性的时候。
# 父类还是用父类的， 子类不再有父类的，而是用自己的。
# normal = Phone("1")
# smart = SmartPhone(2, '华为')

# 重写例子2
iphone = Iphone('苹果5')
iphone.call('开始', face=True)

# smart = SmartPhone("123", '华为')
# smart.call('阿东', face=True)
