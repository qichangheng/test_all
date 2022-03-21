class YiFu:

    def __init__(self, brand, model, size):
        pass


    def sell(self, param):
        print("商场正在麦衣服")
        print("卖不出去，打9折")
        print("还卖不出去，打骨折")


class GirlYiFu(YiFu):
    def __init__(self):
        pass

    def sell(self):
        # super() =  YiFu('', '', '')

        super().sell('data')

        print("女装独特的卖衣服的技巧")
        print("你买我的衣服，我还给你钱")


# normal = YiFu()
# normal.sell()

nvzhuang = GirlYiFu()
nvzhuang.sell()






