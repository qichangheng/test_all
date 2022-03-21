# if 的嵌套

a = 8
b = 6

dalao = ['yuz', '牛腩', '罗哥', "小猪"]
real_dalao = '小王子'

if a > b:
    print("大于，可是开始吃瓜了")
    if real_dalao in dalao:
        print("大佬出来了，大家快来学习")

    else:
        print("这是假大佬")
else:
    print("小于等于，没有瓜吃")