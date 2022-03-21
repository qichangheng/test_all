

def congratulate_offer(offer_name, money):
    """庆祝拿到 offer """
    print("{}拿到了一个{}k 的 offer.".format(offer_name, money))
    # 请客
    eat(offer_name, '小龙虾')


# eat('热水', '小龙虾')
def eat(name, food):
    print("{}喜欢吃食物：{}".format(name, food))


congratulate_offer('小王子', 22)