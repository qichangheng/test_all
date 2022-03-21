class Phone:
    def __init__(self, brand):
        self.brand = brand


# 继承，表示你可以去使用父类的属性和方法，
class Iphone(Phone):
    def __init__(self):
        # 你就已经有自我。

        super().__init__("苹果")
        print(self)
        # self.brand = "苹果"

iphone = Iphone()
# print(iphone.brand)
print(iphone.brand)