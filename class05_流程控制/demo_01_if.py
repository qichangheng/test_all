#########
######### if 的表示

# if 条件表达式 :
#     (缩进)条件满足以后要运行的代代
# elif 条件表达式2:
        # 代码2
# elif 条件表达3：
        # 代码 3
# else  (没有表达式， 剩下所有的情况):
#     （缩进）else 条件满足要运行的代码
# 当其中的一个条件满足，其他的条件分支自动屏蔽，不会再运行


# 例子：
######## 遇到冒号要缩进
# 缩进：1个缩进用4个空格
# 4个空格并不等于 1 个 tab

# 在 一个 if 表达式中，if..elif..else... 如果运行了其中的一个条件，
# 其他的分支就不会再运行了。
# if 4 > 3:
#     print("我比牛腩大。。")
# elif 4 != 3:
#     print("不可能")
# elif 4 == 5:
#     print("abc")
# else:
#     print("想得美")


# 练习1：
# yuz_age = input("雨泽的年龄：")
# xiaowangzi_age = input("小王子的年龄：")
#
# if int(yuz_age) > int(xiaowangzi_age):
#     print("29期的人每个给雨泽 10 块钱")
# elif int(yuz_age) < int(xiaowangzi_age):
#     print("雨泽给29期总共 10 块钱")


# 运算方式
if 'yuz' in 'yuz wang':
    print("我是yuz")


# if 变量
# "", [], {}, 0, False, () 代表的就是条件不成立
if 1:
    print("这是1")

if "":
    print("这是 空字符串")

if True:
    print("这是True")


