class Phone:

    def __init__(self, number):
        self.number = number


phone = Phone('137')

# # 对象.属性
# print(phone.number)
#
# # 动态获取属性
# print(getattr(phone, 'number'))

# 动态获取不存在的属性
# print(phone.brand)
# 可以加上 default 参数，设置默认值。当没有该属性的属性，不会报错。
# 而是返回默认值。
# print(getattr(phone, 'brand', default='苹果'))

# 动态属性，属性名 == 变量

prop_name = 'brand'
# phone.prop_name
# phone.brand
print(getattr(phone, prop_name, '苹果'))
print(phone.brand)

# 设置 set 属性。
# print(phone.number)
# setattr(phone, 'number', '155')
# # phone.number = 155
# phone.color = '白色'
# print(phone.number)

